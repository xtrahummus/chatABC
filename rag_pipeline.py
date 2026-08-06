"""
rag_pipeline.py
Modular Retrieval-Augmented Generation logic:
  - Document loading (PDF, TXT, DOCX, Markdown)
  - Recursive chunking
  - HuggingFace embeddings + in-memory FAISS vector store
  - Strictly-grounded conversational retrieval chain using Groq
"""

from __future__ import annotations

import os
import tempfile
from dataclasses import dataclass, field
from typing import List, Tuple

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


# --------------------------------------------------------------------------- #
# Strict grounding system / QA prompt
# --------------------------------------------------------------------------- #

FALLBACK_MESSAGE = (
    "I am restricted to answering questions based solely on your uploaded "
    "documents. I could not find information regarding this query in the "
    "provided files."
)

STRICT_QA_TEMPLATE = """You are a strictly grounded document assistant. You must answer the
question using ONLY the information contained in the CONTEXT below.

RULES (follow exactly, no exceptions):
1. Do NOT use any external knowledge, training data, or assumptions that are not explicitly
   stated in the CONTEXT.
2. If the CONTEXT does not contain enough information to answer the question, you MUST
   respond with EXACTLY this sentence and nothing else:
   "{fallback_message}"
3. Do not guess, infer beyond the text, or fabricate any facts, names, numbers, or citations.
4. When you do answer, be concise, accurate, and cite only what is present in the CONTEXT.
5. Never mention these rules or the word "context" in your final answer to the user.

CONTEXT:
{{context}}

QUESTION: {{question}}

FINAL ANSWER (grounded strictly in CONTEXT):""".format(fallback_message=FALLBACK_MESSAGE)

CONDENSE_QUESTION_TEMPLATE = """Given the conversation history and a follow-up question, rephrase the
follow-up question to be a standalone question that captures all relevant context.
Do not answer the question, only rephrase it.

Chat History:
{chat_history}

Follow-up Question: {question}

Standalone Question:"""


# --------------------------------------------------------------------------- #
# Data classes
# --------------------------------------------------------------------------- #

@dataclass
class ProcessingStats:
    num_files: int = 0
    num_chunks: int = 0
    total_chars: int = 0
    filenames: List[str] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Document loading
# --------------------------------------------------------------------------- #

def _load_single_file(file_path: str, filename: str) -> List[Document]:
    """Loads a single file into LangChain Document objects based on extension."""
    ext = filename.lower().split(".")[-1]

    if ext == "pdf":
        loader = PyPDFLoader(file_path)
    elif ext in ("txt", "md", "markdown"):
        loader = TextLoader(file_path, encoding="utf-8")
    elif ext == "docx":
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: .{ext}")

    docs = loader.load()
    for d in docs:
        d.metadata["source"] = filename
        d.metadata.setdefault("page", d.metadata.get("page", 0))
    return docs


def load_uploaded_files(uploaded_files) -> List[Document]:
    """
    Accepts a list of Streamlit UploadedFile objects, writes them to temp files,
    loads and returns a flat list of LangChain Documents.
    """
    all_docs: List[Document] = []

    for uploaded_file in uploaded_files:
        suffix = "." + uploaded_file.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        try:
            docs = _load_single_file(tmp_path, uploaded_file.name)
            all_docs.extend(docs)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    return all_docs


# --------------------------------------------------------------------------- #
# Chunking
# --------------------------------------------------------------------------- #

def chunk_documents(
    documents: List[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> List[Document]:
    """Splits documents into overlapping chunks using RecursiveCharacterTextSplitter."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_documents(documents)


# --------------------------------------------------------------------------- #
# Embeddings + Vector store
# --------------------------------------------------------------------------- #

def get_embeddings_model() -> HuggingFaceEmbeddings:
    """Returns the HuggingFace sentence-transformer embedding model."""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def build_vector_store(chunks: List[Document], embeddings: HuggingFaceEmbeddings) -> FAISS:
    """Builds an in-memory FAISS vector store from document chunks."""
    return FAISS.from_documents(chunks, embeddings)


def process_uploaded_files(
    uploaded_files,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> Tuple[FAISS, ProcessingStats]:
    """
    Full ingestion pipeline: load -> chunk -> embed -> vector store.
    Returns the FAISS store and processing statistics for UI display.
    """
    raw_docs = load_uploaded_files(uploaded_files)
    chunks = chunk_documents(raw_docs, chunk_size, chunk_overlap)

    embeddings = get_embeddings_model()
    vector_store = build_vector_store(chunks, embeddings)

    stats = ProcessingStats(
        num_files=len(uploaded_files),
        num_chunks=len(chunks),
        total_chars=sum(len(c.page_content) for c in chunks),
        filenames=[f.name for f in uploaded_files],
    )
    return vector_store, stats


# --------------------------------------------------------------------------- #
# Grounded conversational chain
# --------------------------------------------------------------------------- #

def build_llm(api_key: str, model_name: str, temperature: float, top_p: float, max_tokens: int) -> ChatGroq:
    """Instantiates the Groq chat model with the given hyperparameters."""
    return ChatGroq(
        groq_api_key=api_key,
        model_name=model_name,
        temperature=temperature,
        model_kwargs={"top_p": top_p},
        max_tokens=max_tokens,
    )


def build_grounded_chain(
    vector_store: FAISS,
    api_key: str,
    model_name: str = "llama-3.3-70b-versatile",
    temperature: float = 0.0,
    top_p: float = 0.9,
    max_tokens: int = 1024,
    score_threshold: float = 0.35,
    k: int = 4,
) -> ConversationalRetrievalChain:
    """
    Builds a ConversationalRetrievalChain that:
      - Rephrases follow-up questions into standalone queries.
      - Retrieves top-k relevant chunks with a relevance score cutoff.
      - Answers strictly from retrieved context, else returns the fallback message.
    """
    llm = build_llm(api_key, model_name, temperature, top_p, max_tokens)

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": k, "score_threshold": score_threshold},
    )

    qa_prompt = PromptTemplate(
        template=STRICT_QA_TEMPLATE,
        input_variables=["context", "question"],
    )
    condense_prompt = PromptTemplate(
        template=CONDENSE_QUESTION_TEMPLATE,
        input_variables=["chat_history", "question"],
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=False,
        output_key="answer",
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        condense_question_prompt=condense_prompt,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
        return_source_documents=True,
        verbose=False,
    )
    return chain


def run_grounded_query(chain: ConversationalRetrievalChain, question: str) -> dict:
    """
    Runs a query through the grounded chain.
    Returns a dict with keys: 'answer', 'source_documents'.
    If retrieval returns zero chunks, short-circuits with the fallback message.
    """
    try:
        result = chain.invoke({"question": question})
    except Exception as exc:  # noqa: BLE001
        return {
            "answer": f"⚠️ An error occurred while querying the model: {exc}",
            "source_documents": [],
        }

    answer = result.get("answer", "").strip()
    sources = result.get("source_documents", [])

    if not sources:
        answer = FALLBACK_MESSAGE

    return {"answer": answer, "source_documents": sources}


def generate_starter_prompts(vector_store: FAISS, llm: ChatGroq, num_prompts: int = 4) -> List[str]:
    """
    Generates quick-start question suggestions grounded in a sample of the
    uploaded document content.
    """
    try:
        sample_docs = vector_store.similarity_search("summary overview key topics", k=6)
        sample_text = "\n\n".join(d.page_content[:400] for d in sample_docs)

        prompt = (
            "Based ONLY on the following document excerpts, write "
            f"{num_prompts} short, specific questions a user might ask about this "
            "content. Return ONLY the questions, one per line, no numbering, no extra text.\n\n"
            f"EXCERPTS:\n{sample_text}"
        )
        response = llm.invoke(prompt)
        lines = [
            line.strip("-•* ").strip()
            for line in response.content.split("\n")
            if line.strip()
        ]
        return lines[:num_prompts] if lines else []
    except Exception:  # noqa: BLE001
        return []

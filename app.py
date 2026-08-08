"""
app.py
Main Streamlit application for the RAG Chatbot — a strictly document-grounded
Retrieval-Augmented Generation assistant.
"""

import time
import streamlit as st

from styles import (
    inject_custom_css,
    render_hero_header,
    render_guardrail_badge,
    render_connection_badge,
    render_source_chunk,
)
from rag_pipeline import (
    process_uploaded_files,
    build_grounded_chain,
    run_grounded_query,
    generate_starter_prompts,
    build_llm,
    FALLBACK_MESSAGE,
)

# --------------------------------------------------------------------------- #
# Page config (must be first Streamlit call)
# --------------------------------------------------------------------------- #

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()


# --------------------------------------------------------------------------- #
# Session state initialization
# --------------------------------------------------------------------------- #

def init_session_state():
    defaults = {
        "messages": [],                # list[{"role": ..., "content": ..., "sources": [...]}]
        "vector_store": None,
        "chain": None,
        "processing_stats": None,
        "api_key_valid": False,
        "groq_api_key": "",
        "starter_prompts": [],
        "pending_prompt": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()


# --------------------------------------------------------------------------- #
# Sidebar
# --------------------------------------------------------------------------- #

with st.sidebar:
    st.markdown('<div class="sidebar-section-title">API Access</div>', unsafe_allow_html=True)

    default_key = ""
    try:
        if "GROQ_API_KEY" in st.secrets:
            default_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        default_key = ""

    api_key_input = st.text_input(
        "Groq API Key",
        value=st.session_state.groq_api_key or default_key,
        type="password",
        placeholder="Enter your API key",
        label_visibility="collapsed",
        help="Your key is kept only in this session and is never displayed.",
    )
    st.session_state.groq_api_key = api_key_input
    st.session_state.api_key_valid = bool(api_key_input)

    # Neutral connection indicator — reveals connection state only, never the key itself.
    render_connection_badge(st.session_state.api_key_valid)

    st.markdown('<div class="sidebar-section-title">Model Settings</div>', unsafe_allow_html=True)

    model_name = st.selectbox(
        "Model",
        options=["llama-3.3-70b-versatile", "mixtral-8x7b-32768", "llama-3.1-8b-instant"],
        index=0,
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.0, 0.05,
                             help="Kept low by default to minimize hallucination risk.")
    top_p = st.slider("Top-P", 0.0, 1.0, 0.9, 0.05)
    max_tokens = st.slider("Max Tokens", 128, 4096, 1024, 64)

    st.markdown('<div class="sidebar-section-title">Document Management</div>', unsafe_allow_html=True)

    uploaded_files = st.file_uploader(
        "Upload documents",
        type=["pdf", "txt", "docx", "md"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    process_btn = st.button("Process Documents", use_container_width=True)

    if process_btn:
        if not uploaded_files:
            st.warning("Please upload at least one document first.")
        elif not st.session_state.api_key_valid:
            st.error("Please enter a valid Groq API key first.")
        else:
            progress_bar = st.progress(0, text="Loading documents...")
            try:
                progress_bar.progress(20, text="Reading & chunking documents...")
                vector_store, stats = process_uploaded_files(uploaded_files)
                progress_bar.progress(70, text="Building embeddings & FAISS index...")

                chain = build_grounded_chain(
                    vector_store,
                    api_key=st.session_state.groq_api_key,
                    model_name=model_name,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                )
                progress_bar.progress(90, text="Generating starter prompts...")

                llm = build_llm(st.session_state.groq_api_key, model_name, temperature, top_p, max_tokens)
                starter_prompts = generate_starter_prompts(vector_store, llm)

                st.session_state.vector_store = vector_store
                st.session_state.chain = chain
                st.session_state.processing_stats = stats
                st.session_state.starter_prompts = starter_prompts
                st.session_state.messages = []

                progress_bar.progress(100, text="Done!")
                time.sleep(0.4)
                progress_bar.empty()
                st.success(f"Processed {stats.num_files} file(s) into {stats.num_chunks} chunks.")
            except Exception as exc:  # noqa: BLE001
                progress_bar.empty()
                st.error(f"Processing failed: {exc}")

    if st.session_state.processing_stats:
        stats = st.session_state.processing_stats
        c1, c2 = st.columns(2)
        c1.metric("Files", stats.num_files)
        c2.metric("Chunks", stats.num_chunks)
        with st.expander("Loaded files"):
            for fname in stats.filenames:
                st.markdown(f"- {fname}")

    st.markdown('<div class="sidebar-section-title">Guardrails</div>', unsafe_allow_html=True)
    render_guardrail_badge()
    st.caption("Answers are restricted to retrieved document context only. No outside knowledge is used.")

    st.markdown('<div class="sidebar-section-title">Session</div>', unsafe_allow_html=True)
    if st.button("Reset Chat & Vector Store", use_container_width=True):
        for key in ["messages", "vector_store", "chain", "processing_stats", "starter_prompts", "pending_prompt"]:
            st.session_state[key] = [] if key in ("messages", "starter_prompts") else None
        st.rerun()


# --------------------------------------------------------------------------- #
# Main area
# --------------------------------------------------------------------------- #

render_hero_header()

if not st.session_state.chain:
    st.info(
        "Upload one or more documents (PDF, TXT, DOCX, or Markdown) in the sidebar and click "
        "**Process Documents** to begin. All answers will be strictly grounded in your uploaded files."
    )
else:
    # Starter prompt buttons
    if st.session_state.starter_prompts and not st.session_state.messages:
        st.markdown('<div class="sidebar-section-title">Suggested Questions</div>', unsafe_allow_html=True)
        cols = st.columns(min(len(st.session_state.starter_prompts), 4))
        for i, prompt_text in enumerate(st.session_state.starter_prompts):
            with cols[i % len(cols)]:
                if st.button(prompt_text, key=f"starter_{i}", use_container_width=True):
                    st.session_state.pending_prompt = prompt_text

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander(f"View {len(msg['sources'])} source citation(s)"):
                for src in msg["sources"]:
                    st.markdown(
                        render_source_chunk(src["filename"], src["page"], src["text"]),
                        unsafe_allow_html=True,
                    )

# Chat input
user_input = st.chat_input(
    "Ask a question about your documents..." if st.session_state.chain else "Process documents first...",
    disabled=st.session_state.chain is None,
)

# Handle starter-prompt click as if it were typed input
if st.session_state.pending_prompt and not user_input:
    user_input = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if user_input and st.session_state.chain:
    st.session_state.messages.append({"role": "user", "content": user_input, "sources": []})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        with st.spinner("Retrieving grounded context..."):
            result = run_grounded_query(st.session_state.chain, user_input)

        answer = result["answer"]
        source_docs = result["source_documents"]

        # Simple streaming animation
        streamed = ""
        for word in answer.split(" "):
            streamed += word + " "
            placeholder.markdown(streamed + "▌")
            time.sleep(0.012)
        placeholder.markdown(streamed.strip())

        sources_payload = []
        if source_docs and answer != FALLBACK_MESSAGE:
            with st.expander(f"View {len(source_docs)} source citation(s)"):
                for doc in source_docs:
                    filename = doc.metadata.get("source", "unknown")
                    page = doc.metadata.get("page", "N/A")
                    text = doc.page_content[:500]
                    st.markdown(render_source_chunk(filename, page, text), unsafe_allow_html=True)
                    sources_payload.append({"filename": filename, "page": page, "text": text})

    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources_payload})

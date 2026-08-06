# 🔮 NeuralDocs RAG — Strictly Grounded RAG Chatbot

A visually polished, strictly grounded Retrieval-Augmented Generation chatbot built with
**Streamlit + LangChain + Groq + FAISS**. The assistant answers questions **only** from
the content of documents you upload — if the answer isn't in your files, it says so
instead of guessing.

## ✨ Features

- **Zero-hallucination guardrails** — prompt-level + retrieval-level enforcement, with a
  clean fallback message when no relevant context is found.
- **Multi-format ingestion** — PDF, TXT, DOCX, and Markdown.
- **Conversational memory** — follow-up questions are rephrased into standalone queries
  before retrieval.
- **Source citations** — collapsible expanders showing exact chunks, filenames, and pages.
- **Dark glassmorphic UI** — custom CSS, gradient header, animated chat bubbles.
- **Tunable hyperparameters** — temperature, top-p, max tokens, all sidebar-controlled.
- **Dynamic starter prompts** — auto-generated from your uploaded documents.

## 📁 Project Structure

```text
rag-streamlit-app/
├── .streamlit/
│   └── config.toml   # Theme & server settings
├── app.py             # Main Streamlit app & layout
├── rag_pipeline.py    # RAG logic: loading, chunking, embeddings, grounded chain
├── styles.py          # Custom CSS injections
├── requirements.txt   # Pinned dependencies
├── colab_setup.py     # Google Colab launch helper
└── README.md
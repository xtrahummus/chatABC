# 🔮 RAG Chatbot — Strictly Grounded RAG Chatbot

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
- **Frosted white glassmorphic UI** — custom CSS, translucent panels, glowing accents,
  animated chat bubbles.
- **Tunable hyperparameters** — temperature, top-p, max tokens, all sidebar-controlled.
- **Dynamic starter prompts** — auto-generated from your uploaded documents.

## 📁 Project Structure

```text
rag-streamlit-app/
├── .streamlit/
│   └── config.toml   # Light theme & server settings
├── app.py             # Main Streamlit app & layout
├── rag_pipeline.py    # RAG logic: loading, chunking, embeddings, grounded chain
├── styles.py           # Custom CSS injections (white glassmorphism)
├── requirements.txt   # Pinned dependencies
├── colab_setup.py     # Google Colab launch helper
└── README.md
```

## 🔑 Getting a Groq API Key

1. Sign up at [console.groq.com](https://console.groq.com).
2. Create an API key from the dashboard.
3. Paste it into the sidebar's **API Key** field, or set it as a Streamlit secret (see below).

## ☁️ Deploying to Streamlit Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and create a new app pointing
   at `app.py` on your `main` branch.
3. In **App settings → Secrets**, add:

   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```

4. Deploy. The app will automatically pick up the key from `st.secrets`, or users can
   paste their own key in the sidebar at runtime.

## ⚙️ Local Development

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 🧪 Running in Google Colab

See `colab_setup.py` for a localtunnel/ngrok launch helper if you want to test the app
inside a Colab notebook.

## 🛡️ How Grounding Is Enforced

1. **Retrieval thresholding** — only chunks above a similarity-score cutoff are returned;
   if none qualify, the app returns the fallback message directly.
2. **Strict QA prompt** — instructs the model to answer only from provided context and to
   emit the exact fallback sentence otherwise.
3. **Belt-and-braces check** — even if the LLM strays, the app verifies source documents
   were actually retrieved before treating the answer as valid content.

## 📄 License

MIT — use freely for personal or commercial projects.

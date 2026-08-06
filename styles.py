"""
styles.py
Custom CSS injections for a frosted white glassmorphic RAG chatbot UI.
"""

import streamlit as st


def inject_custom_css() -> None:
    """Injects the full white-glassmorphic custom CSS theme into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* ---------- GLOBAL ---------- */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        /* Ambient glowing background mesh */
        .stApp {
            background: 
                radial-gradient(circle at 15% 15%, rgba(255, 255, 255, 0.95), transparent 45%),
                radial-gradient(circle at 85% 20%, rgba(220, 235, 255, 0.7), transparent 40%),
                radial-gradient(circle at 50% 80%, rgba(240, 243, 250, 0.9), transparent 50%),
                linear-gradient(135deg, #eef2f7 0%, #e2e8f0 100%);
            background-attachment: fixed;
            color: #1E293B;
        }

        /* Hide default Streamlit chrome */
        #MainMenu, footer, header {visibility: hidden;}

        /* ---------- SCROLLBAR ---------- */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        }

        /* ---------- HERO HEADER (FROSTED WHITE GLASS) ---------- */
        .hero-header {
            padding: 1.8rem 2.2rem;
            border-radius: 24px;
            margin-bottom: 1.5rem;
            background: rgba(255, 255, 255, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.75);
            box-shadow: 
                0 20px 40px rgba(0, 0, 0, 0.04),
                0 0 30px rgba(255, 255, 255, 0.8),
                inset 0 0 25px rgba(255, 255, 255, 0.6);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            position: relative;
            overflow: hidden;
        }
        
        /* Subtle rotating white glow animation */
        .hero-header::before {
            content: "";
            position: absolute;
            top: -50%; left: -50%;
            width: 200%; height: 200%;
            background: conic-gradient(from 0deg, transparent, rgba(255, 255, 255, 0.5), transparent 40%);
            animation: rotateGlow 14s linear infinite;
        }
        @keyframes rotateGlow { 100% { transform: rotate(360deg); } }

        .hero-title {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #0F172A 0%, #334155 50%, #475569 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
            position: relative;
            z-index: 1;
            letter-spacing: -0.03em;
            text-shadow: 0 10px 20px rgba(255, 255, 255, 0.5);
        }
        .hero-subtitle {
            color: #64748B;
            font-size: 0.98rem;
            font-weight: 500;
            margin-top: 0.4rem;
            position: relative;
            z-index: 1;
        }

        /* ---------- BADGE ---------- */
        .guardrail-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.55);
            border: 1px solid rgba(16, 185, 129, 0.35);
            color: #059669;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            margin-bottom: 0.8rem;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.08), inset 0 0 10px rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(12px);
        }
        .guardrail-dot {
            width: 8px; height: 8px;
            border-radius: 50%;
            background: #10B981;
            box-shadow: 0 0 10px #10B981, 0 0 20px #10B981;
            animation: pulse 1.6s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.7); }
        }

        /* ---------- GLASS CARDS ---------- */
        .glass-card {
            background: rgba(255, 255, 255, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.7);
            border-radius: 20px;
            padding: 1.2rem 1.4rem;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03), inset 0 0 15px rgba(255, 255, 255, 0.5);
            margin-bottom: 1rem;
        }

        /* ---------- SIDEBAR (WHITE GLASS) ---------- */
        section[data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.35);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            border-right: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 5px 0 25px rgba(0, 0, 0, 0.02);
        }
        section[data-testid="stSidebar"] .stTextInput input,
        section[data-testid="stSidebar"] .stNumberInput input {
            background: rgba(255, 255, 255, 0.65);
            border: 1px solid rgba(255, 255, 255, 0.9);
            color: #1E293B;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02);
        }
        section[data-testid="stSidebar"] .stTextInput input:focus {
            border-color: rgba(99, 102, 241, 0.5);
            box-shadow: 0 0 15px rgba(255, 255, 255, 0.9), 0 0 10px rgba(99, 102, 241, 0.2);
        }

        .sidebar-section-title {
            font-size: 0.76rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.09em;
            color: #475569;
            margin: 1.2rem 0 0.6rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.6);
            padding-bottom: 0.4rem;
        }

        /* ---------- CHAT BUBBLES ---------- */
        div[data-testid="stChatMessage"] {
            border-radius: 20px;
            padding: 0.8rem 1rem;
            margin-bottom: 0.8rem;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            animation: fadeInUp 0.35s ease;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* User Bubble - Frosted Pure White */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
            background: rgba(255, 255, 255, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.95);
            box-shadow: 
                0 10px 25px rgba(0, 0, 0, 0.03),
                0 0 20px rgba(255, 255, 255, 0.8);
            color: #0F172A;
        }

        /* Assistant Bubble - Soft Semi-Transparent Gloss */
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
            background: rgba(255, 255, 255, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.75);
            box-shadow: 
                0 12px 30px rgba(0, 0, 0, 0.025),
                inset 0 0 15px rgba(255, 255, 255, 0.6);
            color: #1E293B;
        }

        /* ---------- SOURCE CHUNKS ---------- */
        .source-chunk {
            background: rgba(255, 255, 255, 0.65);
            border-left: 3px solid #94A3B8;
            border: 1px solid rgba(255, 255, 255, 0.8);
            padding: 0.7rem 0.9rem;
            border-radius: 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: #334155;
            margin-bottom: 0.6rem;
            white-space: pre-wrap;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
        }
        .source-meta {
            font-size: 0.72rem;
            color: #64748B;
            font-weight: 700;
            margin-bottom: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }

        /* ---------- BUTTONS (GLOWING GLASS) ---------- */
        .stButton > button {
            border-radius: 14px;
            border: 1px solid rgba(255, 255, 255, 0.85);
            background: rgba(255, 255, 255, 0.5);
            color: #1E293B;
            backdrop-filter: blur(10px);
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        }
        .stButton > button:hover {
            border-color: rgba(255, 255, 255, 1);
            background: rgba(255, 255, 255, 0.85);
            box-shadow: 
                0 8px 25px rgba(0, 0, 0, 0.06),
                0 0 20px rgba(255, 255, 255, 0.9);
            transform: translateY(-2px);
            color: #0F172A;
        }

        /* ---------- FILE UPLOADER ---------- */
        section[data-testid="stFileUploaderDropzone"] {
            background: rgba(255, 255, 255, 0.35);
            border: 2px dashed rgba(255, 255, 255, 0.8);
            border-radius: 18px;
            backdrop-filter: blur(10px);
            box-shadow: inset 0 0 20px rgba(255, 255, 255, 0.4);
            transition: all 0.2s ease;
        }
        section[data-testid="stFileUploaderDropzone"]:hover {
            border-color: rgba(255, 255, 255, 1);
            background: rgba(255, 255, 255, 0.55);
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
        }

        /* ---------- STATUS PILLS ---------- */
        .status-pill-ok {
            color: #059669; font-weight: 700; font-size: 0.82rem;
        }
        .status-pill-bad {
            color: #DC2626; font-weight: 700; font-size: 0.82rem;
        }
        .status-pill-warn {
            color: #D97706; font-weight: 700; font-size: 0.82rem;
        }

        /* ---------- METRIC CARDS ---------- */
        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.8);
            border-radius: 16px;
            padding: 0.7rem 0.9rem 0.4rem 0.9rem;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02);
        }

        /* ---------- CHAT INPUT ---------- */
        .stChatInputContainer, div[data-testid="stChatInput"] {
            border-radius: 20px !important;
            background: rgba(255, 255, 255, 0.6) !important;
            border: 1px solid rgba(255, 255, 255, 0.9) !important;
            backdrop-filter: blur(20px) !important;
            box-shadow: 
                0 10px 30px rgba(0, 0, 0, 0.04),
                0 0 25px rgba(255, 255, 255, 0.8) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero_header() -> None:
    """Renders the frosted white-glass hero header block."""
    st.markdown(
        """
        <div class="hero-header">
            <div class="hero-title">🔮 NeuralDocs RAG</div>
            <div class="hero-subtitle">
                Strictly grounded document intelligence — powered by Groq + LangChain + FAISS
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_guardrail_badge() -> None:
    """Renders the 'Strict Document Grounding Enabled' badge."""
    st.markdown(
        """
        <div class="guardrail-badge">
            <span class="guardrail-dot"></span>
            Strict Document Grounding Enabled
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_source_chunk(source_name: str, page: str, text: str) -> str:
    """Returns HTML for a single source citation chunk inside a translucent white card."""
    return f"""
    <div class="source-chunk">
        <div class="source-meta">{source_name} · page {page}</div>
        {text}
    </div>
    """
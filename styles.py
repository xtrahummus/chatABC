"""
styles.py
A cohesive "liquid glass" design system: clear, boxy, frosted-white panels,
one neutral palette, one accent color, consistent radii / blur / shadow
tokens reused across every surface (header, sidebar, cards, chat, buttons,
inputs, expanders).
"""

import streamlit as st


def inject_custom_css() -> None:
    """Injects the full liquid-glass design system into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* ============================================================ */
        /* DESIGN TOKENS — single source of truth, reused everywhere     */
        /* ============================================================ */
        :root {
            --accent: 79, 70, 229;            /* indigo-600, the ONE accent color */
            --accent-solid: #4F46E5;
            --ink: #12172B;                   /* primary text */
            --ink-muted: #5B6478;             /* secondary text */
            --ink-faint: #8890A0;             /* tertiary / captions */

            --glass-fill: 255, 255, 255;      /* base glass tint (white) */
            --glass-a1: 0.55;                 /* strong panel opacity */
            --glass-a2: 0.38;                 /* medium panel opacity */
            --glass-a3: 0.22;                 /* subtle panel opacity */

            --border-a1: 0.55;
            --border-a2: 0.35;

            --radius-xl: 26px;
            --radius-lg: 20px;
            --radius-md: 14px;
            --radius-sm: 10px;

            --blur-strong: blur(28px) saturate(180%);
            --blur-med: blur(20px) saturate(160%);
            --blur-soft: blur(14px) saturate(140%);

            --shadow-ambient: 0 12px 40px rgba(18, 23, 43, 0.08);
            --shadow-lift: 0 18px 48px rgba(18, 23, 43, 0.12);
        }

        /* ============================================================ */
        /* GLOBAL                                                        */
        /* ============================================================ */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--ink);
        }

        /* Calm, mostly-neutral backdrop — two soft accent blooms, nothing more */
        .stApp {
            background:
                radial-gradient(circle at 12% 8%, rgba(var(--accent), 0.10), transparent 42%),
                radial-gradient(circle at 88% 82%, rgba(var(--accent), 0.07), transparent 46%),
                linear-gradient(160deg, #F4F6FB 0%, #E9EDF5 55%, #E3E8F2 100%);
            background-attachment: fixed;
            color: var(--ink);
        }

        #MainMenu, footer, header {visibility: hidden;}

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(var(--glass-fill), 0.9);
            border: 1px solid rgba(255,255,255,1);
            border-radius: 10px;
        }

        /* ============================================================ */
        /* CORE GLASS SURFACE — the one panel style, reused everywhere   */
        /* ============================================================ */
        .lg-panel {
            position: relative;
            background: rgba(var(--glass-fill), var(--glass-a1));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-radius: var(--radius-lg);
            backdrop-filter: var(--blur-med);
            -webkit-backdrop-filter: var(--blur-med);
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.8);
            overflow: hidden;
        }
        /* Specular sheen along the top edge — the "liquid" highlight */
        .lg-panel::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 42%;
            background: linear-gradient(180deg, rgba(255,255,255,0.55), transparent);
            pointer-events: none;
        }

        /* ---------- HERO HEADER ---------- */
        .hero-header {
            position: relative;
            padding: 2rem 2.4rem;
            border-radius: var(--radius-xl);
            margin-bottom: 1.6rem;
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            backdrop-filter: var(--blur-strong);
            -webkit-backdrop-filter: var(--blur-strong);
            box-shadow: var(--shadow-lift), inset 0 1px 0 rgba(255,255,255,0.85);
            overflow: hidden;
        }
        .hero-header::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 55%;
            background: linear-gradient(180deg, rgba(255,255,255,0.6), transparent);
            pointer-events: none;
        }
        .hero-header::after {
            content: "";
            position: absolute;
            top: -60%; right: -20%;
            width: 60%; height: 220%;
            background: radial-gradient(circle, rgba(var(--accent), 0.10), transparent 70%);
            pointer-events: none;
        }

        .hero-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--accent-solid);
            position: relative;
            z-index: 1;
        }
        .hero-title {
            font-size: 2.35rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: var(--ink);
            margin: 0.35rem 0 0.3rem 0;
            position: relative;
            z-index: 1;
        }
        .hero-subtitle {
            color: var(--ink-muted);
            font-size: 0.98rem;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }

        /* ---------- BADGE ---------- */
        .guardrail-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.42rem 0.95rem;
            border-radius: var(--radius-sm);
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: 0 6px 18px rgba(16, 163, 74, 0.10), inset 0 1px 0 rgba(255,255,255,0.75);
            color: #0E7A3F;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.01em;
            margin-bottom: 0.7rem;
        }
        .guardrail-dot {
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #16A34A;
            box-shadow: 0 0 6px #16A34A, 0 0 12px rgba(22, 163, 74, 0.6);
            animation: pulse 1.8s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.45; transform: scale(0.7); }
        }

        /* Neutral connection-status pill (used for API key state — never reveals the key) */
        .conn-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.35rem 0.8rem;
            border-radius: var(--radius-sm);
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.01em;
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
        }
        .conn-badge.is-on {
            background: rgba(22, 163, 74, 0.10);
            color: #0E7A3F;
        }
        .conn-badge.is-off {
            background: rgba(220, 38, 38, 0.08);
            color: #B91C1C;
        }
        .conn-dot {
            width: 6px; height: 6px;
            border-radius: 50%;
        }
        .conn-badge.is-on .conn-dot { background: #16A34A; box-shadow: 0 0 6px rgba(22,163,74,0.7); }
        .conn-badge.is-off .conn-dot { background: #DC2626; box-shadow: 0 0 6px rgba(220,38,38,0.5); }

        /* ---------- GLASS CARDS ---------- */
        .glass-card {
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-radius: var(--radius-lg);
            padding: 1.1rem 1.3rem;
            backdrop-filter: var(--blur-med);
            -webkit-backdrop-filter: var(--blur-med);
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.7);
            margin-bottom: 0.9rem;
        }

        /* ---------- SIDEBAR ---------- */
        section[data-testid="stSidebar"] {
            background: rgba(var(--glass-fill), 0.30);
            backdrop-filter: var(--blur-strong);
            -webkit-backdrop-filter: var(--blur-strong);
            border-right: 1px solid rgba(255, 255, 255, 0.5);
        }
        section[data-testid="stSidebar"] > div {
            padding-top: 1.2rem;
        }

        section[data-testid="stSidebar"] .stTextInput input,
        section[data-testid="stSidebar"] .stNumberInput input,
        section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
            background: rgba(var(--glass-fill), 0.60) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            color: var(--ink) !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }
        section[data-testid="stSidebar"] .stTextInput input:focus,
        section[data-testid="stSidebar"] .stNumberInput input:focus {
            border-color: rgba(var(--accent), 0.55) !important;
            box-shadow: 0 0 0 3px rgba(var(--accent), 0.14) !important;
        }

        .sidebar-section-title {
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.10em;
            color: var(--ink-muted);
            margin: 1.3rem 0 0.6rem 0;
            padding-bottom: 0.45rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.55);
        }
        .sidebar-section-title:first-of-type { margin-top: 0.2rem; }

        /* ---------- CHAT BUBBLES ---------- */
        div[data-testid="stChatMessage"] {
            border-radius: var(--radius-lg);
            padding: 0.9rem 1.1rem;
            margin-bottom: 0.85rem;
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            backdrop-filter: var(--blur-med);
            -webkit-backdrop-filter: var(--blur-med);
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.7);
            animation: fadeInUp 0.3s ease;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }

        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
            background: rgba(var(--glass-fill), 0.62);
            border-color: rgba(255, 255, 255, 0.85);
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
            background: rgba(var(--glass-fill), 0.34);
            border-color: rgba(255, 255, 255, 0.55);
        }

        /* ---------- SOURCE CHUNKS ---------- */
        .source-chunk {
            background: rgba(var(--glass-fill), 0.55);
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-left: 3px solid var(--accent-solid);
            padding: 0.75rem 0.95rem;
            border-radius: var(--radius-sm);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.79rem;
            color: var(--ink);
            margin-bottom: 0.55rem;
            white-space: pre-wrap;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
        }
        .source-meta {
            font-size: 0.71rem;
            color: var(--ink-muted);
            font-weight: 700;
            margin-bottom: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* ---------- BUTTONS (boxy glass, glow on hover) ---------- */
        .stButton > button {
            border-radius: var(--radius-md);
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            background: rgba(var(--glass-fill), 0.55);
            color: var(--ink);
            padding: 0.62rem 1.1rem;
            font-weight: 600;
            font-size: 0.92rem;
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.7);
            transition: transform 0.18s ease, box-shadow 0.25s ease, border-color 0.25s ease, background 0.25s ease;
        }
        .stButton > button:hover {
            border-color: rgba(var(--accent), 0.45);
            background: rgba(var(--accent), 0.08);
            box-shadow:
                0 0 0 1px rgba(var(--accent), 0.18),
                0 10px 28px rgba(var(--accent), 0.22),
                inset 0 1px 0 rgba(255,255,255,0.8);
            transform: translateY(-2px);
            color: var(--accent-solid);
        }
        .stButton > button:active {
            transform: translateY(0px);
        }

        /* Primary CTA (Process Documents) gets a filled accent treatment */
        .stButton > button[kind="primary"],
        section[data-testid="stSidebar"] .stButton > button:first-of-type {
            font-weight: 700;
        }

        /* ---------- FILE UPLOADER ---------- */
        section[data-testid="stFileUploaderDropzone"] {
            background: rgba(var(--glass-fill), 0.32);
            border: 1.5px dashed rgba(var(--accent), 0.35);
            border-radius: var(--radius-lg);
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            transition: border-color 0.2s ease, background 0.2s ease;
        }
        section[data-testid="stFileUploaderDropzone"]:hover {
            border-color: rgba(var(--accent), 0.6);
            background: rgba(var(--accent), 0.05);
        }

        /* ---------- STATUS PILLS (legacy hooks kept for compatibility) ---------- */
        .status-pill-ok { color: #0E7A3F; font-weight: 700; font-size: 0.82rem; }
        .status-pill-bad { color: #B91C1C; font-weight: 700; font-size: 0.82rem; }
        .status-pill-warn { color: #B45309; font-weight: 700; font-size: 0.82rem; }

        /* ---------- METRIC CARDS ---------- */
        div[data-testid="stMetric"] {
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-radius: var(--radius-md);
            padding: 0.75rem 0.9rem 0.4rem 0.9rem;
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
        }

        /* ---------- CHAT INPUT ---------- */
        .stChatInputContainer, div[data-testid="stChatInput"] {
            border-radius: var(--radius-lg) !important;
            background: rgba(var(--glass-fill), 0.55) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            box-shadow: var(--shadow-lift), inset 0 1px 0 rgba(255,255,255,0.75) !important;
        }
        div[data-testid="stChatInput"] textarea:focus {
            box-shadow: none !important;
        }

        /* ---------- EXPANDERS ---------- */
        div[data-testid="stExpander"] {
            background: rgba(var(--glass-fill), 0.30);
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-radius: var(--radius-md);
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            overflow: hidden;
        }
        div[data-testid="stExpander"] summary {
            font-weight: 600;
            color: var(--ink);
        }

        /* ---------- SLIDERS ---------- */
        div[data-testid="stSlider"] [role="slider"] {
            background-color: var(--accent-solid) !important;
            box-shadow: 0 0 0 4px rgba(var(--accent), 0.18) !important;
        }
        div[data-testid="stSlider"] > div > div > div > div {
            background: var(--accent-solid) !important;
        }

        /* ---------- ALERTS (info/warning/success/error) ---------- */
        div[data-testid="stAlert"] {
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-radius: var(--radius-md);
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: var(--shadow-ambient);
        }

        /* ---------- PROGRESS BAR ---------- */
        div[data-testid="stProgress"] > div > div {
            background-color: var(--accent-solid) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero_header() -> None:
    """Renders the liquid-glass hero header block."""
    st.markdown(
        """
        <div class="hero-header">
            <div class="hero-eyebrow">Document Intelligence</div>
            <div class="hero-title">RAG Chatbot</div>
            <div class="hero-subtitle">
                Strictly grounded answers from your own documents — powered by Groq, LangChain &amp; FAISS
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


def render_connection_badge(is_connected: bool) -> None:
    """
    Renders a neutral connection-status pill for the sidebar.
    Never displays or hints at the underlying key value.
    """
    state_class = "is-on" if is_connected else "is-off"
    label = "Connected" if is_connected else "Not connected"
    st.markdown(
        f"""
        <div class="conn-badge {state_class}">
            <span class="conn-dot"></span>
            {label}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_source_chunk(source_name: str, page: str, text: str) -> str:
    """Returns HTML for a single glass-style source citation chunk."""
    return f"""
    <div class="source-chunk">
        <div class="source-meta">{source_name} · page {page}</div>
        {text}
    </div>
    """

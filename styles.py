"""
styles.py
Apple "Liquid Glass"-inspired design system for the Streamlit RAG Chatbot.
"""

import streamlit as st


def inject_custom_css() -> None:
    """Injects the liquid-glass design system into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* ============================================================ */
        /* DESIGN TOKENS                                                 */
        /* ============================================================ */
        :root {
            color-scheme: light !important;

            --accent: 79, 70, 229;             /* indigo-600 */
            --accent-solid: #4F46E5;

            --ink: #0F172A;                    /* ultra-crisp slate dark */
            --ink-muted: #475569;
            --ink-faint: #94A3B8;

            --glass-fill: 255, 255, 255;
            --border-glass: rgba(255, 255, 255, 0.85);

            --radius-xl: 28px;
            --radius-lg: 20px;
            --radius-md: 14px;
            --radius-sm: 10px;

            --blur-strong: blur(32px) saturate(200%);
            --blur-med: blur(20px) saturate(180%);
            --blur-soft: blur(14px) saturate(160%);

            --shadow-ambient: 0 8px 30px rgba(15, 23, 42, 0.05);
            --shadow-lift: 0 20px 40px rgba(15, 23, 42, 0.09);
        }

        html { color-scheme: light !important; }

        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: var(--ink);
        }

        /* Continuous fluid background mesh */
        .stApp {
            background:
                radial-gradient(circle at 12% 10%, rgba(var(--accent), 0.08), transparent 45%),
                radial-gradient(circle at 88% 85%, rgba(var(--accent), 0.06), transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(255, 255, 255, 0.6), transparent 70%),
                linear-gradient(165deg, #F8FAFC 0%, #EEF2F6 50%, #E2E8F0 100%);
            background-attachment: fixed;
            color: var(--ink);
        }

        /* ============================================================ */
        /* TOP TITLE BAR / HEADER (Forces White Glass & Black Text)      */
        /* ============================================================ */
        header[data-testid="stHeader"],
        div[data-testid="stHeader"],
        .stAppHeader {
            background: rgba(255, 255, 255, 0.72) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border-bottom: 1px solid var(--border-glass) !important;
            box-shadow: 0 4px 20px rgba(15, 23, 42, 0.03) !important;
            visibility: visible !important;
            height: 3.5rem !important;
        }

        /* Target all text, icons, buttons inside the top header */
        header[data-testid="stHeader"] *,
        div[data-testid="stHeader"] *,
        .stAppHeader *,
        div[data-testid="stToolbar"] *,
        button[data-testid="stHeaderIconButton"] {
            color: var(--ink) !important;
            fill: var(--ink) !important;
        }

        /* Hide footer, but keep header visible and styled */
        footer { visibility: hidden; height: 0; }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(15, 23, 42, 0.15); border-radius: 10px; }
        ::selection { background: rgba(var(--accent), 0.2); color: var(--ink); }

        /* ============================================================ */
        /* GLOBAL TEXT ENFORCEMENT                                       */
        /* ============================================================ */
        p, span, label, .stMarkdown,
        section[data-testid="stSidebar"] *,
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stWidgetLabel"] label {
            color: var(--ink) !important;
        }
        div[data-testid="stCaptionContainer"], .stCaption, small {
            color: var(--ink-muted) !important;
        }

        /* ============================================================ */
        /* HERO HEADER BLOCK                                             */
        /* ============================================================ */
        .hero-header {
            position: relative;
            padding: 2.2rem 2.6rem;
            border-radius: var(--radius-xl);
            margin-bottom: 1.8rem;
            margin-top: 1rem;
            background: rgba(var(--glass-fill), 0.55);
            border: 1px solid var(--border-glass);
            backdrop-filter: var(--blur-strong);
            -webkit-backdrop-filter: var(--blur-strong);
            box-shadow: var(--shadow-lift), inset 0 1.5px 0 rgba(255, 255, 255, 0.95);
            overflow: hidden;
        }
        .hero-header::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 50%;
            background: linear-gradient(180deg, rgba(255,255,255,0.7), transparent);
            pointer-events: none;
        }
        .hero-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.73rem;
            font-weight: 800;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: var(--accent-solid) !important;
            position: relative;
            z-index: 1;
        }
        .hero-title {
            font-size: 2.6rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            color: var(--ink) !important;
            margin: 0.3rem 0 0.4rem 0;
            position: relative;
            z-index: 1;
        }
        .hero-subtitle {
            color: var(--ink-muted) !important;
            font-size: 1.02rem;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }

        /* ============================================================ */
        /* SIDEBAR SHELL                                                 */
        /* ============================================================ */
        section[data-testid="stSidebar"] {
            background: rgba(var(--glass-fill), 0.45) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border-right: 1px solid var(--border-glass) !important;
            box-shadow: 4px 0 24px rgba(15, 23, 42, 0.02) !important;
        }
        section[data-testid="stSidebar"] > div { padding-top: 1rem; }

        .sidebar-section-title {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: var(--ink-muted) !important;
            margin: 1.6rem 0 0.8rem 0;
            padding-bottom: 0.4rem;
            border-bottom: 1px solid rgba(15, 23, 42, 0.08);
        }
        .sidebar-section-title:first-of-type { margin-top: 0.2rem; }
        .sidebar-section-title::before {
            content: "";
            width: 6px; height: 6px;
            border-radius: 50%;
            background: var(--accent-solid);
        }

        /* ============================================================ */
        /* BADGES & STATUS PILLS                                         */
        /* ============================================================ */
        .guardrail-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            padding: 0.45rem 1rem;
            border-radius: 999px;
            background: rgba(22, 163, 74, 0.08);
            border: 1px solid rgba(22, 163, 74, 0.25);
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            color: #15803D !important;
            font-size: 0.78rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.8);
        }
        .guardrail-dot {
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #16A34A;
            box-shadow: 0 0 8px rgba(22, 163, 74, 0.8);
            animation: pulse 2s ease-in-out infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(0.75); }
        }

        .conn-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 0.95rem;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
        }
        .conn-badge.is-on {
            background: rgba(22, 163, 74, 0.08);
            border: 1px solid rgba(22, 163, 74, 0.25);
            color: #15803D !important;
        }
        .conn-badge.is-off {
            background: rgba(220, 38, 38, 0.08);
            border: 1px solid rgba(220, 38, 38, 0.25);
            color: #B91C1C !important;
        }
        .conn-dot { width: 6px; height: 6px; border-radius: 50%; }
        .conn-badge.is-on .conn-dot { background: #16A34A; box-shadow: 0 0 6px rgba(22,163,74,0.7); }
        .conn-badge.is-off .conn-dot { background: #DC2626; box-shadow: 0 0 6px rgba(220,38,38,0.7); }

        /* ============================================================ */
        /* GLASS CARDS, METRICS & EXPANDERS                              */
        /* ============================================================ */
        .glass-card,
        div[data-testid="stAlert"],
        div[data-testid="stExpander"],
        div[data-testid="stMetric"] {
            background: rgba(var(--glass-fill), 0.5) !important;
            border: 1px solid var(--border-glass) !important;
            border-radius: var(--radius-lg) !important;
            backdrop-filter: var(--blur-med) !important;
            -webkit-backdrop-filter: var(--blur-med) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.85) !important;
        }
        div[data-testid="stExpander"] summary { font-weight: 600; color: var(--ink) !important; }
        div[data-testid="stMetric"] { padding: 0.9rem 1.1rem !important; }
        div[data-testid="stMetricValue"] { color: var(--ink) !important; font-weight: 800 !important; }

        /* ============================================================ */
        /* FORM INPUTS & SELECTBOXES                                    */
        /* ============================================================ */
        .stTextInput > div > div,
        .stSelectbox > div > div,
        div[data-baseweb="input"],
        div[data-baseweb="select"] > div {
            background: rgba(var(--glass-fill), 0.75) !important;
            border: 1px solid var(--border-glass) !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.8) !important;
        }
        .stTextInput input { color: var(--ink) !important; font-weight: 500; }
        .stSelectbox * { color: var(--ink) !important; font-weight: 500; }

        /* Dropdown popover list */
        ul[data-testid="stSelectboxVirtualDropdown"],
        div[data-baseweb="popover"] ul[role="listbox"],
        div[data-baseweb="menu"] {
            background: rgba(255, 255, 255, 0.92) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border: 1px solid var(--border-glass) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-lift) !important;
        }
        ul[data-testid="stSelectboxVirtualDropdown"] li:hover,
        div[data-baseweb="popover"] li[role="option"]:hover {
            background: rgba(var(--accent), 0.1) !important;
            color: var(--accent-solid) !important;
        }

        /* ============================================================ */
        /* SLIDERS (Indigo Accent)                                       */
        /* ============================================================ */
        .stSlider [role="slider"] {
            background: #FFFFFF !important;
            border: 3px solid var(--accent-solid) !important;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.15) !important;
        }
        .stSlider [data-baseweb="slider"] > div:first-child > div {
            background-color: var(--accent-solid) !important;
        }
        .stSlider [data-testid="stThumbValue"] {
            background: var(--ink) !important;
            color: #FFFFFF !important;
            border-radius: var(--radius-sm) !important;
        }

        /* ============================================================ */
        /* BUTTONS                                                       */
        /* ============================================================ */
        .stButton > button,
        button[data-testid^="baseButton"],
        section[data-testid="stFileUploaderDropzone"] button {
            border-radius: var(--radius-md) !important;
            border: 1px solid var(--border-glass) !important;
            background: rgba(var(--glass-fill), 0.7) !important;
            color: var(--ink) !important;
            padding: 0.65rem 1.25rem !important;
            font-weight: 600 !important;
            backdrop-filter: var(--blur-soft) !important;
            -webkit-backdrop-filter: var(--blur-soft) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.9) !important;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
        }
        .stButton > button:hover,
        section[data-testid="stFileUploaderDropzone"] button:hover {
            border-color: rgba(var(--accent), 0.4) !important;
            background: rgba(var(--accent), 0.08) !important;
            color: var(--accent-solid) !important;
            transform: translateY(-1.5px);
            box-shadow: 0 10px 25px rgba(var(--accent), 0.15), inset 0 1px 0 rgba(255,255,255,0.95) !important;
        }

        /* ============================================================ */
        /* FILE UPLOADER                                                 */
        /* ============================================================ */
        section[data-testid="stFileUploaderDropzone"] {
            background: rgba(var(--glass-fill), 0.38) !important;
            border: 1.5px dashed rgba(var(--accent), 0.35) !important;
            border-radius: var(--radius-lg) !important;
            backdrop-filter: var(--blur-soft) !important;
            -webkit-backdrop-filter: var(--blur-soft) !important;
        }
        section[data-testid="stFileUploaderDropzone"]:hover {
            border-color: rgba(var(--accent), 0.65) !important;
            background: rgba(var(--accent), 0.04) !important;
        }

        /* ============================================================ */
        /* CHAT MESSAGES                                                 */
        /* ============================================================ */
        div[data-testid="stChatMessage"] {
            border-radius: var(--radius-lg) !important;
            padding: 1rem 1.25rem !important;
            margin-bottom: 0.9rem !important;
            background: rgba(var(--glass-fill), 0.5) !important;
            border: 1px solid var(--border-glass) !important;
            backdrop-filter: var(--blur-med) !important;
            -webkit-backdrop-filter: var(--blur-med) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.85) !important;
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
            background: rgba(var(--glass-fill), 0.75) !important;
            border-color: rgba(255, 255, 255, 0.95) !important;
        }

        /* ============================================================ */
        /* BOTTOM CHAT INPUT BAR                                         */
        /* ============================================================ */
        div[data-testid="stBottom"],
        div[data-testid="stBottomBlockContainer"] {
            background: linear-gradient(180deg, rgba(238,242,246,0) 0%, rgba(238,242,246,0.85) 40%, rgba(238,242,246,0.98) 100%) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
        }
        .stChatInput, div[data-testid="stChatInput"] {
            border-radius: var(--radius-lg) !important;
            background: rgba(var(--glass-fill), 0.85) !important;
            border: 1.5px solid var(--border-glass) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            box-shadow: var(--shadow-lift), inset 0 1px 0 rgba(255,255,255,0.9) !important;
        }
        .stChatInput textarea, div[data-testid="stChatInput"] textarea {
            color: var(--ink) !important;
            -webkit-text-fill-color: var(--ink) !important;
        }
        .stChatInput button, div[data-testid="stChatInput"] button {
            background: var(--accent-solid) !important;
            border: none !important;
            border-radius: var(--radius-sm) !important;
        }
        .stChatInput button svg, div[data-testid="stChatInput"] button svg { fill: #FFFFFF !important; }

        /* ============================================================ */
        /* CITATION CHUNKS                                               */
        /* ============================================================ */
        .source-chunk {
            background: rgba(var(--glass-fill), 0.65) !important;
            border: 1px solid var(--border-glass);
            border-left: 3.5px solid var(--accent-solid);
            padding: 0.85rem 1.05rem;
            border-radius: var(--radius-sm);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: var(--ink) !important;
            margin-bottom: 0.6rem;
            white-space: pre-wrap;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
        }
        .source-meta {
            font-size: 0.72rem;
            color: var(--ink-muted) !important;
            font-weight: 700;
            margin-bottom: 0.35rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
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
    """Renders connection-status pill."""
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

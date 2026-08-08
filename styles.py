"""
styles.py
Apple "Liquid Glass"-inspired design system for the RAG Chatbot.

This targets the ACTUAL underlying DOM Streamlit/BaseWeb render (not just the
high-level wrapper divs), including elements rendered in portals outside the
sidebar (select dropdown menus). Native form controls are forced into light
mode via `color-scheme: light` so the browser stops substituting its own
dark-mode chrome for inputs, selects, and sliders.
"""

import streamlit as st


def inject_custom_css() -> None:
    """Injects the full liquid-glass design system into the Streamlit app."""
    st.markdown(
        """
        <style>
        /* ============================================================ */
        /* DESIGN TOKENS                                                 */
        /* ============================================================ */
        :root {
            color-scheme: light !important;

            --accent: 79, 70, 229;             /* indigo-600 — the one accent */
            --accent-solid: #4F46E5;
            --accent-soft: #EEF0FE;

            --ink: #10142B;                    /* primary text — near-black */
            --ink-muted: #4B5268;               /* secondary text */
            --ink-faint: #8A90A6;               /* tertiary / captions */

            --glass-fill: 255, 255, 255;
            --glass-a1: 0.62;                   /* strong panel opacity */
            --glass-a2: 0.42;                   /* medium panel opacity */
            --glass-a3: 0.24;                   /* subtle panel opacity */

            --border-a1: 0.65;
            --border-a2: 0.40;

            --radius-xl: 28px;
            --radius-lg: 20px;
            --radius-md: 14px;
            --radius-sm: 11px;

            --blur-strong: blur(30px) saturate(190%);
            --blur-med: blur(22px) saturate(170%);
            --blur-soft: blur(16px) saturate(150%);

            --shadow-ambient: 0 10px 32px rgba(16, 20, 43, 0.07);
            --shadow-lift: 0 20px 52px rgba(16, 20, 43, 0.12);
        }

        html { color-scheme: light !important; }

        /* ============================================================ */
        /* GLOBAL                                                        */
        /* ============================================================ */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

        html, body, [class*="css"], .stApp {
            font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
            color: var(--ink);
        }

        .stApp {
            background:
                radial-gradient(circle at 10% 6%, rgba(var(--accent), 0.10), transparent 40%),
                radial-gradient(circle at 90% 84%, rgba(var(--accent), 0.07), transparent 46%),
                linear-gradient(160deg, #F6F8FC 0%, #ECF0F8 55%, #E6EAF3 100%);
            background-attachment: fixed;
            color: var(--ink);
        }

        #MainMenu, footer, div[data-testid="stHeader"] { visibility: hidden; height: 0; }

        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(16, 20, 43, 0.18);
            border-radius: 10px;
        }

        /* Kill Streamlit's default red focus/selection color everywhere */
        ::selection { background: rgba(var(--accent), 0.25); color: var(--ink); }

        /* ============================================================ */
        /* TEXT — force readable ink color on every label / caption,     */
        /* overriding any dark-mode default Streamlit may fall back to.  */
        /* ============================================================ */
        p, span, label, .stMarkdown, .stCaption,
        section[data-testid="stSidebar"] * ,
        div[data-testid="stWidgetLabel"] p,
        div[data-testid="stWidgetLabel"] label {
            color: var(--ink) !important;
        }
        div[data-testid="stCaptionContainer"], .stCaption, small {
            color: var(--ink-muted) !important;
        }

        /* ============================================================ */
        /* UNIVERSAL FORM-CONTROL FALLBACK                                */
        /* Guarantees legible text/backgrounds even if a more targeted   */
        /* selector below doesn't match this Streamlit build's DOM.      */
        /* ============================================================ */
        input, textarea, select {
            background: transparent !important;
            color: var(--ink) !important;
            border: none !important;
        }
        input::placeholder, textarea::placeholder { color: var(--ink-faint) !important; }

        /* Outer control shells, keyed off Streamlit's own stable testids
           (these do not depend on BaseWeb's internal attribute names,
           which can change between Streamlit versions). */
        div[data-testid="stTextInput"] > div:last-of-type,
        div[data-testid="stNumberInput"] > div:last-of-type,
        div[data-testid="stSelectbox"] > div:last-of-type {
            background: rgba(var(--glass-fill), 0.72) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6) !important;
        }
        div[data-testid="stTextInput"] > div:last-of-type *,
        div[data-testid="stNumberInput"] > div:last-of-type *,
        div[data-testid="stSelectbox"] > div:last-of-type * {
            background: transparent !important;
            color: var(--ink) !important;
        }
        div[data-testid="stTextInput"] > div:last-of-type svg,
        div[data-testid="stSelectbox"] > div:last-of-type svg {
            fill: var(--ink-muted) !important;
        }
        div[data-testid="stTextInput"]:focus-within > div:last-of-type,
        div[data-testid="stSelectbox"]:focus-within > div:last-of-type {
            border-color: rgba(var(--accent), 0.55) !important;
            box-shadow: 0 0 0 3px rgba(var(--accent), 0.16) !important;
        }

        /* Slider control shell + thumb, via stable testid */
        div[data-testid="stSlider"] [role="slider"] {
            background: #FFFFFF !important;
            border: 3px solid var(--accent-solid) !important;
            box-shadow: 0 2px 8px rgba(16, 20, 43, 0.18) !important;
        }
        div[data-testid="stSlider"] [data-testid="stThumbValue"] {
            background: var(--ink) !important;
            color: #FFFFFF !important;
            border-radius: var(--radius-sm) !important;
            font-weight: 600 !important;
        }
        div[data-testid="stSlider"] [data-testid="stTickBarMin"],
        div[data-testid="stSlider"] [data-testid="stTickBarMax"] {
            color: var(--ink-faint) !important;
        }
        /* Any inline-styled fill/track div inside the slider still carrying
           Streamlit's literal default red — force it to the accent color. */
        div[data-testid="stSlider"] div[style*="background-color"] {
            background-color: var(--accent-solid) !important;
        }

        /* Selectbox dropdown list — multiple possible portal testids across
           Streamlit versions, all covered defensively. */
        ul[data-testid="stSelectboxVirtualDropdown"],
        div[data-baseweb="popover"] ul[role="listbox"],
        div[data-baseweb="menu"] {
            background: rgba(255, 255, 255, 0.92) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border: 1px solid rgba(255, 255, 255, 0.8) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-lift) !important;
        }
        ul[data-testid="stSelectboxVirtualDropdown"] li,
        div[data-baseweb="popover"] li[role="option"] {
            color: var(--ink) !important;
            background: transparent !important;
        }
        ul[data-testid="stSelectboxVirtualDropdown"] li:hover,
        div[data-baseweb="popover"] li[role="option"]:hover,
        div[data-baseweb="popover"] li[aria-selected="true"] {
            background: rgba(var(--accent), 0.10) !important;
            color: var(--accent-solid) !important;
        }

        /* ============================================================ */
        /* HERO HEADER                                                   */
        /* ============================================================ */
        .hero-header {
            position: relative;
            padding: 2.1rem 2.5rem;
            border-radius: var(--radius-xl);
            margin-bottom: 1.7rem;
            background: rgba(var(--glass-fill), var(--glass-a2));
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            backdrop-filter: var(--blur-strong);
            -webkit-backdrop-filter: var(--blur-strong);
            box-shadow: var(--shadow-lift), inset 0 1px 0 rgba(255,255,255,0.9);
            overflow: hidden;
        }
        .hero-header::before {
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 55%;
            background: linear-gradient(180deg, rgba(255,255,255,0.65), transparent);
            pointer-events: none;
        }
        .hero-header::after {
            content: "";
            position: absolute;
            top: -60%; right: -15%;
            width: 55%; height: 220%;
            background: radial-gradient(circle, rgba(var(--accent), 0.10), transparent 70%);
            pointer-events: none;
        }
        .hero-eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--accent-solid) !important;
            position: relative;
            z-index: 1;
        }
        .hero-title {
            font-size: 2.5rem;
            font-weight: 800;
            letter-spacing: -0.035em;
            color: var(--ink) !important;
            margin: 0.4rem 0 0.35rem 0;
            position: relative;
            z-index: 1;
        }
        .hero-subtitle {
            color: var(--ink-muted) !important;
            font-size: 1rem;
            font-weight: 500;
            position: relative;
            z-index: 1;
        }

        /* ============================================================ */
        /* SECTION TITLES — accent bar instead of colorful default emoji */
        /* ============================================================ */
        .sidebar-section-title {
            display: flex;
            align-items: center;
            gap: 0.55rem;
            font-size: 0.71rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--ink-muted) !important;
            margin: 1.5rem 0 0.7rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(16, 20, 43, 0.08);
        }
        .sidebar-section-title:first-of-type { margin-top: 0.1rem; }
        .sidebar-section-title::before {
            content: "";
            width: 6px;
            height: 6px;
            border-radius: 2px;
            background: var(--accent-solid);
            flex-shrink: 0;
        }

        /* ============================================================ */
        /* BADGES                                                        */
        /* ============================================================ */
        .guardrail-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.45rem 1rem;
            border-radius: 999px;
            background: rgba(22, 163, 74, 0.09);
            border: 1px solid rgba(22, 163, 74, 0.28);
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.5);
            color: #0E7A3F !important;
            font-size: 0.78rem;
            font-weight: 700;
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

        .conn-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 0.9rem;
            border-radius: 999px;
            font-size: 0.76rem;
            font-weight: 700;
            border: 1px solid transparent;
            backdrop-filter: var(--blur-soft);
            -webkit-backdrop-filter: var(--blur-soft);
        }
        .conn-badge.is-on {
            background: rgba(22, 163, 74, 0.09);
            border-color: rgba(22, 163, 74, 0.28);
            color: #0E7A3F !important;
        }
        .conn-badge.is-off {
            background: rgba(220, 38, 38, 0.07);
            border-color: rgba(220, 38, 38, 0.24);
            color: #B91C1C !important;
        }
        .conn-dot { width: 6px; height: 6px; border-radius: 50%; }
        .conn-badge.is-on .conn-dot { background: #16A34A; box-shadow: 0 0 6px rgba(22,163,74,0.7); }
        .conn-badge.is-off .conn-dot { background: #DC2626; box-shadow: 0 0 6px rgba(220,38,38,0.5); }

        /* ============================================================ */
        /* GLASS CARDS / ALERTS / EXPANDERS / METRICS                    */
        /* ============================================================ */
        .glass-card,
        div[data-testid="stAlert"],
        div[data-testid="stExpander"],
        div[data-testid="stMetric"] {
            background: rgba(var(--glass-fill), var(--glass-a2)) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            border-radius: var(--radius-lg) !important;
            backdrop-filter: var(--blur-med) !important;
            -webkit-backdrop-filter: var(--blur-med) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.7) !important;
        }
        .glass-card { padding: 1.1rem 1.3rem; margin-bottom: 0.9rem; }
        div[data-testid="stExpander"] { overflow: hidden; }
        div[data-testid="stExpander"] summary { font-weight: 600; color: var(--ink) !important; }
        div[data-testid="stMetric"] { padding: 0.8rem 1rem 0.5rem 1rem !important; }
        div[data-testid="stMetricValue"] { color: var(--ink) !important; }
        div[data-testid="stMetricLabel"] { color: var(--ink-muted) !important; }

        /* ============================================================ */
        /* SIDEBAR SHELL                                                 */
        /* ============================================================ */
        section[data-testid="stSidebar"] {
            background: rgba(var(--glass-fill), 0.34) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.55);
        }
        section[data-testid="stSidebar"] > div { padding-top: 1.3rem; }

        /* ============================================================ */
        /* TEXT INPUT — style the real BaseWeb wrapper, not just <input> */
        /* ============================================================ */
        div[data-baseweb="input"],
        div[data-baseweb="base-input"] {
            background: rgba(var(--glass-fill), 0.7) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6) !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }
        div[data-baseweb="input"]:focus-within {
            border-color: rgba(var(--accent), 0.55) !important;
            box-shadow: 0 0 0 3px rgba(var(--accent), 0.16) !important;
        }
        div[data-baseweb="input"] input,
        div[data-baseweb="base-input"] input {
            background: transparent !important;
            color: var(--ink) !important;
            caret-color: var(--accent-solid);
        }
        div[data-baseweb="input"] input::placeholder {
            color: var(--ink-faint) !important;
        }
        /* Password-reveal icon button */
        div[data-testid="stTextInput"] button {
            background: transparent !important;
            border: none !important;
            color: var(--ink-muted) !important;
        }
        div[data-testid="stTextInput"] button:hover {
            color: var(--accent-solid) !important;
        }
        div[data-testid="stTextInput"] button svg { fill: currentColor !important; }

        /* ============================================================ */
        /* SELECTBOX — outer container + the portal-rendered dropdown    */
        /* ============================================================ */
        div[data-baseweb="select"] > div {
            background: rgba(var(--glass-fill), 0.7) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            border-radius: var(--radius-sm) !important;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6) !important;
            color: var(--ink) !important;
        }
        div[data-baseweb="select"] * {
            color: var(--ink) !important;
        }
        div[data-baseweb="select"] svg { fill: var(--ink-muted) !important; }

        /* The option list renders in a portal appended to <body>, so this
           selector must NOT be scoped to the sidebar. */
        div[data-baseweb="popover"] ul[role="listbox"],
        div[data-baseweb="menu"] {
            background: rgba(255, 255, 255, 0.88) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border: 1px solid rgba(255, 255, 255, 0.8) !important;
            border-radius: var(--radius-md) !important;
            box-shadow: var(--shadow-lift) !important;
            overflow: hidden;
        }
        div[data-baseweb="popover"] li[role="option"] {
            color: var(--ink) !important;
            background: transparent !important;
        }
        div[data-baseweb="popover"] li[role="option"]:hover,
        div[data-baseweb="popover"] li[aria-selected="true"] {
            background: rgba(var(--accent), 0.10) !important;
            color: var(--accent-solid) !important;
        }

        /* ============================================================ */
        /* SLIDER — real BaseWeb track / fill / thumb                    */
        /* ============================================================ */
        div[data-testid="stSlider"] { padding-top: 0.2rem; }
        div[data-baseweb="slider"] [data-testid="stTickBarMin"],
        div[data-baseweb="slider"] [data-testid="stTickBarMax"] {
            color: var(--ink-faint) !important;
        }
        /* Background track */
        div[data-baseweb="slider"] > div:first-child {
            background: rgba(16, 20, 43, 0.10) !important;
        }
        /* Filled/selected range */
        div[data-baseweb="slider"] > div:first-child > div {
            background: var(--accent-solid) !important;
        }
        /* Thumb handle */
        div[data-baseweb="slider"] div[role="slider"] {
            background: #FFFFFF !important;
            border: 3px solid var(--accent-solid) !important;
            box-shadow: 0 2px 8px rgba(16, 20, 43, 0.18) !important;
        }
        div[data-baseweb="slider"] div[role="slider"]:focus-visible {
            box-shadow: 0 0 0 4px rgba(var(--accent), 0.20) !important;
        }
        /* Value bubble tooltip above the thumb */
        div[data-baseweb="slider"] div[data-testid="stThumbValue"] {
            background: var(--ink) !important;
            color: #FFFFFF !important;
            border-radius: var(--radius-sm) !important;
            font-weight: 600;
        }

        /* ============================================================ */
        /* BUTTONS — normalize every kind Streamlit renders               */
        /* ============================================================ */
        .stButton > button,
        button[data-testid^="baseButton"],
        button[kind="secondary"],
        button[kind="secondaryFormSubmit"],
        button[kind="primary"],
        section[data-testid="stFileUploaderDropzone"] button {
            border-radius: var(--radius-md) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            background: rgba(var(--glass-fill), 0.62) !important;
            color: var(--ink) !important;
            padding: 0.65rem 1.15rem !important;
            font-weight: 600 !important;
            font-size: 0.92rem !important;
            min-height: 2.7rem;
            backdrop-filter: var(--blur-soft) !important;
            -webkit-backdrop-filter: var(--blur-soft) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.75) !important;
            transition: transform 0.18s ease, box-shadow 0.25s ease, border-color 0.25s ease, background 0.25s ease, color 0.25s ease;
        }
        .stButton > button:hover,
        button[data-testid^="baseButton"]:hover,
        section[data-testid="stFileUploaderDropzone"] button:hover {
            border-color: rgba(var(--accent), 0.5) !important;
            background: rgba(var(--accent), 0.10) !important;
            box-shadow:
                0 0 0 1px rgba(var(--accent), 0.20),
                0 12px 30px rgba(var(--accent), 0.24),
                inset 0 1px 0 rgba(255,255,255,0.85) !important;
            transform: translateY(-2px);
            color: var(--accent-solid) !important;
        }
        .stButton > button:active,
        button[data-testid^="baseButton"]:active {
            transform: translateY(0px);
        }
        .stButton > button p { color: inherit !important; }

        /* ============================================================ */
        /* FILE UPLOADER                                                 */
        /* ============================================================ */
        section[data-testid="stFileUploaderDropzone"] {
            background: rgba(var(--glass-fill), 0.34) !important;
            border: 1.5px dashed rgba(var(--accent), 0.35) !important;
            border-radius: var(--radius-lg) !important;
            backdrop-filter: var(--blur-soft) !important;
            -webkit-backdrop-filter: var(--blur-soft) !important;
            transition: border-color 0.2s ease, background 0.2s ease;
        }
        section[data-testid="stFileUploaderDropzone"]:hover {
            border-color: rgba(var(--accent), 0.6) !important;
            background: rgba(var(--accent), 0.05) !important;
        }
        section[data-testid="stFileUploaderDropzone"] small,
        section[data-testid="stFileUploaderDropzone"] span {
            color: var(--ink-muted) !important;
        }
        div[data-testid="stFileUploaderFile"] {
            background: rgba(var(--glass-fill), 0.5) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            border-radius: var(--radius-sm) !important;
        }

        /* ============================================================ */
        /* CHAT — messages + the fixed bottom input bar                  */
        /* ============================================================ */
        div[data-testid="stChatMessage"] {
            border-radius: var(--radius-lg) !important;
            padding: 0.95rem 1.15rem !important;
            margin-bottom: 0.85rem !important;
            background: rgba(var(--glass-fill), var(--glass-a2)) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            backdrop-filter: var(--blur-med) !important;
            -webkit-backdrop-filter: var(--blur-med) !important;
            box-shadow: var(--shadow-ambient), inset 0 1px 0 rgba(255,255,255,0.7) !important;
            animation: fadeInUp 0.3s ease;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(8px); }
            to { opacity: 1; transform: translateY(0); }
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
            background: rgba(var(--glass-fill), 0.68) !important;
            border-color: rgba(255, 255, 255, 0.85) !important;
        }
        div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {
            background: rgba(var(--glass-fill), 0.36) !important;
            border-color: rgba(255, 255, 255, 0.55) !important;
        }
        div[data-testid="stChatMessage"] p { color: var(--ink) !important; }

        /* The fixed bottom container that wraps the chat input — this is
           what was rendering as a solid black bar. */
        div[data-testid="stBottom"],
        div[data-testid="stBottomBlockContainer"],
        .stChatFloatingInputContainer {
            background: linear-gradient(180deg, rgba(236,240,248,0) 0%, rgba(236,240,248,0.92) 35%, rgba(236,240,248,0.98) 100%) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            border-top: 1px solid rgba(255,255,255,0.6) !important;
        }
        div[data-testid="stChatInput"] {
            border-radius: var(--radius-lg) !important;
            background: rgba(var(--glass-fill), 0.75) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1)) !important;
            backdrop-filter: var(--blur-strong) !important;
            -webkit-backdrop-filter: var(--blur-strong) !important;
            box-shadow: var(--shadow-lift), inset 0 1px 0 rgba(255,255,255,0.8) !important;
        }
        /* Defensive: strip any inner wrapper's own opaque background so the
           glass fill above always shows through, regardless of internal
           DOM depth in this Streamlit build. */
        div[data-testid="stChatInput"] > div,
        div[data-testid="stChatInput"] > div > div {
            background: transparent !important;
            border: none !important;
        }
        div[data-testid="stChatInput"] textarea {
            background: transparent !important;
            color: var(--ink) !important;
        }
        div[data-testid="stChatInput"] textarea::placeholder {
            color: var(--ink-faint) !important;
        }
        div[data-testid="stChatInput"] textarea:focus {
            box-shadow: none !important;
        }
        div[data-testid="stChatInputSubmitButton"] button {
            background: var(--accent-solid) !important;
            border: none !important;
            border-radius: var(--radius-sm) !important;
        }
        div[data-testid="stChatInputSubmitButton"] button svg { fill: #FFFFFF !important; }

        /* ============================================================ */
        /* SOURCE CHUNKS                                                 */
        /* ============================================================ */
        .source-chunk {
            background: rgba(var(--glass-fill), 0.6) !important;
            border: 1px solid rgba(255, 255, 255, var(--border-a1));
            border-left: 3px solid var(--accent-solid);
            padding: 0.8rem 1rem;
            border-radius: var(--radius-sm);
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.79rem;
            color: var(--ink) !important;
            margin-bottom: 0.55rem;
            white-space: pre-wrap;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.6);
        }
        .source-meta {
            font-size: 0.71rem;
            color: var(--ink-muted) !important;
            font-weight: 700;
            margin-bottom: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }

        /* ============================================================ */
        /* PROGRESS BAR                                                  */
        /* ============================================================ */
        div[data-testid="stProgress"] > div { background: rgba(16, 20, 43, 0.10) !important; border-radius: 999px !important; }
        div[data-testid="stProgress"] > div > div { background-color: var(--accent-solid) !important; }
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
        <div style="text-align:right; font-size:0.68rem; color:#8A90A6; margin:-0.9rem 0.3rem 0.9rem 0;">
            UI build: liquid-glass-v3
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

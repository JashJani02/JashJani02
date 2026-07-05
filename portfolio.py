import streamlit as st
from pathlib import Path

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Jash Jani · Portfolio",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Load resume PDF ────────────────────────────────────────────────────────────
_resume_path = Path(__file__).parent / "Jash_Jani_resume.pdf"
_resume_bytes = _resume_path.read_bytes() if _resume_path.exists() else None

# ══════════════════════════════════════════════════════════════════════════════
# THEME CATALOGUE
# ══════════════════════════════════════════════════════════════════════════════

FONT_PAIRS = {
    "Ocean (Default)": {
        "heading": "Syne",
        "mono":    "IBM Plex Mono",
        "import":  "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Syne:wght@700;800&display=swap",
    },
    "Sharp": {
        "heading": "Space Grotesk",
        "mono":    "Fira Code",
        "import":  "https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Space+Grotesk:wght@700;800&display=swap",
    },
    "Editorial": {
        "heading": "DM Serif Display",
        "mono":    "Source Code Pro",
        "import":  "https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Source+Code+Pro:wght@400;600&display=swap",
    },
    "Clean": {
        "heading": "Inter",
        "mono":    "JetBrains Mono",
        "import":  "https://fonts.googleapis.com/css2?family=Inter:wght@700;800&family=JetBrains+Mono:wght@400;600&display=swap",
    },
    "Futuristic": {
        "heading": "Orbitron",
        "mono":    "Share Tech Mono",
        "import":  "https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800&family=Share+Tech+Mono&display=swap",
    },
    "Rajdhani": {
        "heading": "Rajdhani",
        "mono":    "Fira Code",
        "import":  "https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=Fira+Code:wght@400;600&display=swap",
    },
}

COLOR_THEMES = {
    "Ocean (Default)": {"accent": "#4d9fff", "bg": "#0a0c0f", "card_bg": "#0d141e", "border": "#1a2030"},
    "Terminal":        {"accent": "#00ff88", "bg": "#0a0c0f", "card_bg": "#0d1a12", "border": "#1a2030"},
    "Amber":           {"accent": "#ffb347", "bg": "#0c0a06", "card_bg": "#1a1208", "border": "#2a1e0a"},
    "Rose":            {"accent": "#ff6b9d", "bg": "#0c0a0e", "card_bg": "#180d18", "border": "#2a1030"},
    "Violet":          {"accent": "#a855f7", "bg": "#08060f", "card_bg": "#120d1e", "border": "#1e1030"},
    "Cyan":            {"accent": "#00e5ff", "bg": "#060c0f", "card_bg": "#0a1820", "border": "#0f2530"},
    "Copper":          {"accent": "#b87333", "bg": "#0a0805", "card_bg": "#160f06", "border": "#2a1a08"},
    "Gold":            {"accent": "#ffd700", "bg": "#0a0900", "card_bg": "#181400", "border": "#2a2200"},
    "Crimson":         {"accent": "#ff3355", "bg": "#0f0608", "card_bg": "#1e0a0e", "border": "#300a12"},
    "Teal":            {"accent": "#14b8a6", "bg": "#060f0e", "card_bg": "#0a1a18", "border": "#0f2825"},
    "Indigo":          {"accent": "#6366f1", "bg": "#07060f", "card_bg": "#0e0d1e", "border": "#1a1830"},
    "Lime":            {"accent": "#a3e635", "bg": "#070a04", "card_bg": "#0f1a06", "border": "#1a2a08"},
    "Ice":             {"accent": "#e0f4ff", "bg": "#06080f", "card_bg": "#0d1220", "border": "#1a2035"},
    "Sakura":          {"accent": "#ffb7c5", "bg": "#0f080a", "card_bg": "#1e0e12", "border": "#2e1820"},
    "Catppuccin":      {"accent": "#cba6f7", "bg": "#11111b", "card_bg": "#1e1e2e", "border": "#313244"},
}

# ── Session state defaults ─────────────────────────────────────────────────────
if "color_sel" not in st.session_state:
    st.session_state.color_sel = "Ocean (Default)"
if "font_sel" not in st.session_state:
    st.session_state.font_sel = "Ocean (Default)"
if "show_settings" not in st.session_state:
    st.session_state.show_settings = False
# Persistent values — survive widget unmount when panel is hidden
if "color_val" not in st.session_state:
    st.session_state.color_val = "Ocean (Default)"
if "font_val" not in st.session_state:
    st.session_state.font_val = "Ocean (Default)"

font  = FONT_PAIRS[st.session_state.font_val]
theme = COLOR_THEMES[st.session_state.color_val]

accent     = theme["accent"]
bg         = theme["bg"]
card_bg    = theme["card_bg"]
border     = theme["border"]
heading_fn = font["heading"]
mono_fn    = font["mono"]

# ── Dynamic CSS ────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('{font["import"]}');

[data-testid="stAppViewContainer"], [data-testid="stMain"], .main {{
    background-color: {bg} !important;
}}
[data-testid="stHeader"], footer, [data-testid="stToolbar"] {{ display: none !important; }}
[data-testid="stSidebar"] {{ display: none !important; }}

h1, h2, h3, h4 {{ font-family: '{heading_fn}', sans-serif !important; color: #eaf0f8 !important; }}
h2 {{ font-size: 26px !important; }}
h3 {{ font-size: 22px !important; }}
h4 {{ font-size: 18px !important; }}
p, li, div, span, label {{ color: #c8d6e5; }}

[data-testid="stMetricLabel"] > div {{
    color: #5a7a9a !important;
    font-size: 11px !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-family: '{mono_fn}', monospace !important;
}}
[data-testid="stMetricValue"] > div {{
    color: {accent} !important;
    font-size: 22px !important;
    font-family: '{mono_fn}', monospace !important;
}}

code {{
    background: {card_bg} !important;
    color: #7aafd4 !important;
    border: 1px solid {border} !important;
    border-radius: 2px !important;
    font-family: '{mono_fn}', monospace !important;
    padding: 2px 8px !important;
}}

hr {{ border-color: {border} !important; margin: 8px 0 !important; }}

[data-testid="stExpander"] {{
    background: {card_bg} !important;
    border: 1px solid {border} !important;
    border-radius: 0 !important;
    transition: border-color 0.2s;
}}
[data-testid="stExpander"]:hover {{ border-color: {accent}40 !important; }}
[data-testid="stExpander"] summary {{
    color: #eaf0f8 !important;
    font-family: '{heading_fn}', sans-serif !important;
    font-weight: 700 !important;
    font-size: 20px !important;
}}

[data-testid="stLinkButton"] > a {{
    background: {card_bg} !important;
    border: 1px solid {accent}40 !important;
    color: {accent} !important;
    border-radius: 0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
}}
[data-testid="stLinkButton"] > a:hover {{
    background: {accent}15 !important;
    border-color: {accent}88 !important;
    color: {accent} !important;
}}

[data-testid="stDownloadButton"] > button {{
    background: {card_bg} !important;
    border: 1px solid {accent}55 !important;
    color: {accent} !important;
    border-radius: 0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
    padding: 8px 20px !important;
}}
[data-testid="stDownloadButton"] > button:hover {{
    background: {accent}20 !important;
    border-color: {accent} !important;
    color: #fff !important;
}}

[data-testid="stCaptionContainer"] p {{
    color: #a0b8d0 !important;
    font-family: '{mono_fn}', monospace !important;
    font-size: 12px !important;
}}
[data-testid="stExpander"] [data-testid="stCaptionContainer"] p {{
    color: #c8d6e5 !important;
}}
[data-testid="stExpander"] p,
[data-testid="stExpander"] div,
[data-testid="stExpander"] span {{
    color: #eaf0f8 !important;
}}

/* Settings panel */
.settings-panel {{
    position: fixed;
    bottom: 80px;
    right: 24px;
    background: {card_bg};
    border: 1px solid {accent}55;
    padding: 20px;
    z-index: 9999;
    min-width: 220px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
}}
.settings-fab {{
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: {card_bg};
    border: 1px solid {accent}55;
    color: {accent};
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 18px;
    z-index: 9999;
    box-shadow: 0 4px 16px rgba(0,0,0,0.4);
}}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def section_header(title: str):
    st.markdown(
        f"<p style='font-size:15px;letter-spacing:4px;text-transform:uppercase;"
        f"color:{accent};opacity:0.85;font-family:{mono_fn},monospace;font-weight:600;"
        f"margin:0 0 4px 0;'>// {title}</p>",
        unsafe_allow_html=True,
    )
    st.divider()


def skill_row(category: str, skills: list):
    st.markdown(
        f"<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        f"color:#3a5a8a;font-family:{mono_fn},monospace;margin:18px 0 6px;font-weight:600;'>"
        f"{category}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("&nbsp;&nbsp;".join(f"`{s}`" for s in skills))


def project_card(title: str, desc: str, tags: list, gh_url: str, live_url: str = None, pypi_url: str = None):
    with st.expander(title):
        st.caption(desc)
        st.markdown("&nbsp;&nbsp;".join(f"`{t}`" for t in tags))
        st.write("")
        btn_cols = st.columns([1.2, 1.2, 1.2, 3])
        with btn_cols[0]:
            st.link_button("→ GitHub", gh_url)
        if live_url:
            with btn_cols[1]:
                st.link_button("⎋ Live Demo", live_url)
        if pypi_url:
            with btn_cols[2]:
                st.link_button("⬡ PyPI", pypi_url)


# ══════════════════════════════════════════════════════════════════════════════
# FLOATING SETTINGS BUTTON + PANEL
# ══════════════════════════════════════════════════════════════════════════════

with st.container():
    if st.button("⚙", key="fab", help="Customise theme"):
        st.session_state.show_settings = not st.session_state.show_settings

if st.session_state.show_settings:
    with st.container():
        st.markdown(
            f"<p style='font-size:10px;letter-spacing:3px;text-transform:uppercase;"
            f"color:{accent};font-family:{mono_fn},monospace;margin-bottom:8px;'>// Customise</p>",
            unsafe_allow_html=True,
        )
        def save_color(): st.session_state.color_val = st.session_state.color_widget
        def save_font():  st.session_state.font_val  = st.session_state.font_widget

        st.selectbox(
            "Colour Theme",
            list(COLOR_THEMES.keys()),
            index=list(COLOR_THEMES.keys()).index(st.session_state.color_val),
            key="color_widget",
            on_change=save_color,
        )
        st.selectbox(
            "Font Pair",
            list(FONT_PAIRS.keys()),
            index=list(FONT_PAIRS.keys()).index(st.session_state.font_val),
            key="font_widget",
            on_change=save_font,
        )
        st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.write("")
st.markdown(
    f"<h1 style='font-size:clamp(48px,8vw,88px);font-weight:800;line-height:0.95;"
    f"letter-spacing:-3px;margin-bottom:16px;font-family:{heading_fn},sans-serif;'>"
    f"Jash <span style='color:{accent};'>Jani</span></h1>",
    unsafe_allow_html=True,
)

st.markdown(
    f"<p style='font-size:13px;color:#5a7a9a;line-height:1.8;max-width:580px;"
    f"font-family:{mono_fn},monospace;margin-bottom:28px;'>"
    "Python-Backend Developer &amp; ICT Student @ Marwadi University.<br>"
    "Building full-stack tools, AI platforms &amp; hardware-software systems."
    "</p>",
    unsafe_allow_html=True,
)

h1, h2, h3, h4, h5, _ = st.columns([1, 1, 1, 1, 1, 1])
with h1:
    st.link_button("⌥ GitHub", "https://github.com/JashJani02")
with h2:
    st.link_button("⌘ LinkedIn", "https://linkedin.com/in/jash-jani-58a49b322")
with h3:
    st.link_button("✦ Dev.to", "https://dev.to/jash_jani_02")
with h4:
    st.link_button("✉ jash.janee@gmail.com", "mailto:jash.janee@gmail.com")
with h5:
    if _resume_bytes:
        st.download_button(
            label="⤓ Resume",
            data=_resume_bytes,
            file_name="Jash_Jani_resume.pdf",
            mime="application/pdf",
        )

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════════════════════
section_header("Technical Skills")

skill_row("Languages",            ["Python", "Java", "C", "JavaScript", "R", "SQL", "Markdown"])
skill_row("Frameworks & Backend", ["Streamlit", "Flask", "Django", "REST APIs", "SQLite", "FFmpeg"])
skill_row("Data Science",         ["Pandas", "NumPy", "Matplotlib"])
skill_row("Tools & Platforms",    ["Git / GitHub", "VIM", "VS Code", "Jupyter Notebooks", "Arduino IDE", "Linux", "ComfyUI"])

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════════════════════
section_header("Projects")

projects = [
    ("multimedia_downloader",
     "Python library to download audio, video, and images from any social media platform. "
     "Published on PyPI — installable with a single pip command.",
     ["Python", "PyPI", "Open Source", "CLI"],
     "https://github.com/JashJani02/multimedia_downloader",
     None,
     "https://pypi.org/project/multimedia-downloader/"),

    ("Medly-AI",
     "Privacy-first medical AI platform powered by Ollama for fully local, on-device inference. "
     "No API keys, no data leaving the machine. Handles medical data processing and intelligent response generation.",
     ["Python", "Ollama", "AI/ML", "Local LLM"],
     "https://github.com/JashJani02/Medly-AI",
     None, None),

    ("Mathematical Equation Visualizer",
     "Interactive visualizer for mathematical equations and functions. "
     "Renders plots in real-time from user-defined expressions with a clean Streamlit interface.",
     ["Python", "Streamlit", "Matplotlib", "NumPy"],
     "https://github.com/JashJani02/MEV",
     "https://jash02-mev.streamlit.app/",
     None),

    ("CNC / PCB Plotter",
     "Software stack for a low-cost CNC/PCB Plotter. "
     "Co-authored the official patent draft application — documentation withheld from public repo for IP and privacy reasons.",
     ["Hardware", "Software Integration", "Patent Draft"],
     "https://github.com/JashJani02/3D-CNC-Plotter",
     None, None),

    ("A-V Downloader",
     "Web-based utility for high-quality media extraction using yt-dlp. "
     "Integrates FFmpeg for real-time format conversion. The core downloader logic later evolved into the multimedia_downloader PyPI library.",
     ["Python", "Flask", "Streamlit", "FFmpeg", "yt-dlp"],
     "https://github.com/JashJani02/A-V-Downloader",
     None, None),

    ("Image Downloader",
     "Script-based tool to automate bulk image retrieval and directory organisation "
     "via web scraping, with a live Streamlit UI.",
     ["Python", "Streamlit", "Web Scraping"],
     "https://github.com/JashJani02/Image-downloader",
     "https://jash02-image-downloader.streamlit.app/",
     None),
]

col_a, col_b, col_c = st.columns(3)
cols = [col_a, col_b, col_c]
for i, (title, desc, tags, gh, live, pypi) in enumerate(projects):
    with cols[i % 3]:
        project_card(title, desc, tags, gh, live, pypi)

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
section_header("Education")

e1_left, e1_right = st.columns([1, 4])
with e1_left:
    st.metric("CGPA", "8.67")
    st.caption("SGPA 8.43 · Current")
with e1_right:
    st.subheader("Diploma in Information & Communication Technology")
    st.write("**Marwadi University** · Rajkot, Gujarat")
    st.caption("July 2024 – May 2027 · 3rd Year Student")

st.write("")

e2_left, e2_right = st.columns([1, 4])
with e2_left:
    st.metric("SSC %", "77.03")
with e2_right:
    st.subheader("Secondary School Certificate (SSC)")
    st.write("**P.V. Modi School** · Rajkot, Gujarat")
    st.caption("Completed 2024")

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# CERTIFICATIONS & ACTIVITIES
# ══════════════════════════════════════════════════════════════════════════════
section_header("Certifications & Activities")

cert_col, club_col = st.columns(2)

with cert_col:
    st.markdown(
        f"<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        f"color:#3a5a8a;font-family:{mono_fn},monospace;margin-bottom:10px;'>Certifications</p>",
        unsafe_allow_html=True,
    )
    for cert in [
        "Cisco · Computer Hardware Basics",
        "Arduino Step-by-Step",
        "Learn Python by Coding: 10 Projects",
        '"Code Storm" Annual Technical Fest',
        "Linux & Version Control Seminars",
    ]:
        st.write(f"→ {cert}")

with club_col:
    st.markdown(
        f"<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        f"color:#3a5a8a;font-family:{mono_fn},monospace;margin-bottom:10px;'>Active Clubs</p>",
        unsafe_allow_html=True,
    )
    for club in ["10x Club", "Competitive Programming (CP)", "Cloud Computing & DevOps (CCDC)", "Data Science Club"]:
        st.write(f"`{club}`")

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# LANGUAGES
# ══════════════════════════════════════════════════════════════════════════════
section_header("Languages")

la, lb, lc, _ = st.columns([1, 1, 1, 4])
with la:
    st.metric("Gujarati", "Native")
with lb:
    st.metric("Hindi", "Fluent")
with lc:
    st.metric("English", "Proficient")

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    f"<p style='text-align:center;font-size:11px;color:#1e3a5a;"
    f"font-family:{mono_fn},monospace;letter-spacing:1px;padding:24px 0;'>"
    "⌥ &nbsp;Jash Jani · 2026 &nbsp;·&nbsp; Built with Python &amp; Streamlit &nbsp;⌘"
    "</p>",
    unsafe_allow_html=True,
)
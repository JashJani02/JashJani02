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

# ── Minimal CSS: only bg, hide chrome, style native widgets ───────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Syne:wght@700;800&display=swap');

[data-testid="stAppViewContainer"], [data-testid="stMain"], .main {
    background-color: #0a0c0f !important;
}
[data-testid="stHeader"], footer, [data-testid="stToolbar"] { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }

h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; color: #eaf0f8 !important; }
h2 { font-size: 26px !important; }
h3 { font-size: 22px !important; }
h4 { font-size: 18px !important; }
p, li, div, span, label { color: #c8d6e5; }

[data-testid="stMetricLabel"] > div {
    color: #5a7a9a !important;
    font-size: 11px !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-family: 'IBM Plex Mono', monospace !important;
}
[data-testid="stMetricValue"] > div {
    color: #4d9fff !important;
    font-size: 22px !important;
    font-family: 'IBM Plex Mono', monospace !important;
}

code {
    background: #0d141e !important;
    color: #7aafd4 !important;
    border: 1px solid #1a2a3a !important;
    border-radius: 2px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    padding: 2px 8px !important;
}

hr { border-color: #1a2030 !important; margin: 8px 0 !important; }

[data-testid="stExpander"] {
    background: #0d141e !important;
    border: 1px solid #1a2030 !important;
    border-radius: 0 !important;
    transition: border-color 0.2s;
}
[data-testid="stExpander"]:hover { border-color: #4d9fff40 !important; }
[data-testid="stExpander"] summary {
    color: #eaf0f8 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 20px !important;
}

[data-testid="stLinkButton"] > a {
    background: #0d1220 !important;
    border: 1px solid #1a2e50 !important;
    color: #4d9fff !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
}
[data-testid="stLinkButton"] > a:hover {
    background: #4d9fff15 !important;
    border-color: #4d9fff55 !important;
    color: #4d9fff !important;
}
            /* Download button — matches link buttons but with solid blue accent */
[data-testid="stDownloadButton"] > button {
    background: #0d1a2e !important;
    border: 1px solid #4d9fff55 !important;
    color: #4d9fff !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 1px;
    padding: 8px 20px !important;
}
[data-testid="stDownloadButton"] > button:hover {
    background: #4d9fff20 !important;
    border-color: #4d9fff !important;
    color: #fff !important;
}

[data-testid="stCaptionContainer"] p {
    color: #4a6a8a !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def section_header(title: str):
    st.markdown(
        f"<p style='font-size:15px;letter-spacing:4px;text-transform:uppercase;"
        f"color:#4d9fff;opacity:0.85;font-family:IBM Plex Mono,monospace;font-weight:600;"
        f"margin:0 0 4px 0;'>// {title}</p>",
        unsafe_allow_html=True,
    )
    st.divider()


def skill_row(category: str, skills: list):
    st.markdown(
        f"<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        f"color:#3a5a8a;font-family:IBM Plex Mono,monospace;margin:18px 0 6px;font-weight:600;'>"
        f"{category}</p>",
        unsafe_allow_html=True,
    )
    st.markdown("&nbsp;&nbsp;".join(f"`{s}`" for s in skills))


def project_card(num: str, title: str, desc: str, tags: list, gh_url: str):
    with st.expander(f"{num}  {title}"):
        st.caption(desc)
        st.markdown("&nbsp;&nbsp;".join(f"`{t}`" for t in tags))
        st.write("")
        st.link_button("→ View on GitHub", gh_url)


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════
st.write("")
st.markdown(
    "<h1 style='font-size:clamp(48px,8vw,88px);font-weight:800;line-height:0.95;"
    "letter-spacing:-3px;margin-bottom:16px;'>"
    "Jash <span style='color:#4d9fff;'>Jani</span></h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p style='font-size:13px;color:#5a7a9a;line-height:1.8;max-width:580px;"
    "font-family:IBM Plex Mono,monospace;margin-bottom:28px;'>"
    "Python-Backend Developer &amp; ICT Student @ Marwadi University.<br>"
    "Building full-stack tools, AI platforms &amp; hardware-software systems.<br>"

    "</p>",
    unsafe_allow_html=True,
)

# Social / contact links
h1, h2, h3, h4, h5, _ = st.columns([1, 1, 1, 1, 1, 1])
with h1:
    st.link_button("⌥ GitHub", "https://github.com/JashJani02")
with h2:
    st.link_button("⌘ LinkedIn", "https://linkedin.com/in/jash~jani-58a49b322")
with h3:
    st.link_button("✦ Dev.to", "https://dev.to/jash_jani_02")
with h4:
    st.link_button("✉ jash.janee@gmail.com", "mailto:jash.janee@gmail.com")
with h5:
    if _resume_bytes:
        st.download_button(
            label="⬇ Resume",
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
    ("01", "Medly-AI",
     "AI-centric platform for medical data processing and intelligent response generation. "
     "Backend handles async data requests and AI model outputs.",
     ["Python", "API Integration", "AI/ML"], "https://github.com/JashJani02/Medly-AI"),

    ("02", "CNC / PCB Plotter",
     "Software stack for a low-cost CNC/PCB Plotter. Co-authored the official patent application — "
     "demonstrating technical writing and IP expertise.",
     ["Hardware", "Software Integration"], "https://github.com/JashJani02/3D-CNC-Plotter"),

    ("03", "A-V Downloader",
     "Web-based utility for high-quality media extraction using yt-dlp. "
     "Integrates FFmpeg for real-time format conversion with server-side file handling.",
     ["Python", "Flask", "Streamlit", "FFmpeg", "yt-dlp"], "https://github.com/JashJani02/A-V-Downloader"),

    ("04", "Library Management System",
     "Full-stack CRUD application for managing digital library inventories "
     "built with Flask and a clean REST architecture.",
     ["Python", "Flask", "CRUD", "SQLite"], "https://github.com/JashJani02/Library-Management-System"),

    ("05", "Image Downloader",
     "Script-based tool to automate bulk image retrieval and directory organisation "
     "via web scraping, with a Streamlit UI.",
     ["Python", "Streamlit", "Web Scraping"], "https://github.com/JashJani02/Image-downloader"),

    ("06", "Music Player",
     "Built a Django Powered Music Player able to stream audio."
     "Transformed the audio downloader component into a Flask-based Microservice enabling the site to download to stream audio files in different formats.",
     ["Python", "Django", "Flask"], "https://github.com/JashJani02/Music-Player"),
    
    ("07", "Grid-Generator Game",
     "Interactive logic game using dynamic DOM manipulation and "
     "algorithm-based grid rendering in pure JavaScript.",
     ["JavaScript", "DOM", "Game Logic"], "https://github.com/JashJani02/Grid-Generator-game"),

    ("08", "Python Concepts",
     "Open-source beginner-friendly guide covering OOP, File Handling, and Data Structures. "
     "Recognised by faculty as potential curriculum material.",
     ["Python", "Jupyter", "Open Source", "Pedagogy"], "https://github.com/JashJani02/Basic-to-Intermediate-Python"),
]

col_a, col_b, col_c = st.columns(3)
cols = [col_a, col_b, col_c]
for i, (num, title, desc, tags, url) in enumerate(projects):
    with cols[i % 3]:
        project_card(num, title, desc, tags, url)

st.write("")
st.divider()

# ══════════════════════════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════════════════════════
section_header("Education")

e1_left, e1_right = st.columns([1, 4])
with e1_left:
    st.metric("CGPA", "8.76")
    st.caption("SGPA 8.23 · Current")
with e1_right:
    st.subheader("Diploma in Information & Communication Technology")
    st.write("**Marwadi University** · Rajkot, Gujarat")
    st.caption("July 2024 – May 2027 · 2nd Year Student")

st.write("")

e2_left, e2_right = st.columns([1, 4])
with e2_left:
    st.metric("SSC %", "70.03")
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
        "<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        "color:#3a5a8a;font-family:IBM Plex Mono,monospace;margin-bottom:10px;'>Certifications</p>",
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
        "<p style='font-size:13px;letter-spacing:3px;text-transform:uppercase;"
        "color:#3a5a8a;font-family:IBM Plex Mono,monospace;margin-bottom:10px;'>Active Clubs</p>",
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
    "<p style='text-align:center;font-size:11px;color:#1e3a5a;"
    "font-family:IBM Plex Mono,monospace;letter-spacing:1px;padding:24px 0;'>"
    "⌥ &nbsp;Jash Jani · 2025 &nbsp;·&nbsp; Built with Python &amp; Streamlit &nbsp;⌘"
    "</p>",
    unsafe_allow_html=True,
)

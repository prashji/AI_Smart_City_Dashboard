import streamlit as st
import base64
from pathlib import Path

# ==========================================
# PROJECT ROOT
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ==========================================
# LOAD CSS
# ==========================================

def load_css():

    css_path = PROJECT_ROOT / "css" / "style.css"

    if css_path.exists():

        with open(css_path, "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    else:

        st.error(f"CSS file not found:\n{css_path}")


# ==========================================
# IMAGE TO BASE64
# ==========================================

def image_to_base64(image_path):

    try:
        with open(image_path, "rb") as img:
            return base64.b64encode(img.read()).decode()

    except Exception:
        return None


# ==========================================
# SET BACKGROUND
# ==========================================

from pathlib import Path
import base64
import streamlit as st

def set_background(weather):
    
    project_root = Path(__file__).resolve().parent.parent

    image_path = project_root / "images" / f"{weather.lower()}.jpg"

    if image_path.exists():

        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()

        
        st.markdown(f"""
<style>

.stApp {{
    background:
        linear-gradient(
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.65)
        ),
        url("data:image/jpg;base64,{data}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: #f8fafc;
}}

</style>
""", unsafe_allow_html=True)

    else:
        st.error(f"Background image not found:\n{image_path}")

# ==========================================
# GLASS CARD
# ==========================================

def glass_card(content):

    return f"""
    <div class="glass-card">
        {content}
    </div>
    """


# ==========================================
# INFO CARD
# ==========================================

def info_card(title, value, icon="📊"):

    return f"""
    <div class="info-card">
        <h4>{icon} {title}</h4>
        <h2>{value}</h2>
    </div>
    """


# ==========================================
# SECTION TITLE
# ==========================================

def section_title(title):

    st.markdown(
        f"""
        <div class="section-title">
            <h2>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
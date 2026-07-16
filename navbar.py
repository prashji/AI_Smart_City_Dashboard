import streamlit as st
from datetime import datetime

def navbar(city):

    now = datetime.now()

    st.markdown(
        f"""
<div class="navbar">
    <div class="nav-left">🌍 <b>AI Smart City Dashboard</b></div>
    <div class="nav-center">📍 {city}</div>
    <div class="nav-right">
        📅 {now.strftime("%d %B %Y")} &nbsp;&nbsp;
        🕒 {now.strftime("%I:%M:%S %p")}
    </div>
</div>
""",
        unsafe_allow_html=True
    )
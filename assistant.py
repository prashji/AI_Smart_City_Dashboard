import streamlit as st

def ai_panel(recommendations):

    st.markdown("""
    <div class="glass-card">
        <h2>🤖 AI Assistant</h2>
    </div>
    """, unsafe_allow_html=True)

    for rec in recommendations:
        st.info(rec)
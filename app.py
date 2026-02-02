import streamlit as st

st.set_page_config(
    page_title="SQL Job Portal",
    layout="wide"
)

# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💼 Intelligent Job Portal (SQL-First)")

st.markdown("""
### Welcome 👋

This project demonstrates:
- SQL-first candidate matching
- MySQL joins, CTEs & window functions
- ML-based acceptance prediction
- GenAI-based resume parsing

👉 Use the **sidebar** to navigate through pages.
""")

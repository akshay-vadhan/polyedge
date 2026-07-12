import streamlit as st


def header():

    st.title("🚀 Polymarket Edge Pro")

    st.caption("AI Powered Paper Trading System")

    st.divider()


def section(title):

    st.markdown(f"## {title}")
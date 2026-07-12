import streamlit as st


def live_status():

    c1, c2, c3 = st.columns(3)

    c1.success("🟢 BOT RUNNING")

    c2.info("⚡ LIVE")

    c3.success("DATABASE CONNECTED")
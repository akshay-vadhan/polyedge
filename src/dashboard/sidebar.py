import streamlit as st


def render_sidebar():

    st.sidebar.title("🚀 Polymarket Edge")

    st.sidebar.success("Bot Running")

    refresh = st.sidebar.slider(

        "Refresh",

        1,

        10,

        2

    )

    st.sidebar.markdown("---")

    st.sidebar.write("Mode")

    st.sidebar.info("Paper Trading")

    st.sidebar.write("Version")

    st.sidebar.success("V3")

    return refresh
import streamlit as st


def load_theme():

    st.markdown(
        """
<style>

.main{

    background:#0E1117;

}

.metric-container{

    background:#1F2937;

    padding:15px;

    border-radius:10px;

}

.block-container{

    padding-top:1rem;

}

div[data-testid="metric-container"]{

    background:#1F2937;

    border-radius:10px;

    padding:12px;

    border:1px solid #333;

}

</style>

""",
        unsafe_allow_html=True
    )
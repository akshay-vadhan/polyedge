import streamlit as st


def render_latest_trade(df):

    st.subheader("Latest Trade")

    if df.empty:

        st.info("No Trades")

        return

    st.dataframe(

        df,

        use_container_width=True

    )


def render_trade_history(df):

    st.subheader("Trade History")

    st.dataframe(

        df,

        width="stretch"

    )
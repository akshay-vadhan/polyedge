import plotly.express as px
import streamlit as st


def render_btc_chart(df):

    if df.empty:

        return

    chart = df.sort_values("timestamp")

    fig = px.line(

        chart,

        x="timestamp",

        y="btc_price",

        title="BTC Price"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )


def render_yes_no_chart(df):

    if df.empty:

        return

    chart = df.sort_values("timestamp")

    fig = px.line(

        chart,

        x="timestamp",

        y=[

            "yes_price",

            "no_price"

        ],

        title="YES vs NO"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )
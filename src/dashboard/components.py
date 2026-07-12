import streamlit as st


def render_signal(trade):

    st.subheader("Signal")

    if trade.empty:

        st.warning("No Signal")

        return

    row = trade.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Side",

        row["side"]

    )

    c2.metric(

        "Status",

        row["status"]

    )

    c3.metric(

        "Confidence",

        row["confidence"]

    )


def render_stats(stats):

    row = stats.iloc[0]

    c1, c2, c3 = st.columns(3)

    c1.metric(

        "Trades",

        int(row["total"])

    )

    c2.metric(

        "Wins",

        int(row["wins"])

    )

    c3.metric(

        "PnL",

        round(row["pnl"], 4)

    )
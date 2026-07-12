import streamlit as st


def render_metrics(latest):

    if latest.empty:

        st.warning("No Market Data")

        return

    row = latest.iloc[0]

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "BTC",
        f"${row['btc_price']:.2f}"
    )

    c2.metric(
        "YES",
        f"{row['yes_price']:.3f}"
    )

    c3.metric(
        "NO",
        f"{row['no_price']:.3f}"
    )

    c4.metric(
        "Spread",
        f"{row['yes_spread']:.3f}"
    )

    c5.metric(
        "Volume",
        round(row["volume"], 2)
    )
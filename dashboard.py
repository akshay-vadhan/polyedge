import sqlite3
import pandas as pd
import streamlit as st
from datetime import datetime, timezone
import time



# -----------------------------
# Dashboard Modules
# -----------------------------

from src.dashboard.theme import load_theme
from src.dashboard.sidebar import render_sidebar
from src.dashboard.layout import header
from src.dashboard.live import live_status

from src.dashboard.metrics import render_metrics



from src.dashboard.tables import (
    render_latest_trade,
    render_trade_history
)

from src.dashboard.components import (
    render_signal,
    render_stats
)

from streamlit_autorefresh import st_autorefresh

st_autorefresh(
    interval=1000,   # 1 second
    key="live"
)

# -----------------------------
# Streamlit Config
# -----------------------------

st.set_page_config(

    page_title="Polymarket Edge Pro",

    page_icon="🚀",

    layout="wide"

)


start = time.time()

# -----------------------------
# Theme
# -----------------------------

load_theme()

refresh = render_sidebar()

header()

live_status()

# -----------------------------
# Database
# -----------------------------

DB = "data/polymarket.db"

conn = sqlite3.connect(DB)

# -----------------------------
# Latest Tick
# -----------------------------

latest = pd.read_sql("""

SELECT *

FROM market_ticks

ORDER BY id DESC

LIMIT 1

""", conn)

if not latest.empty:

    last_tick = latest.iloc[0]["timestamp"]

    last_tick = datetime.fromisoformat(
        last_tick.replace("Z", "+00:00")
    )

    seconds = (
        datetime.now(timezone.utc) - last_tick
    ).total_seconds()

    if seconds < 3:
        st.success("🟢 BOT RUNNING")
    else:
        st.error("🔴 BOT OFFLINE")

else:

    st.warning("No market data available")

# -----------------------------
# Latest Trade
# -----------------------------

latest_trade = pd.read_sql("""

SELECT *

FROM paper_trades

ORDER BY id DESC

LIMIT 1

""", conn)



# -----------------------------
# Recent Ticks
# -----------------------------

ticks = pd.read_sql("""

SELECT

timestamp,

btc_price,

yes_price,

no_price

FROM market_ticks

ORDER BY id DESC

LIMIT 300

""", conn)

# -----------------------------
# Trade History
# -----------------------------

history = pd.read_sql("""

SELECT

entry_time,

market_slug,

side,

status,

entry_price,

exit_price,

pnl,

roi

FROM paper_trades

ORDER BY id DESC

LIMIT 30

""", conn)

# -----------------------------
# Statistics
# -----------------------------

stats = pd.read_sql("""

SELECT

COUNT(*) total,

SUM(

CASE

WHEN pnl > 0

THEN 1

ELSE 0

END

) wins,

COALESCE(

SUM(pnl),

0

) pnl

FROM paper_trades

""", conn)

conn.close()

# ===========================================================
# TOP METRICS
# ===========================================================

render_metrics(latest)

st.divider()

# ===========================================================
# SIGNAL
# ===========================================================

render_signal(latest_trade)

st.divider()

# ===========================================================
# CHARTS
# ===========================================================



# ===========================================================
# TABLES
# ===========================================================

left, right = st.columns(2)

with left:

    render_latest_trade(latest_trade)

with right:

    render_trade_history(history)

st.divider()

# ===========================================================
# STATS
# ===========================================================

render_stats(stats)

st.divider()

# ===========================================================
# FOOTER
# ===========================================================

st.markdown(
    """
---
### 🚀 Polymarket Edge Pro

AI Powered Paper Trading Dashboard

Version : **4.0**

Status : **RUNNING**
"""
)

st.caption(f"Dashboard Render Time : {round(time.time()-start,2)} sec")
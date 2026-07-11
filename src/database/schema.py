"""
Database Schema
"""

MARKETS_TABLE = """
CREATE TABLE IF NOT EXISTS markets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    slug TEXT UNIQUE NOT NULL,

    condition_id TEXT NOT NULL,

    up_token TEXT NOT NULL,

    down_token TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""


MARKET_TICKS_TABLE = """
CREATE TABLE IF NOT EXISTS market_ticks (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    market_slug TEXT,

    btc_price REAL,

    yes_price REAL,
    no_price REAL,

    yes_bid REAL,
    yes_ask REAL,
    yes_mid REAL,
    yes_spread REAL,

    yes_bid_volume REAL,
    yes_ask_volume REAL,
    yes_imbalance REAL,

    no_bid REAL,
    no_ask REAL,
    no_mid REAL,
    no_spread REAL,

    no_bid_volume REAL,
    no_ask_volume REAL,
    no_imbalance REAL,

    last_trade REAL,

    liquidity REAL,

    volume REAL,

    one_hour_change REAL
);
"""


PAPER_TRADES_TABLE = """
CREATE TABLE IF NOT EXISTS paper_trades(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    trade_id TEXT UNIQUE,

    market_slug TEXT,

    side TEXT,

    status TEXT,

    entry_time TEXT,

    exit_time TEXT,

    entry_price REAL,

    exit_price REAL,

    btc_entry REAL,

    btc_exit REAL,

    confidence INTEGER,

    score INTEGER,

    pnl REAL,

    roi REAL,

    result TEXT,

    reason TEXT

);
"""
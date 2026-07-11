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

    timestamp TEXT NOT NULL,

    market_slug TEXT NOT NULL,

    btc_price REAL,

    yes_bid REAL,
    yes_ask REAL,

    no_bid REAL,
    no_ask REAL,

    yes_last REAL,
    no_last REAL,

    spread REAL,

    remaining_seconds INTEGER

);
"""


PAPER_TRADES_TABLE = """
CREATE TABLE IF NOT EXISTS paper_trades (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    entry_time TEXT,

    exit_time TEXT,

    side TEXT,

    entry_price REAL,

    exit_price REAL,

    pnl REAL,

    strategy TEXT

);
"""
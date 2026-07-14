"""
Paper Trading V2 Schema
"""

PORTFOLIO_TABLE = """

CREATE TABLE IF NOT EXISTS portfolio(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    balance REAL,

    available_cash REAL,

    locked_cash REAL,

    equity REAL,

    total_pnl REAL,

    created_at TEXT,

    updated_at TEXT

);

"""

POSITIONS_TABLE = """

CREATE TABLE IF NOT EXISTS positions(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    position_id TEXT UNIQUE,

    market_slug TEXT,

    side TEXT,

    status TEXT,

    entry_price REAL,

    current_price REAL,

    shares REAL,

    trade_amount REAL,

    current_value REAL,

    unrealized_pnl REAL,

    realized_pnl REAL,

    max_payout REAL,

    max_profit REAL,

    max_loss REAL,

    opened_at TEXT,

    closed_at TEXT,

    resolution TEXT,

    result TEXT

);

"""

PORTFOLIO_HISTORY_TABLE = """

CREATE TABLE IF NOT EXISTS portfolio_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    balance REAL,

    equity REAL,

    total_pnl REAL,

    snapshot_time TEXT

);

"""
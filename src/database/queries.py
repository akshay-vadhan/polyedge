INSERT_MARKET_TICK = """
INSERT INTO market_ticks(

timestamp,
market_slug,

btc_price,

yes_price,
no_price,

yes_bid,
yes_ask,
yes_mid,
yes_spread,

yes_bid_volume,
yes_ask_volume,
yes_imbalance,

no_bid,
no_ask,
no_mid,
no_spread,

no_bid_volume,
no_ask_volume,
no_imbalance,

last_trade,

liquidity,

volume,

one_hour_change

)

VALUES(
?,?,?,?,?,
?,?,?,?,?,
?,?,?,?,?,
?,?,?,?,?,
?,?,?
)
"""



INSERT_PAPER_TRADE = """
INSERT INTO paper_trades(

trade_id,
market_slug,
side,
status,

entry_time,
exit_time,

entry_price,
exit_price,

btc_entry,
btc_exit,

confidence,
score,

pnl,
roi,

result,

reason

)

VALUES(

?,?,?,?,?,
?,
?,?,?,?,?,
?,
?,?,?,
?

)
"""
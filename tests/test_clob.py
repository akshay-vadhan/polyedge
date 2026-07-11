from src.api.gamma import GammaClient
from src.api.clob import ClobClient


def print_book(title, book):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    print(f"Best Bid   : {book.best_bid:.2f}")
    print(f"Best Ask   : {book.best_ask:.2f}")
    print(f"Mid Price  : {book.mid_price:.2f}")
    print(f"Spread     : {book.spread:.2f}")
    print(f"Bid Volume : {book.bid_volume:.2f}")
    print(f"Ask Volume : {book.ask_volume:.2f}")
    print(f"Imbalance  : {book.imbalance:.4f}")

    print("\nTop 5 Bids")
    for level in book.bids[:5]:
        print(f"  {level.price:.2f}  |  {level.size:.2f}")

    print("\nTop 5 Asks")
    for level in book.asks[:5]:
        print(f"  {level.price:.2f}  |  {level.size:.2f}")


def main():

    gamma = GammaClient()
    clob = ClobClient()

    market = gamma.find_active_btc_market()

    print(f"\nMarket : {market.slug}")

    up = clob.get_orderbook(market.up_token)
    down = clob.get_orderbook(market.down_token)

    print_book("UP ORDERBOOK", up)
    print_book("DOWN ORDERBOOK", down)


if __name__ == "__main__":
    main()
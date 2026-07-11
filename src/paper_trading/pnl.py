class PnLCalculator:

    @staticmethod
    def calculate(side, entry, winner):

        if side == winner:

            exit_price = 1.0

        else:

            exit_price = 0.0

        pnl = exit_price - entry

        roi = 0

        if entry > 0:

            roi = (pnl / entry) * 100

        return {

            "exit_price": exit_price,

            "pnl": round(pnl, 4),

            "roi": round(roi, 2)

        }
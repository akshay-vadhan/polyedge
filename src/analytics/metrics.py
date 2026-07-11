class Metrics:

    @staticmethod
    def pct_change(old, new):

        if old == 0:

            return 0

        return (new - old) / old
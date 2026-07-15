class TopIncome:
    """
    Return the largest credit transactions.
    """

    def generate(
        self,
        transactions: list[dict],
        top_n: int = 10,
    ) -> list[dict]:

        income = [
            tx
            for tx in transactions
            if (tx.get("credit") or 0.0) > 0
        ]

        income.sort(
            key=lambda tx: tx["credit"],
            reverse=True,
        )

        return income[:top_n]
class TopExpenses:
    """
    Return the largest debit transactions.
    """

    def generate(
        self,
        transactions: list[dict],
        top_n: int = 10,
    ) -> list[dict]:

        expenses = [
            tx
            for tx in transactions
            if (tx.get("debit") or 0.0) > 0
        ]

        expenses.sort(
            key=lambda tx: tx["debit"],
            reverse=True,
        )

        return expenses[:top_n]
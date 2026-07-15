class InterestDetector:
    """
    Detect interest-related transactions.
    """

    KEYWORDS = [
        "INTEREST",
        "INT",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        interest_transactions = []

        credit_total = 0.0
        debit_total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(keyword in description for keyword in self.KEYWORDS):

                interest_transactions.append(tx)

                credit_total += tx.get("credit") or 0.0
                debit_total += tx.get("debit") or 0.0

        return {
            "interest_credit": credit_total,
            "interest_debit": debit_total,
            "count": len(interest_transactions),
            "transactions": interest_transactions,
        }
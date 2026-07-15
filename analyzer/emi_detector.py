import re


class EMIDetector:
    """
    Detect EMI and loan repayment transactions.
    """

    KEYWORDS = [
        "EMI",
        "LOAN",
        "REPAYMENT",
        "INSTALLMENT",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        emi_transactions = []

        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(
                re.search(rf"\b{re.escape(keyword)}\b", description)
                for keyword in self.KEYWORDS
            ):
                emi_transactions.append(tx)

                total += tx.get("debit") or 0.0

        return {
            "total": total,
            "count": len(emi_transactions),
            "transactions": emi_transactions,
        }
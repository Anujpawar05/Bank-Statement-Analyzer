import re


class CashWithdrawalDetector:
    """
    Detect cash withdrawal transactions.
    """

    KEYWORDS = [
        "ATM",
        "WDL",
        "CASH WDL",
        "WITHDRAWAL",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        withdrawals = []
        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(
                re.search(rf"\b{re.escape(keyword)}\b", description)
                for keyword in self.KEYWORDS
            ):
                withdrawals.append(tx)

                total += tx.get("debit") or 0.0

        return {
            "total": total,
            "count": len(withdrawals),
            "transactions": withdrawals,
        }
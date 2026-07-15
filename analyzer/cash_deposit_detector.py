import re


class CashDepositDetector:
    """
    Detect cash deposit transactions.
    """

    KEYWORDS = [
        "CASH DEPOSIT",
        "CSH DEP",
        "DEPOSITED",
        "CDM",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        deposits = []
        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(
                re.search(rf"\b{re.escape(keyword)}\b", description)
                for keyword in self.KEYWORDS
            ):
                deposits.append(tx)

                total += tx.get("credit") or 0.0

        return {
            "total": total,
            "count": len(deposits),
            "transactions": deposits,
        }
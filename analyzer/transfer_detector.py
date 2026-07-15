import re


class TransferDetector:
    """
    Detect bank transfer transactions.
    """

    KEYWORDS = [
        "UPI",
        "NEFT",
        "IMPS",
        "RTGS",
        "INB",
        "TRANSFER",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        transfers = []
        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(
                re.search(rf"\b{re.escape(keyword)}\b", description)
                for keyword in self.KEYWORDS
            ):
                transfers.append(tx)

                amount = (
                    tx.get("debit")
                    or tx.get("credit")
                    or 0.0
                )

                total += amount

        return {
            "total": total,
            "count": len(transfers),
            "transactions": transfers,
        }
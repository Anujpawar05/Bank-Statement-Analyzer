from collections import defaultdict


class RecurringDetector:
    """
    Detect recurring merchants by grouping transactions
    having the same merchant.
    """

    def detect(self, transactions: list[dict]) -> dict:

        merchants = defaultdict(
            lambda: {
                "count": 0,
                "total": 0.0,
            }
        )

        for tx in transactions:

            merchant = tx.get("merchant", "").strip().upper()

            if not merchant:
                continue

            amount = (
                tx.get("debit")
                or tx.get("credit")
                or tx.get("amount")
                or 0.0
            )

            merchants[merchant]["count"] += 1
            merchants[merchant]["total"] += amount

        recurring = {}

        total_amount = 0.0

        for merchant, data in merchants.items():

            if data["count"] >= 2:

                recurring[merchant] = data

                total_amount += data["total"]

        return {
            "count": len(recurring),
            "total": total_amount,
            "merchants": recurring,
        }
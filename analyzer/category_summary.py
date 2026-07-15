class CategorySummary:
    """
    Generate spending summary by transaction category.
    """

    def generate(self, transactions: list[dict]) -> dict:

        report = {}

        for tx in transactions:

            category = tx.get("category", "Uncategorized")

            amount = tx.get("debit") or 0.0

            report.setdefault(category, 0.0)

            report[category] += amount

        return report
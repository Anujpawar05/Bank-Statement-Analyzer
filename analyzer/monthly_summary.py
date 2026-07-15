class MonthlySummary:
    """
    Generate month-wise income and expense summary.
    """

    def generate(self, transactions: list[dict]) -> dict:

        report = {}

        for tx in transactions:

            month = tx["date"][3:]

            if month not in report:

                report[month] = {
                    "income": 0.0,
                    "expense": 0.0,
                    "net": 0.0,
                }

            report[month]["income"] += tx.get("credit") or 0.0

            report[month]["expense"] += tx.get("debit") or 0.0

            report[month]["net"] = (
                report[month]["income"]
                - report[month]["expense"]
            )

        return report
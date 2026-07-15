import re


class SalaryDetector:
    """
    Detect salary-related transactions.
    """

    KEYWORDS = [
        "SALARY",
        "PAYROLL",
        "SAL",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        salaries = []
        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(
                re.search(rf"\b{re.escape(keyword)}\b", description)
                for keyword in self.KEYWORDS
            ):
                salaries.append(tx)

                amount = tx.get("credit") or tx.get("amount") or 0.0
                total += amount

        return {
            "salary_total": total,
            "count": len(salaries),
            "transactions": salaries,
        }
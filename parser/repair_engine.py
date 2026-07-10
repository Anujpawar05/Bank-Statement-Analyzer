from typing import List, Dict


class RepairEngine:
    """
    Attempts to detect transactions that are mathematically inconsistent.

    This version DOES NOT modify transactions.
    It only reports which transactions appear repairable.
    """

    def analyze(self, transactions: List[Dict]) -> List[Dict]:
        issues = []

        if len(transactions) < 2:
            return issues

        previous_balance = transactions[0]["balance"]

        for i in range(1, len(transactions)):
            tx = transactions[i]

            debit = tx["debit"]
            credit = tx["credit"]
            balance = tx["balance"]

            expected_balance = previous_balance - debit + credit

            difference = round(balance - expected_balance, 2)

            if abs(difference) > 0.01:
                issues.append(
                    {
                        "index": i,
                        "date": tx["date"],
                        "description": tx["description"][:80],
                        "expected_balance": expected_balance,
                        "actual_balance": balance,
                        "difference": difference,
                        "repairable": (
                            debit == 0
                            or credit == 0
                            or balance == 0
                        )
                    }
                )

            previous_balance = balance

        return issues
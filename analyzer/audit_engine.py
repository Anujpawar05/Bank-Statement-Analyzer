class AuditEngine:
    """
    Performs financial integrity checks on parsed transactions.

    Unlike RepairEngine, this class NEVER modifies data.
    It only reports inconsistencies.
    """

    def audit(self, transactions):

        report = {
            "passed": 0,
            "failed": 0,
            "issues": []
        }

        if len(transactions) < 2:
            return report

        previous_balance = transactions[0]["balance"]

        for i in range(1, len(transactions)):

            t = transactions[i]

            debit = t.get("debit", 0.0)
            credit = t.get("credit", 0.0)
            balance = t.get("balance", 0.0)

            expected = round(previous_balance - debit + credit, 2)

            difference = round(balance - expected, 2)

            if abs(difference) <= 0.01:

                report["passed"] += 1

            else:

                report["failed"] += 1

                report["issues"].append({
                    "index": i,
                    "date": t["date"],
                    "expected_balance": expected,
                    "actual_balance": balance,
                    "difference": difference,
                    "message": (
                        f"Expected {expected:.2f}, "
                        f"found {balance:.2f}"
                    )
                })

            previous_balance = balance

        return report
class RepairEngine:
    """
    Attempts safe mathematical reconciliation of parsed transactions.
    Only repairs values when they can be inferred with certainty.
    """

    def analyze(self, transactions):
        repairs = []

        if len(transactions) < 2:
            return repairs

        previous_balance = transactions[0]["balance"]

        for index in range(1, len(transactions)):

            t = transactions[index]

            debit = t.get("debit", 0.0)
            credit = t.get("credit", 0.0)
            balance = t.get("balance", 0.0)

            expected = round(previous_balance - debit + credit, 2)

            repaired = False
            repair_type = None

            # --------------------------
            # Missing balance
            # --------------------------
            if balance == 0:
                t["balance"] = expected
                balance = expected

                repaired = True
                repair_type = "balance"

            # --------------------------
            # Missing debit
            # --------------------------
            elif debit == 0 and credit == 0:

                pass

            # --------------------------
            # Missing debit
            # --------------------------
            elif debit == 0 and balance < previous_balance:

                inferred = round(previous_balance + credit - balance, 2)

                if inferred > 0:
                    t["debit"] = inferred

                    repaired = True
                    repair_type = "debit"

            # --------------------------
            # Missing credit
            # --------------------------
            elif credit == 0 and balance > previous_balance:

                inferred = round(balance - previous_balance + debit, 2)

                if inferred > 0:
                    t["credit"] = inferred

                    repaired = True
                    repair_type = "credit"

            difference = round(balance - expected, 2)

            if repaired or abs(difference) > 0.01:

                repairs.append({
                    "index": index,
                    "date": t["date"],
                    "repair_type": repair_type,
                    "difference": difference,
                    "repaired": repaired
                })

            previous_balance = t["balance"]

        return repairs
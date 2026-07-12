class RepairEngine:
    """
    Attempts safe mathematical reconciliation of parsed transactions.
    Repairs only when a value can be inferred confidently.
    """

    TOLERANCE = 0.01

    def analyze(self, transactions):

        repairs = []

        if len(transactions) < 2:
            return repairs

        previous_balance = transactions[0]["balance"]

        for index in range(1, len(transactions)):

            t = transactions[index]

            debit = float(t.get("debit", 0.0))
            credit = float(t.get("credit", 0.0))
            balance = float(t.get("balance", 0.0))

            expected = round(previous_balance - debit + credit, 2)

            repaired = False
            repair_type = None

            # ---------------------------------------------------
            # Rule 1 : Missing balance
            # ---------------------------------------------------
            if balance == 0:

                t["balance"] = expected
                balance = expected

                repaired = True
                repair_type = "balance"

            # ---------------------------------------------------
            # Rule 2 : Missing debit
            # ---------------------------------------------------
            elif debit == 0 and credit > 0 and balance < previous_balance:

                inferred = round(previous_balance + credit - balance, 2)

                if inferred > 0:

                    t["debit"] = inferred

                    repaired = True
                    repair_type = "debit"

            # ---------------------------------------------------
            # Rule 3 : Missing credit
            # ---------------------------------------------------
            elif credit == 0 and debit > 0 and balance > previous_balance:

                inferred = round(balance - previous_balance + debit, 2)

                if inferred > 0:

                    t["credit"] = inferred

                    repaired = True
                    repair_type = "credit"

            # ---------------------------------------------------
            # Rule 4 : Missing leading digit in balance
            # Example:
            # Expected = 4771.30
            # OCR      = 771.30
            # ---------------------------------------------------
            elif abs(balance - expected) > 1000:

                expected_str = f"{expected:.2f}"
                balance_str = f"{balance:.2f}"

                if expected_str.endswith(balance_str):

                    t["balance"] = expected
                    balance = expected

                    repaired = True
                    repair_type = "leading_digit"

            # ---------------------------------------------------
            # Rule 5 : Large OCR difference
            # ---------------------------------------------------
            difference = round(balance - expected, 2)

            if (
                not repaired
                and abs(difference) > 5000
                and balance != 0
            ):
                # Keep record for review but do not auto-fix
                repair_type = "manual_review"

            if repaired or repair_type == "manual_review":

                repairs.append({
                    "index": index,
                    "date": t["date"],
                    "repair_type": repair_type,
                    "difference": difference,
                    "repaired": repaired
                })

            previous_balance = t["balance"]

        return repairs
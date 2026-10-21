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

        # Infer first transaction's balance if missing
        if transactions[0].get("balance", 0.0) == 0 and len(transactions) > 1:
            t1 = transactions[1]
            t1_bal = float(t1.get("balance", 0.0))
            t1_deb = float(t1.get("debit", 0.0))
            t1_crd = float(t1.get("credit", 0.0))
            if t1_bal > 0:
                transactions[0]["balance"] = round(t1_bal + t1_deb - t1_crd, 2)

        previous_balance = float(transactions[0].get("balance", 0.0))

        for index in range(1, len(transactions)):

            t = transactions[index]

            debit = float(t.get("debit", 0.0))
            credit = float(t.get("credit", 0.0))
            balance = float(t.get("balance", 0.0))

            repaired = False
            repair_type = None

            # ---------------------------------------------------
            # Rule 0 : Both debit and credit present (mutually exclusive)
            # ---------------------------------------------------
            if debit > 0 and credit > 0:
                if balance > 0 and previous_balance > 0:
                    if balance < previous_balance:
                        t["debit"] = round(previous_balance - balance, 2)
                        t["credit"] = 0.0
                    else:
                        t["credit"] = round(balance - previous_balance, 2)
                        t["debit"] = 0.0
                else:
                    # Keep larger or default to debit
                    if credit > debit:
                        t["debit"] = 0.0
                    else:
                        t["credit"] = 0.0
                repaired = True
                repair_type = "both_amounts_resolved"
                debit = float(t.get("debit", 0.0))
                credit = float(t.get("credit", 0.0))

            expected = round(previous_balance - debit + credit, 2)

            # ---------------------------------------------------
            # Rule 1 : Missing balance
            # ---------------------------------------------------
            if balance == 0:

                t["balance"] = expected
                balance = expected

                repaired = True
                repair_type = "balance"

            # ---------------------------------------------------
            # Rule 2 : Misclassified as credit (balance decreased)
            # ---------------------------------------------------
            elif debit == 0 and credit > 0 and balance < previous_balance:

                drop = round(previous_balance - balance, 2)
                t["debit"] = credit if abs(credit - drop) <= 0.05 else drop
                t["credit"] = 0.0
                debit = t["debit"]
                credit = 0.0

                repaired = True
                repair_type = "credit_reclassified_to_debit"

            # ---------------------------------------------------
            # Rule 3 : Misclassified as debit (balance increased)
            # ---------------------------------------------------
            elif credit == 0 and debit > 0 and balance > previous_balance:

                gain = round(balance - previous_balance, 2)
                t["credit"] = debit if abs(debit - gain) <= 0.05 else gain
                t["debit"] = 0.0
                credit = t["credit"]
                debit = 0.0

                repaired = True
                repair_type = "debit_reclassified_to_credit"

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
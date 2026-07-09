class AnalysisEngine:
    """
    Performs financial analysis on parsed transactions.
    """

    def analyze(self, transactions):
        """
        Analyze a list of transactions.

        Parameters
        ----------
        transactions : list

        Returns
        -------
        dict
        """

        total_debit = 0.0
        total_credit = 0.0

        largest_debit = 0.0
        largest_credit = 0.0

        debit_count = 0
        credit_count = 0

        category_summary = {}

        for transaction in transactions:

            debit = transaction.get("debit", 0.0)
            credit = transaction.get("credit", 0.0)
            category = transaction.get("category")

            total_debit += debit
            total_credit += credit

            # Category-wise spending (only debits)
            if category and debit > 0:
                category_summary[category] = (
                    category_summary.get(category, 0.0) + debit
                )

            if debit > largest_debit:
                largest_debit = debit

            if credit > largest_credit:
                largest_credit = credit

            if debit > 0:
                debit_count += 1

            if credit > 0:
                credit_count += 1

        net_cash_flow = total_credit - total_debit

        average_debit = (
            total_debit / debit_count
            if debit_count
            else 0.0
        )

        average_credit = (
            total_credit / credit_count
            if credit_count
            else 0.0
        )

        return {
            "total_debit": total_debit,
            "total_credit": total_credit,
            "net_cash_flow": net_cash_flow,
            "transaction_count": len(transactions),
            "largest_debit": largest_debit,
            "largest_credit": largest_credit,
            "debit_count": debit_count,
            "credit_count": credit_count,
            "average_debit": average_debit,
            "average_credit": average_credit,
            "category_summary": category_summary,
        }
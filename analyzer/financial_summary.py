class FinancialSummary:
    """
    Generate overall financial metrics from detector outputs.
    """

    def generate(self, insights: dict) -> dict:
        """
        Generate overall financial metrics from detector outputs.
        """

        salary = insights["salary"].get(
            "total",
            insights["salary"].get("salary_total", 0.0),
        )

        interest = insights["interest"].get(
        "total",
            insights["interest"].get("interest_total", 0.0),
        )

        deposits = insights["cash_deposits"].get("total", 0.0)

        charges = insights["bank_charges"].get(
        "total",
            insights["bank_charges"].get("charges_total", 0.0),
        )

        emi = insights["emi"].get(
        "total",
            insights["emi"].get("emi_total", 0.0),
    )

        withdrawals = insights["cash_withdrawals"].get("total", 0.0)

        transfers = insights["transfers"].get("total", 0.0)

        total_income = (
            salary
            + interest
            + deposits
        )

        total_expense = (
            charges
            + emi
            + withdrawals
            + transfers
       )

        net_cash_flow = total_income - total_expense

        return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_cash_flow": net_cash_flow,
        }

        
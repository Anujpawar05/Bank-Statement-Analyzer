from analyzer.insight_engine import InsightEngine
from analyzer.financial_summary import FinancialSummary
from analyzer.monthly_summary import MonthlySummary
from analyzer.category_summary import CategorySummary
from analyzer.top_expenses import TopExpenses
from analyzer.top_income import TopIncome


class ReportGenerator:
    """
    Generate the complete analysis report for a bank statement.
    """

    def __init__(self):

        self.insight_engine = InsightEngine()
        self.financial_summary = FinancialSummary()
        self.monthly_summary = MonthlySummary()
        self.category_summary = CategorySummary()
        self.top_expenses = TopExpenses()
        self.top_income = TopIncome()

    def generate(
        self,
        transactions: list[dict],
        metadata: dict,
    ) -> dict:

        insights = self.insight_engine.generate(transactions)

        summary = self.financial_summary.generate(insights)

        monthly = self.monthly_summary.generate(transactions)

        category = self.category_summary.generate(transactions)

        expenses = self.top_expenses.generate(transactions)

        income = self.top_income.generate(transactions)

        return {
            "metadata": metadata,
            "insights": insights,
            "financial_summary": summary,
            "monthly_summary": monthly,
            "category_summary": category,
            "top_expenses": expenses,
            "top_income": income,
            "transactions": transactions,
        }
from analyzer.report_generator import ReportGenerator


transactions = [
    {
        "date": "01/04/2026",
        "description": "SALARY CREDIT",
        "credit": 50000.0,
        "debit": None,
        "category": "Salary",
    },
    {
        "date": "03/04/2026",
        "description": "ATM CASH WITHDRAWAL",
        "credit": None,
        "debit": 5000.0,
        "category": "Cash",
    },
]


metadata = {
    "bank_name": "STATE BANK OF INDIA",
    "account_holder": "JOHN DOE",
}


def test_generate_report():

    generator = ReportGenerator()

    report = generator.generate(
        transactions=transactions,
        metadata=metadata,
    )

    assert "metadata" in report
    assert "insights" in report
    assert "financial_summary" in report
    assert "monthly_summary" in report
    assert "category_summary" in report
    assert "top_expenses" in report
    assert "top_income" in report
    assert "transactions" in report
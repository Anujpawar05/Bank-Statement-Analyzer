from analyzer.insight_engine import InsightEngine


transactions = [

    {
        "description": "SALARY CREDIT",
        "credit": 50000.0,
        "debit": None,
    },

    {
        "description": "ATM CASH WITHDRAWAL",
        "credit": None,
        "debit": 3000.0,
    },

    {
        "description": "BANK CHARGES",
        "credit": None,
        "debit": 295.0,
    },

    {
        "description": "HOME LOAN EMI",
        "credit": None,
        "debit": 15000.0,
    },

    {
        "description": "UPI/DR/ABC",
        "credit": None,
        "debit": 500.0,
    },

    {
        "description": "INTEREST CREDIT",
        "credit": 120.0,
        "debit": None,
    },

    {
        "description": "NETFLIX SUBSCRIPTION",
        "credit": None,
        "debit": 649.0,
    },
]


def test_generate_report():

    engine = InsightEngine()

    report = engine.generate(transactions)

    assert "salary" in report
    assert "interest" in report
    assert "bank_charges" in report
    assert "recurring" in report
    assert "emi" in report
    assert "cash_deposits" in report
    assert "cash_withdrawals" in report
    assert "transfers" in report
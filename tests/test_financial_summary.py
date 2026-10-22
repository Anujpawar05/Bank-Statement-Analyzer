from analyzer.financial_summary import FinancialSummary


insights = {
    "salary": {
        "salary_total": 50000.0,
    },
    "interest": {
        "interest_total": 250.0,
    },
    "cash_deposits": {
        "total": 10000.0,
    },
    "bank_charges": {
        "charges_total": 295.0,
    },
    "emi": {
        "total": 15000.0,
    },
    "cash_withdrawals": {
        "total": 3000.0,
    },
    "transfers": {
        "total": 500.0,
    },
}


def test_total_income():

    summary = FinancialSummary()

    report = summary.generate(insights)

    assert report["total_income"] == 60250.0


def test_total_expense():

    summary = FinancialSummary()

    report = summary.generate(insights)

    assert report["total_expense"] == 18795.0


def test_net_cash_flow():

    summary = FinancialSummary()

    report = summary.generate(insights)

    assert report["net_cash_flow"] == 41455.0
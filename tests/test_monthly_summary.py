from analyzer.monthly_summary import MonthlySummary


transactions = [
    {
        "date": "01/04/2026",
        "credit": 50000.0,
        "debit": None,
    },
    {
        "date": "03/04/2026",
        "credit": None,
        "debit": 5000.0,
    },
    {
        "date": "10/05/2026",
        "credit": 52000.0,
        "debit": None,
    },
    {
        "date": "15/05/2026",
        "credit": None,
        "debit": 12000.0,
    },
]

def test_month_count():

    summary = MonthlySummary()

    report = summary.generate(transactions)

    assert len(report) == 2


def test_april_income():

    summary = MonthlySummary()

    report = summary.generate(transactions)

    assert report["04/2026"]["income"] == 50000.0


def test_april_expense():

    summary = MonthlySummary()

    report = summary.generate(transactions)

    assert report["04/2026"]["expense"] == 5000.0


def test_may_income():

    summary = MonthlySummary()

    report = summary.generate(transactions)

    assert report["05/2026"]["income"] == 52000.0


def test_may_expense():

    summary = MonthlySummary()

    report = summary.generate(transactions)

    assert report["05/2026"]["expense"] == 12000.0
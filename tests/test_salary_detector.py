from analyzer.salary_detector import SalaryDetector


transactions = [
    {
        "description": "SALARY CREDIT ABC TECHNOLOGIES",
        "credit": 50000.0,
        "debit": None,
    },
    {
        "description": "UPI PAYMENT",
        "credit": None,
        "debit": 500.0,
    },
    {
        "description": "NEFT SALARY",
        "credit": 25000.0,
        "debit": None,
    },
]


def test_salary_total():

    detector = SalaryDetector()

    result = detector.detect(transactions)

    assert result["salary_total"] == 75000.0


def test_salary_count():

    detector = SalaryDetector()

    result = detector.detect(transactions)

    assert result["count"] == 2


def test_salary_transactions():

    detector = SalaryDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 2
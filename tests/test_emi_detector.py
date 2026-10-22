from analyzer.emi_detector import EMIDetector


transactions = [
    {
        "description": "HOME LOAN EMI",
        "debit": 15000.0,
    },
    {
        "description": "UPI PAYMENT",
        "debit": 500.0,
    },
    {
        "description": "CAR EMI",
        "debit": 8200.0,
    },
    {
        "description": "LOAN REPAYMENT",
        "debit": 12000.0,
    },
]


def test_emi_total():

    detector = EMIDetector()

    result = detector.detect(transactions)

    assert result["total"] == 35200.0


def test_emi_count():

    detector = EMIDetector()

    result = detector.detect(transactions)

    assert result["count"] == 3


def test_emi_transactions():

    detector = EMIDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 3
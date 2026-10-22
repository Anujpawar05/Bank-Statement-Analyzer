from analyzer.interest_detector import InterestDetector


transactions = [
    {
        "description": "SB INTEREST CREDIT",
        "credit": 145.20,
        "debit": None,
    },
    {
        "description": "UPI PAYMENT",
        "credit": None,
        "debit": 500.00,
    },
    {
        "description": "INTEREST PAID",
        "credit": None,
        "debit": 80.00,
    },
]


def test_interest_credit():

    detector = InterestDetector()

    result = detector.detect(transactions)

    assert result["interest_credit"] == 145.20


def test_interest_debit():

    detector = InterestDetector()

    result = detector.detect(transactions)

    assert result["interest_debit"] == 80.00


def test_interest_count():

    detector = InterestDetector()

    result = detector.detect(transactions)

    assert result["count"] == 2
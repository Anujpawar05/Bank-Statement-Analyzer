from analyzer.recurring_detector import RecurringDetector


transactions = [
    {
        "merchant": "NETFLIX",
        "debit": 649.0,
        "credit": None,
    },
    {
        "merchant": "NETFLIX",
        "debit": 649.0,
        "credit": None,
    },
    {
        "merchant": "SPOTIFY",
        "debit": 119.0,
        "credit": None,
    },
    {
        "merchant": "NETFLIX",
        "debit": 649.0,
        "credit": None,
    },
]


def test_recurring_count():

    detector = RecurringDetector()

    result = detector.detect(transactions)

    assert result["count"] == 1


def test_recurring_total():

    detector = RecurringDetector()

    result = detector.detect(transactions)

    assert result["total"] == 1947.0


def test_recurring_merchant():

    detector = RecurringDetector()

    result = detector.detect(transactions)

    assert "NETFLIX" in result["merchants"]


def test_recurring_frequency():

    detector = RecurringDetector()

    result = detector.detect(transactions)

    assert result["merchants"]["NETFLIX"]["count"] == 3
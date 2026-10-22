from analyzer.transfer_detector import TransferDetector


transactions = [
    {
        "description": "UPI/DR/ABC",
        "debit": 500.0,
    },
    {
        "description": "NEFT CREDIT",
        "credit": 2000.0,
    },
    {
        "description": "RTGS PAYMENT",
        "debit": 15000.0,
    },
    {
        "description": "ATM CASH",
        "debit": 500.0,
    },
]


def test_transfer_total():

    detector = TransferDetector()

    result = detector.detect(transactions)

    assert result["total"] == 17500.0


def test_transfer_count():

    detector = TransferDetector()

    result = detector.detect(transactions)

    assert result["count"] == 3


def test_transfer_transactions():

    detector = TransferDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 3
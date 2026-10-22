from analyzer.cash_deposit_detector import CashDepositDetector


transactions = [
    {
        "description": "CASH DEPOSIT",
        "credit": 10000.0,
    },
    {
        "description": "CSH DEP (CDM)",
        "credit": 2500.0,
    },
    {
        "description": "UPI CREDIT",
        "credit": 800.0,
    },
    {
        "description": "CASH Deposited at GCC ATM",
        "credit": 5000.0,
    },
]


def test_cash_deposit_total():

    detector = CashDepositDetector()

    result = detector.detect(transactions)

    assert result["total"] == 17500.0


def test_cash_deposit_count():

    detector = CashDepositDetector()

    result = detector.detect(transactions)

    assert result["count"] == 3


def test_cash_deposit_transactions():

    detector = CashDepositDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 3
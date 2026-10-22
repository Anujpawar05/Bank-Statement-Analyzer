from analyzer.cash_withdrawal_detector import CashWithdrawalDetector


transactions = [
    {
        "description": "ATM CASH WITHDRAWAL",
        "debit": 5000.0,
    },
    {
        "description": "WDL TFR",
        "debit": 2000.0,
    },
    {
        "description": "UPI PAYMENT",
        "debit": 800.0,
    },
    {
        "description": "CASH WDL",
        "debit": 3000.0,
    },
]


def test_cash_withdrawal_total():

    detector = CashWithdrawalDetector()

    result = detector.detect(transactions)

    assert result["total"] == 10000.0


def test_cash_withdrawal_count():

    detector = CashWithdrawalDetector()

    result = detector.detect(transactions)

    assert result["count"] == 3


def test_cash_withdrawal_transactions():

    detector = CashWithdrawalDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 3
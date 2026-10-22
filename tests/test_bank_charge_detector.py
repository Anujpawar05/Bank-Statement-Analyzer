from analyzer.bank_charge_detector import BankChargeDetector


transactions = [
    {
        "description": "CDM CHARGE DR",
        "debit": 47.20,
    },
    {
        "description": "ATM CHARGE",
        "debit": 25.00,
    },
    {
        "description": "UPI PAYMENT",
        "debit": 500.00,
    },
    {
        "description": "SMS CHARGES",
        "debit": 15.00,
    },
]


def test_total_bank_charges():

    detector = BankChargeDetector()

    result = detector.detect(transactions)

    assert result["total_charges"] == 87.20


def test_charge_count():

    detector = BankChargeDetector()

    result = detector.detect(transactions)

    assert result["charge_count"] == 3


def test_detected_descriptions():

    detector = BankChargeDetector()

    result = detector.detect(transactions)

    assert len(result["transactions"]) == 3
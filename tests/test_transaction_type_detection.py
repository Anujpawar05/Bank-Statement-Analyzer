from parser.transaction_parser import TransactionParser


def test_detect_debit_transaction():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "UPI/DR/123456 "
        "500.00 "
        "1500.00"
    )

    tx = parser.parse(line, "debit")

    assert tx["debit"] == 500.00
    assert tx["credit"] is None


def test_detect_credit_transaction():
    parser = TransactionParser()

    line = (
        "02/04/2025 "
        "UPI/CR/654321 "
        "1200.00 "
        "2700.00"
    )

    tx = parser.parse(line, "credit")

    assert tx["credit"] == 1200.00
    assert tx["debit"] is None


def test_detect_generic_transaction():
    parser = TransactionParser()

    line = (
        "03/04/2025 "
        "ATM Withdrawal "
        "800.00 "
        "1900.00"
    )

    tx = parser.parse(line)

    assert tx["amount"] == 800.00
    assert tx["balance"] == 1900.00
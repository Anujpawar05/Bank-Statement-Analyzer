from parser.transaction_parser import TransactionParser


def test_auto_detect_debit():
    parser = TransactionParser()

    line = "01/04/2025 UPI/DR/123456 500.00 1500.00"

    tx = parser.parse(line)

    assert tx["debit"] == 500.00
    assert tx["credit"] is None


def test_auto_detect_credit():
    parser = TransactionParser()

    line = "02/04/2025 UPI/CR/654321 1200.00 2700.00"

    tx = parser.parse(line)

    assert tx["credit"] == 1200.00
    assert tx["debit"] is None


def test_unknown_transaction_type():
    parser = TransactionParser()

    line = "03/04/2025 SOME TEXT 250.00 450.00"

    tx = parser.parse(line)

    assert tx["amount"] == 250.00
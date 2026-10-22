from parser.transaction_parser import TransactionParser


def test_parse_debit_transaction():
    parser = TransactionParser()

    line = "01/04/26 ATM Withdrawal 1000.00 14000.00"

    transaction = parser.parse_debit_line(line)

    assert transaction["debit"] == 1000.00
    assert transaction["credit"] is None
    assert transaction["balance"] == 14000.00


def test_parse_credit_transaction():
    parser = TransactionParser()

    line = "01/04/26 Salary Credit 45000.00 59000.00"

    transaction = parser.parse_credit_line(line)

    assert transaction["credit"] == 45000.00
    assert transaction["debit"] is None
    assert transaction["balance"] == 59000.00
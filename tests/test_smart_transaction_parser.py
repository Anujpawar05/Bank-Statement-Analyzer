from parser.transaction_parser import TransactionParser


def test_smart_parser_detects_debit():

    parser = TransactionParser()

    line = "01/04/26 ATM Withdrawal 1000.00 14000.00"

    transaction = parser.parse(line, transaction_type="debit")

    assert transaction["debit"] == 1000.0
    assert transaction["credit"] is None


def test_smart_parser_detects_credit():

    parser = TransactionParser()

    line = "01/04/26 Salary Credit 45000.00 59000.00"

    transaction = parser.parse(line, transaction_type="credit")

    assert transaction["credit"] == 45000.0
    assert transaction["debit"] is None
from parser.transaction_parser import TransactionParser


sample_line = "01/04/26 ATM Withdrawal 1000.00 14000.00"


def test_parse_transaction_fields():
    parser = TransactionParser()

    transaction = parser.parse_line(sample_line)

    assert transaction["date"] == "01/04/26"
    assert transaction["description"] == "ATM Withdrawal"
    assert transaction["amount"] == 1000.00
    assert transaction["balance"] == 14000.00
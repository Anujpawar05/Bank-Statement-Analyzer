from parser.transaction_parser import TransactionParser


def test_parser_extracts_merchant():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "UPI/DR/ZOMATO ORDER "
        "500.00 "
        "1500.00"
    )

    tx = parser.parse(line)

    assert tx["merchant"] == "Zomato"


def test_parser_unknown_merchant():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "RANDOM STORE "
        "200.00 "
        "1000.00"
    )

    tx = parser.parse(line)

    assert tx["merchant"] == "Unknown"
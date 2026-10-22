from parser.transaction_parser import TransactionParser


def test_parser_assigns_food_category():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "ZOMATO ORDER "
        "500.00 "
        "1500.00"
    )

    tx = parser.parse(line)

    assert tx["category"] == "Food"


def test_parser_assigns_cash_deposit():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "CSH DEP (CDM) "
        "2000.00 "
        "5000.00"
    )

    tx = parser.parse(line)

    assert tx["category"] == "Cash Deposit"
from parser.transaction_parser import TransactionParser


def test_parse_basic_transaction():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "UPI/DR/Zomato "
        "228.06 "
        "843.30"
    )

    tx = parser.parse(line)

    assert tx["date"] == "01/04/2025"
    assert tx["amount"] == 228.06
    assert tx["balance"] == 843.30


def test_parse_amounts_with_commas():
    parser = TransactionParser()

    line = (
        "14/04/2025 "
        "Cash Deposit "
        "18,400.00 "
        "21,071.30"
    )

    tx = parser.parse(line)

    assert tx["amount"] == 18400.00
    assert tx["balance"] == 21071.30


def test_description_contains_spaces():
    parser = TransactionParser()

    line = (
        "20/04/2025 "
        "UPI DR JOHN DOE PAYMENT "
        "500.00 "
        "2500.00"
    )

    tx = parser.parse(line)

    assert tx["description"] == "UPI DR JOHN DOE PAYMENT"

def test_parse_negative_amount():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "ATM Withdrawal "
        "(500.00) "
        "1500.00"
    )

    tx = parser.parse(line)

    assert tx["amount"] == -500.00

def test_parse_zero_amount():
    parser = TransactionParser()

    line = (
        "01/04/2025 "
        "Interest "
        "0.00 "
        "1500.00"
    )

    tx = parser.parse(line)

    assert tx["amount"] == 0.0
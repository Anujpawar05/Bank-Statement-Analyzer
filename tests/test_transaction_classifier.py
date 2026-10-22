from parser.transaction_classifier import TransactionClassifier


def test_food():
    classifier = TransactionClassifier()

    assert (
        classifier.classify(
            "UPI/DR/ZOMATO ORDER"
        )
        == "Food"
    )


def test_cash_deposit():
    classifier = TransactionClassifier()

    assert (
        classifier.classify(
            "CSH DEP (CDM)"
        )
        == "Cash Deposit"
    )


def test_cash_withdrawal():
    classifier = TransactionClassifier()

    assert (
        classifier.classify(
            "ATM WDL"
        )
        == "Cash Withdrawal"
    )


def test_travel():
    classifier = TransactionClassifier()

    assert (
        classifier.classify(
            "CONFIRM TICKET"
        )
        == "Travel"
    )


def test_unknown():
    classifier = TransactionClassifier()

    assert (
        classifier.classify(
            "SOME RANDOM PAYMENT"
        )
        == "Other"
    )
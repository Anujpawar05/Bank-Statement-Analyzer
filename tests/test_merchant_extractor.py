from parser.merchant_extractor import MerchantExtractor


def test_zomato():
    extractor = MerchantExtractor()

    assert (
        extractor.extract("UPI/DR/ZOMATO ORDER")
        == "Zomato"
    )


def test_dominos():
    extractor = MerchantExtractor()

    assert (
        extractor.extract("DOMINOS PAYMENT")
        == "Domino's"
    )


def test_confirm():
    extractor = MerchantExtractor()

    assert (
        extractor.extract("CONFIRM TICKET")
        == "ConfirmTkt"
    )


def test_unknown():
    extractor = MerchantExtractor()

    assert (
        extractor.extract("ABC XYZ")
        == "Unknown"
    )
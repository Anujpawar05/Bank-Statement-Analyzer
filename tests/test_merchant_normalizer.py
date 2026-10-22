from parser.merchant_normalizer import MerchantNormalizer


normalizer = MerchantNormalizer()


def test_normalize_amazon():

    assert normalizer.normalize("AMAZON PAY INDIA") == "Amazon"

    assert normalizer.normalize("AMAZON SELLER SERVICES") == "Amazon"

    assert normalizer.normalize("amazon.in") == "Amazon"


def test_normalize_flipkart():

    assert normalizer.normalize("FLIPKART INTERNET") == "Flipkart"

    assert normalizer.normalize("FKART") == "Flipkart"


def test_normalize_swiggy():

    assert normalizer.normalize("SWIGGY") == "Swiggy"

    assert normalizer.normalize("SWIGGY INSTAMART") == "Swiggy"


def test_normalize_zomato():

    assert normalizer.normalize("ZOMATO") == "Zomato"

    assert normalizer.normalize("ZOMATO LIMITED") == "Zomato"


def test_normalize_google():

    assert normalizer.normalize("GOOGLE PLAY") == "Google"


def test_normalize_phonepe():

    assert normalizer.normalize("PHONEPE") == "PhonePe"


def test_normalize_paytm():

    assert normalizer.normalize("PAYTM") == "Paytm"


def test_normalize_razorpay():

    assert normalizer.normalize("RAZORPAY") == "Razorpay"


def test_normalize_sbi():

    assert normalizer.normalize("STATE BANK OF INDIA") == "SBI"

    assert normalizer.normalize("SBI CARD") == "SBI"


def test_unknown_merchant():

    assert normalizer.normalize("MY LOCAL SHOP") == "My Local Shop"


def test_empty_merchant():

    assert normalizer.normalize("") == "Unknown"

    assert normalizer.normalize(None) == "Unknown"
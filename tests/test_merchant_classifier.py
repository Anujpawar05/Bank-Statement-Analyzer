from parser.merchant_classifier import MerchantClassifier


classifier = MerchantClassifier()


def test_ecommerce():

    assert classifier.classify("Amazon") == "E-commerce"
    assert classifier.classify("Flipkart") == "E-commerce"


def test_food_delivery():

    assert classifier.classify("Swiggy") == "Food Delivery"
    assert classifier.classify("Zomato") == "Food Delivery"


def test_ride_sharing():

    assert classifier.classify("Uber") == "Ride Sharing"
    assert classifier.classify("Ola") == "Ride Sharing"


def test_entertainment():

    assert classifier.classify("Netflix") == "Entertainment"
    assert classifier.classify("Spotify") == "Entertainment"


def test_digital_services():

    assert classifier.classify("Google") == "Digital Services"


def test_fintech():

    assert classifier.classify("PhonePe") == "FinTech"
    assert classifier.classify("Paytm") == "FinTech"
    assert classifier.classify("Razorpay") == "FinTech"


def test_banking():

    assert classifier.classify("SBI") == "Banking"


def test_unknown():

    assert classifier.classify("My Local Shop") == "Other"


def test_empty():

    assert classifier.classify("") == "Unknown"
    assert classifier.classify(None) == "Unknown"
    
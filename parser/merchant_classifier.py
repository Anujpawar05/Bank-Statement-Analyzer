class MerchantClassifier:
    """
    Classify merchants into business categories.
    """

    MERCHANT_TYPES = {
        "Amazon": "E-commerce",
        "Flipkart": "E-commerce",

        "Swiggy": "Food Delivery",
        "Zomato": "Food Delivery",

        "Uber": "Ride Sharing",
        "Ola": "Ride Sharing",

        "Netflix": "Entertainment",
        "Spotify": "Entertainment",

        "Google": "Digital Services",

        "PhonePe": "FinTech",
        "Paytm": "FinTech",
        "Razorpay": "FinTech",

        "SBI": "Banking",
    }

    def classify(self, merchant: str) -> str:

        if not merchant:
            return "Unknown"

        return self.MERCHANT_TYPES.get(
            merchant,
            "Other"
        )
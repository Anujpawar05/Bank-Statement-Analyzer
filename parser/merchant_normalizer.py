import re


class MerchantNormalizer:
    """
    Normalize extracted merchant names into a canonical form.
    """

    MERCHANT_PATTERNS = {
        "Amazon": [
            r"AMAZON",
            r"AMAZON PAY",
            r"AMAZONPAY",
            r"AMAZON SELLER",
            r"AMAZON\.IN",
        ],

        "Flipkart": [
            r"FLIPKART",
            r"FKART",
            r"FLIPKART INTERNET",
        ],

        "Swiggy": [
            r"SWIGGY",
            r"SWIGGY INSTAMART",
            r"SWIGGY LIMITED",
        ],

        "Zomato": [
            r"ZOMATO",
            r"ZOMATO LIMITED",
        ],

        "Uber": [
            r"UBER",
            r"UBER INDIA",
        ],

        "Ola": [
            r"\bOLA\b",
            r"OLA CABS",
        ],

        "Netflix": [
            r"NETFLIX",
        ],

        "Spotify": [
            r"SPOTIFY",
        ],

        "Google": [
            r"GOOGLE",
            r"GOOGLE PLAY",
        ],

        "PhonePe": [
            r"PHONEPE",
        ],

        "Paytm": [
            r"PAYTM",
        ],

        "Razorpay": [
            r"RAZORPAY",
        ],

        "SBI": [
            r"STATE BANK",
            r"\bSBI\b",
        ],
    }

    def normalize(self, merchant: str) -> str:

        if not merchant:
            return "Unknown"

        merchant = merchant.strip()

        for canonical, patterns in self.MERCHANT_PATTERNS.items():

            for pattern in patterns:

                if re.search(pattern, merchant, re.IGNORECASE):
                    return canonical

        return merchant.title()
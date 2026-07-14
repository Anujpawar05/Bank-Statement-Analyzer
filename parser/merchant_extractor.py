class MerchantExtractor:
    """
    Extract merchant names from transaction descriptions.
    """

    def __init__(self):
        self.merchants = {
            "ZOMATO": "Zomato",
            "SWIGGY": "Swiggy",
            "DOMINOS": "Domino's",
            "AMAZON": "Amazon",
            "FLIPKART": "Flipkart",
            "MYNTRA": "Myntra",
            "UBER": "Uber",
            "OLA": "Ola",
            "CONFIRM": "ConfirmTkt",
            "IRCTC": "IRCTC",
            "PAYTM": "Paytm",
            "PHONEPE": "PhonePe",
            "GPAY": "Google Pay",
        }

    def extract(self, description: str) -> str:
        """
        Return merchant name if found.
        """

        text = description.upper()

        for keyword, merchant in self.merchants.items():
            if keyword in text:
                return merchant

        return "Unknown"
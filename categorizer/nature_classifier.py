import re


class NatureClassifier:
    """
    Classifies the nature of a transaction into:
    - 'Cash'
    - 'Online'
    - 'Card'
    """

    CARD_KEYWORDS = [
        "DEBIT CARD",
        "CREDIT CARD",
        "VISA",
        "MASTERCARD",
        "RUPAY",
        "E-COMM",
        "ECOM",
        "CARD WDL",
        "CARD PURCHASE",
        "SWIPE",
        "POS TXN",
    ]

    ONLINE_PREFIXES = [
        "UPI/",
        "UP1/",
        "UPV/",
        "OPI/",
        "OP1/",
        "UPIDR",
        "UPIICR",
        "UPICR",
        "/DR/",
        "/CR/",
    ]

    ONLINE_KEYWORDS = [
        "NEFT",
        "RTGS",
        "IMPS",
        "INB",
        "NET BANKING",
        "NETBANKING",
        "TRANSFER",
        "TFR",
        "WDL TFR",
        "DEP TFR",
        "GPAY",
        "GOOGLE PAY",
        "PHONEPE",
        "PAYTM",
        "AIRP",
        "BILLDESK",
        "RAZORPAY",
        "PAYU",
        "MBK",
        "MOBILE BANKING",
        "NACH",
        "ECS",
    ]

    CASH_KEYWORDS = [
        "CSH",
        "CASH",
        "CDM",
        "ATM WDL",
        "ATM-WDL",
        "ATM CASH",
        "SELF CHEQUE",
        "CASH DEP",
        "CASH WITHDRAWAL",
        "VAULT",
    ]

    @classmethod
    def classify(cls, description: str) -> str:
        """
        Classifies transaction description into Cash, Online, or Card.
        """
        if not description:
            return "Online"

        desc = description.upper().strip()

        # 1. Explicit Card indicators
        if any(keyword in desc for keyword in cls.CARD_KEYWORDS):
            return "Card"

        # Check for standalone POS keyword, avoiding false positives like 'IPOS/' in UPI handles
        if re.search(r"\bPOS\b", desc) and "IPOS/" not in desc:
            return "Card"

        # 2. Explicit Online prefixes (UPI, etc. take precedence over incidental cash remarks)
        if any(prefix in desc for prefix in cls.ONLINE_PREFIXES):
            return "Online"

        # 3. Cash keywords
        if any(keyword in desc for keyword in cls.CASH_KEYWORDS):
            return "Cash"

        # 4. General Online keywords
        if any(keyword in desc for keyword in cls.ONLINE_KEYWORDS):
            return "Online"

        # Fallback default for banking transactions
        return "Online"

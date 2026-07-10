from parser.bank_parsers.sbi_parser import SBIParser


class ParserFactory:
    """
    Returns the appropriate parser for the detected bank.
    """

    def get_parser(self, bank_name: str):

        bank_name = bank_name.strip().upper()

        if bank_name in (
            "SBI",
            "STATE BANK OF INDIA",
        ):
            return SBIParser()

        return None
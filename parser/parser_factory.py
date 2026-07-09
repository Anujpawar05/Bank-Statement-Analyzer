from parser.bank_parsers.sbi_parser import SBIParser


class ParserFactory:
    """
    Factory responsible for returning
    the correct parser for a bank.
    """

    def get_parser(self, bank_name: str):
        """
        Return the correct parser based
        on the detected bank.

        Parameters
        ----------
        bank_name : str

        Returns
        -------
        BaseParser | None
        """

        if bank_name == "STATE BANK OF INDIA":
            return SBIParser()

        return None
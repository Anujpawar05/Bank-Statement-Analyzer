from parser.bank_parsers.base_parser import BaseParser


class SBIParser(BaseParser):
    """
    Parser for SBI bank statements.
    """

    def parse(self, text: str):
        """
        Parse SBI statement.

        Parameters
        ----------
        text : str

        Returns
        -------
        list
        """
        return []
from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Base class for all bank parsers.
    Every bank parser must inherit from this class.
    """

    @abstractmethod
    def parse(self, text: str):
        """
        Parse a bank statement.

        Parameters
        ----------
        text : str
            Complete statement text.

        Returns
        -------
        list
            Parsed transactions.
        """
        pass
    
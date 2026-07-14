from preprocessor.layout_reconstructor import LayoutReconstructor
from preprocessor.transaction_merger import TransactionMerger


class PreprocessingPipeline:
    """
    Applies preprocessing steps before transaction parsing.
    """

    def __init__(self):
        self.layout = LayoutReconstructor()
        self.merger = TransactionMerger()

    def process(self, text: str) -> list[str]:
        """
        Returns cleaned transaction lines.
        """

        lines = self.layout.reconstruct(text)

        lines = self.merger.merge(lines)

        return lines
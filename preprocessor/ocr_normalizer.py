import re


class OCRNormalizer:
    """
    Cleans OCR text before bank parsing.

    This class should NEVER infer financial information.
    It only repairs common OCR formatting issues.
    """

    def normalize(self, text: str) -> str:

        text = self._normalize_line_endings(text)
        text = self._remove_bullets(text)
        text = self._fix_split_decimals(text)
        text = self._fix_split_commas(text)
        text = self._remove_duplicate_spaces(text)

        return text

    def _normalize_line_endings(self, text):

        return text.replace("\r\n", "\n")

    def _remove_bullets(self, text):

        text = text.replace("•", "")
        text = text.replace("▪", "")
        text = text.replace("◦", "")

        return text

    def _fix_split_decimals(self, text):
        """
        5,002. 10
        ->
        5,002.10
        """

        return re.sub(
            r"(\d)\.\s+(\d{2})",
            r"\1.\2",
            text,
        )

    def _fix_split_commas(self, text):
        """
        1 000.00
        ->
        1000.00
        """

        return re.sub(
            r"(\d)\s+(\d{3}\.\d{2})",
            r"\1\2",
            text,
        )

    def _remove_duplicate_spaces(self, text):

        return re.sub(
            r"[ ]{2,}",
            " ",
            text,
        )
import re


class TransactionMerger:
    """
    Merge OCR transaction fragments into complete transaction lines.
    """

    DATE_PATTERN = re.compile(r"^\d{2}[/-]\d{2}[/-]\d{2,4}")

    def merge(self, lines: list[str]) -> list[str]:
        """
        Merge fragmented OCR lines into complete transactions.
        """

        merged = []
        current = ""

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if self.DATE_PATTERN.match(line):

                if current:
                    merged.append(current.strip())

                current = line

            else:
                current += " " + line

        if current:
            merged.append(current.strip())

        return merged
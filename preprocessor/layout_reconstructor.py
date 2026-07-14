import re


class LayoutReconstructor:
    """
    Reconstruct OCR text so that each transaction occupies one line.
    """

    DATE_PATTERN = re.compile(r"\d{2}/\d{2}/\d{4}")

    def reconstruct(self, text: str) -> list[str]:
        """
        Returns reconstructed transaction lines.
        """

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        reconstructed = []

        current = ""

        for line in lines:

            if self.DATE_PATTERN.match(line):

                if current:
                    reconstructed.append(current.strip())

                current = line

            else:

                current += " " + line

        if current:
            reconstructed.append(current.strip())

        return reconstructed
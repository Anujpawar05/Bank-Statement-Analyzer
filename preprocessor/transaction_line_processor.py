import re


class TransactionLineProcessor:

    DATE_PATTERN = re.compile(
        r"\d{2}/\d{2}/\d{4}"
    )

    MONEY_PATTERN = re.compile(
        r"\d[\d,]*\.\d{2}"
    )

    def process(self, line: str):

        dates = self.DATE_PATTERN.findall(line)

        amounts = self.MONEY_PATTERN.findall(line)

        description = line

        for d in dates:
            description = description.replace(d, "")

        for a in amounts:
            description = description.replace(a, "")

        description = " ".join(description.split())

        return {
            "dates": dates,
            "amounts": amounts,
            "description": description
        }
    
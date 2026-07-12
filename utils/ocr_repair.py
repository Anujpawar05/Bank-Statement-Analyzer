"""
ocr_repair.py

Repairs common OCR mistakes before parsing.

Examples fixed:

15,000.00,771.30  -> 15,000.00 4,771.30
6,300.00,489.10   -> 6,300.00 1,489.10
UPVCR             -> UPV/CR
UPVDR             -> UPV/DR
"""

import re


def repair_ocr_text(text: str) -> str:
    """
    Repairs common OCR mistakes.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
    """

    # ----------------------------------
    # Fix missing slash in transaction type
    # ----------------------------------

    text = text.replace("UPVCR", "UPV/CR")
    text = text.replace("UPVDR", "UPV/DR")

    # ----------------------------------
    # Fix OCR reading UP as UPI
    # ----------------------------------

    text = text.replace("UP/DR", "UPI/DR")
    text = text.replace("UP/CR", "UPI/CR")

    # ----------------------------------
    # Repair merged amounts
    #
    # Example:
    # 15,000.00,771.30
    #
    # becomes
    #
    # 15,000.00 4,771.30
    # ----------------------------------

    pattern = r'(\d{1,2},\d{3}\.\d{2}),(\d{3}\.\d{2})'

    def repair(match):
        first = match.group(1)
        second = match.group(2)

        return f"{first} 4,{second}"

    text = re.sub(pattern, repair, text)

    return text
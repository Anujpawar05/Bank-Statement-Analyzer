from parser.metadata_extractor import MetadataExtractor


sample_text = """
STATE BANK OF INDIA

Account Name : JOHN DOE

Account Number : 12345678901

Branch : YAVATMAL

IFSC : SBIN0001234

Statement Period : 01/04/2026 to 30/04/2026
"""


def test_extract_bank_name():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["bank_name"] == "STATE BANK OF INDIA"


def test_extract_account_holder():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["account_holder"] == "JOHN DOE"


def test_extract_account_number():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["account_number"] == "12345678901"


def test_extract_ifsc():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["ifsc"] == "SBIN0001234"


def test_extract_branch():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["branch"] == "YAVATMAL"


def test_extract_statement_period():
    extractor = MetadataExtractor()

    metadata = extractor.extract(sample_text)

    assert metadata["statement_period"] == "01/04/2026 to 30/04/2026"
from extractor.text_extractor import TextExtractor


def test_text_extractor_returns_string(sample_pdf):
    extractor = TextExtractor()

    text = extractor.extract(sample_pdf)

    assert isinstance(text, str)

def test_text_extractor_returns_string_for_any_pdf(sample_pdf):
    """
    The extractor should always return a string,
    even if no embedded text exists.
    """

    extractor = TextExtractor()

    text = extractor.extract(sample_pdf)

    assert isinstance(text, str)
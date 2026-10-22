"""
Tests for DocumentExtractor.
"""

from extractor.document_extractor import DocumentExtractor


def test_document_extractor_returns_string(sample_pdf):
    """
    DocumentExtractor should always return a string.
    """

    extractor = DocumentExtractor()

    text = extractor.extract(sample_pdf)

    assert isinstance(text, str)


def test_document_extractor_handles_image_pdf(sample_pdf):
    extractor = DocumentExtractor()

    text = extractor.extract(sample_pdf)

    assert isinstance(text, str)
    assert len(text) > 0
    assert "State Bank" in text
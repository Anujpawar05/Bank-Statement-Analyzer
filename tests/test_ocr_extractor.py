from extractor.image_converter import ImageConverter
from extractor.ocr_extractor import OCRExtractor


def test_ocr_returns_string(sample_pdf):
    converter = ImageConverter()

    images = converter.convert(sample_pdf)

    extractor = OCRExtractor()

    text = extractor.extract(images)

    assert isinstance(text, str)


def test_ocr_not_empty(sample_pdf):
    converter = ImageConverter()

    images = converter.convert(sample_pdf)

    extractor = OCRExtractor()

    text = extractor.extract(images)

    assert len(text.strip()) > 0
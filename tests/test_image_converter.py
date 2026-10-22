from extractor.image_converter import ImageConverter


def test_image_converter_returns_list(sample_pdf):
    converter = ImageConverter()

    images = converter.convert(sample_pdf)

    assert isinstance(images, list)


def test_image_converter_creates_images(sample_pdf):
    converter = ImageConverter()

    images = converter.convert(sample_pdf)

    assert len(images) == sample_pdf.page_count


def test_generated_images_exist(sample_pdf):
    converter = ImageConverter()

    images = converter.convert(sample_pdf)

    for image in images:
        assert image.exists()
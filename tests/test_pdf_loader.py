def test_pdf_opens(sample_pdf):
    """
    Verify that the sample PDF opens successfully.
    """

    assert sample_pdf is not None


def test_pdf_has_pages(sample_pdf):
    """
    Verify that the PDF contains at least one page.
    """

    assert sample_pdf.page_count > 0
from preprocessor.preprocessing_pipeline import PreprocessingPipeline


def test_pipeline_returns_list():
    pipeline = PreprocessingPipeline()

    text = (
        "01/04/2025\n"
        "UPI/DR/12345\n"
        "Amazon\n"
        "500.00\n"
        "1500.00"
    )

    result = pipeline.process(text)

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0].startswith("01/04/2025")
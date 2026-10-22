from pipeline.processing_pipeline import ProcessingPipeline


def test_pipeline_creation():

    pipeline = ProcessingPipeline()

    assert pipeline.document_extractor is not None
    assert pipeline.bank_detector is not None
    assert pipeline.metadata_extractor is not None
    assert pipeline.parser_factory is not None
    assert pipeline.analysis_engine is not None
    assert pipeline.categorizer is not None
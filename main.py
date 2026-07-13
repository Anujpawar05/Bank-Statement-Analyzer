import traceback
from pathlib import Path
from parser.repair_engine import RepairEngine
from pipeline.processing_pipeline import ProcessingPipeline


def main():
    print("=" * 60)
    print("Bank Statement Analyzer")
    print("=" * 60)

    pdf_path = input("Enter PDF path: ").strip()

    if not Path(pdf_path).exists():
        print("\n❌ PDF not found.")
        return

    try:
        print("\n🚀 Starting processing pipeline...\n")

        pipeline = ProcessingPipeline()

        result = pipeline.process(pdf_path)

        print("\n" + "=" * 60)
        print("OCR TEXT")
        print("=" * 60)

        print(result["text"])

        print("\n" + "=" * 60)
        print("PROCESSING COMPLETE")
        print("=" * 60)

        print(f"\n🏦 Bank: {result['bank_name']}")

        print("\n📋 Metadata")

        for key, value in result["metadata"].items():
            print(f"{key}: {value}")

        print("\n📊 Analysis")

        for key, value in result["analysis"].items():
            print(f"{key}: {value}")

        print(f"\n💳 Transactions Parsed: {len(result['transactions'])}")

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    main()
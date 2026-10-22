# Bank Statement Analyzer 📊

An intelligent, full-stack bank statement analysis tool that parses PDF statements, categorizes transactions, verifies financial integrity through automated debit/credit balancing, and exports structured Excel reports.

---

## 🚀 Key Features

- **Multi-Bank Statement Parsing**: Intelligent layout reconstruction and entity extraction for standard and scanned bank statements.
- **OCR Engine Support**: Seamless OCR processing via PaddleOCR for scanned or image-based statement documents.
- **Password-Protected PDFs**: Built-in support for encrypted PDF statements with on-demand authentication.
- **Transaction Classification**: Automated categorization of transactions by nature (UPI, Online Transfer, Card, Cash Deposit/Withdrawal, Charges).
- **Balance Audit & Reconciliation**: Mathematical verification of opening balances, debits, credits, and closing balances with audit reporting.
- **Excel Report Generator**: Automatically generates styled `.xlsx` reports with reconciliation summaries and formatted financial metrics.
- **Modern Web Interface**: Intuitive web UI powered by FastAPI and modern frontend styling.
- **CLI Pipeline**: Direct command-line interface for batch or automated processing.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, FastAPI, Uvicorn
- **PDF & OCR Processing**: PyMuPDF (`fitz`), PaddleOCR, OpenCV
- **Excel & Data**: OpenPyXL, Pandas
- **Frontend**: HTML5, Vanilla CSS, JavaScript (served via Jinja2 templates)

---

## 📁 Project Structure

```text
Bank-Statement-Analyzer/
├── analyzer/         # Financial summary, audit engines, and detector rules
├── api/              # FastAPI application, routes, and dependency injection
├── categorizer/      # Transaction classification and nature categorizers
├── config.py         # Global configuration settings
├── exporter/         # Excel workbook generator and formatters
├── extractor/        # PDF loaders, OCR engines, and text extraction
├── frontend/         # Web templates and static assets (CSS, JS)
├── main.py           # CLI entry point
├── models/           # Data models and schemas
├── parser/           # Bank-specific parsers and repair engine
├── pipeline/         # End-to-end processing pipeline
├── preprocessor/     # Text normalizers and layout reconstructors
├── rules/            # Banking rules (GST, interest, charges, salary)
├── services/         # Orchestration services
├── tests/            # Test suite
└── utils/            # Amount reconstruction and OCR cleanup helpers
```

---

## ⚙️ Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Anujpawar05/Bank-Statement-Analyzer.git
   cd Bank-Statement-Analyzer
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Running the Application

### 1. Web Application (FastAPI)
Run the local development server:
```bash
python -m uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```
Open your browser and navigate to:
- **Web UI**: [http://127.0.0.1:8000/app](http://127.0.0.1:8000/app)
- **API Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 2. Command-Line Interface (CLI)
To run analysis directly on a statement file:
```bash
python main.py
```
When prompted, provide the path to your bank statement PDF.

---

## 🔒 Privacy & Security

- Statement files, customer data, and generated spreadsheets are strictly excluded from version control via `.gitignore`.
- Temporary image files generated during OCR processing are automatically managed.

---

## 📄 License

This project is licensed under the MIT License.

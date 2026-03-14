# AI DDR Generator - Building Inspection Report Analysis

A Python-based workflow that converts building inspection and thermal analysis reports into a structured Detailed Diagnostic Report (DDR) using Google's Gemini 2.5 Flash model.

## Project Overview

The AI DDR Generator automates the analysis of building inspection documentation. It extracts data from inspection and thermal reports, processes the information using an AI reasoning pipeline, and produces a structured diagnostic report suitable for property owners, engineers, or inspection teams.

This project demonstrates a practical Applied AI workflow involving document ingestion, data extraction, reasoning, and structured report generation.

Key capabilities include:

- Automated PDF text extraction
- Automated image extraction from reports
- AI-driven reasoning using Gemini 2.5 Flash
- Structured DDR generation with standardized sections
- Clean modular architecture
- Reusable pipeline for similar inspection reports

## Architecture

```
Input PDFs
 - Inspection Report
 - Thermal Report
        │
        ▼
PDF Extraction Layer
 - extract_pdf.py
 - extract_images.py
        │
        ▼
Extracted Data
 - Text Data
 - Image References
        │
        ▼
AI Analysis Layer
 - generate_ddr.py
 - Gemini 2.5 Flash API
        │
        ▼
Structured DDR Report
 1. Property Issue Summary
 2. Area-wise Observations
 3. Probable Root Cause
 4. Severity Assessment
 5. Recommended Actions
 6. Additional Notes
 7. Missing or Unclear Information
        │
        ▼
Output
 output/DDR_Report.md
```

## Quick Start

### Prerequisites

- Python 3.8 or newer
- macOS, Linux, or Windows
- Google Gemini API key

### Step 1: Create Virtual Environment

Navigate to the project directory and create a virtual environment.

```bash
cd ai_ddr_generator
python -m venv urbanvenv
```

Activate the virtual environment.

Mac/Linux:

```bash
source urbanvenv/bin/activate
```

Windows:

```bash
urbanvenv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

Copy the environment template file.

```bash
cp .env.example .env
```

Edit `.env` and insert your Gemini API key.

```
GEMINI_API_KEY=your_api_key_here
```

API keys can be created in Google AI Studio:

https://aistudio.google.com/app/apikey

### Step 4: Prepare Input Files

Place the inspection and thermal reports in the `input` folder.

```
input/
 ├── inspection_report.pdf
 └── thermal_report.pdf
```

### Step 5: Run the Workflow

Execute the main pipeline.

```bash
python main.py
```

The generated report will be saved in:

```
output/DDR_Report.md
```

## Project Structure

```
ai_ddr_generator/
│
├── input/
│   ├── inspection_report.pdf
│   └── thermal_report.pdf
│
├── images/
│
├── output/
│   └── DDR_Report.md
│
├── extract_pdf.py
├── extract_images.py
├── generate_ddr.py
├── main.py
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

## Module Overview

### extract_pdf.py

Handles text extraction from PDF documents.

Function:

```
extract_text(pdf_path)
```

Responsibilities:

- Load PDF using PyMuPDF
- Extract text from each page
- Return the combined document text

### extract_images.py

Handles image extraction from PDF files.

Function:

```
extract_images(pdf_path, output_folder)
```

Responsibilities:

- Locate embedded images inside the PDF
- Save images to the `images` folder
- Return a list of saved image file paths

### generate_ddr.py

Responsible for generating the DDR report using Gemini AI.

Function:

```
generate_ddr(inspection_text, thermal_text)
```

Responsibilities:

- Combine extracted inspection and thermal data
- Send structured prompt to Gemini 2.5 Flash
- Generate a structured diagnostic report
- Return the report text

### main.py

Orchestrates the entire pipeline.

Execution flow:

1. Extract inspection report text
2. Extract thermal report text
3. Extract images from both reports
4. Send extracted data to Gemini
5. Generate DDR report
6. Save report to the output directory

## DDR Report Structure

The generated DDR follows a fixed structure required by the assignment.

1. Property Issue Summary  
2. Area-wise Observations  
3. Probable Root Cause  
4. Severity Assessment  
5. Recommended Actions  
6. Additional Notes  
7. Missing or Unclear Information  

The report uses client-friendly language and avoids unnecessary technical jargon.

## Dependencies

| Package | Purpose |
|--------|--------|
| pymupdf | PDF text and image extraction |
| google-genai | Gemini API integration |
| python-dotenv | Environment variable management |

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Error Handling

The workflow includes handling for common issues:

Missing API key  
Missing input files  
API communication errors  
Output file writing issues  

All failures return clear error messages.

## Security Notes

Do not commit `.env` files containing API keys.  
Ensure `.env` is listed in `.gitignore`.

Inspection reports and generated DDR outputs may contain sensitive property information and should be handled accordingly.

## Performance

Typical runtime for a complete workflow:

Text extraction: 1–2 seconds  
Image extraction: 2–5 seconds  
AI analysis: 10–30 seconds  

Total runtime per report: approximately 15–40 seconds.

## Extending the System

This pipeline can be extended to support additional functionality.

Possible improvements:

- Additional inspection report formats
- OCR for scanned PDFs
- Vector database for inspection history
- Image anomaly detection
- Web interface for report generation

## Conclusion

This project demonstrates an Applied AI workflow that converts raw inspection documentation into a structured diagnostic report using document processing and AI reasoning.

The system is designed to generalize to similar inspection reports rather than only the provided sample inputs.
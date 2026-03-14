"""
extract_pdf.py

Module for extracting text content from PDF files using PyMuPDF (fitz).
This module handles PDF reading and text extraction.
"""

import fitz  # PyMuPDF


def extract_text(pdf_path):
    """
    Extract all text content from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file to extract text from.
    
    Returns:
        str: Extracted text from all pages of the PDF.
    
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        Exception: If PDF reading fails.
    
    Example:
        >>> text = extract_text("input/inspection_report.pdf")
        >>> print(f"Extracted {len(text)} characters from PDF")
    """
    try:
        # Open the PDF document
        pdf_document = fitz.open(pdf_path)
        
        extracted_text = ""
        
        # Iterate through all pages and extract text
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            page_text = page.get_text()
            extracted_text += f"\n--- Page {page_number + 1} ---\n"
            extracted_text += page_text
        
        # Close the document to free resources
        pdf_document.close()
        
        return extracted_text
    
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

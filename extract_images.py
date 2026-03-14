"""
extract_images.py

Module for extracting images from PDF files and saving them to disk.
Uses PyMuPDF (fitz) to access and extract embedded images.
"""

import os
import fitz  # PyMuPDF
from pathlib import Path


def extract_images(pdf_path, output_folder):
    """
    Extract all images from a PDF file and save them to a specified folder.
    
    Args:
        pdf_path (str): Path to the PDF file to extract images from.
        output_folder (str): Path to the folder where images will be saved.
    
    Returns:
        list: List of file paths to the extracted images.
    
    Raises:
        FileNotFoundError: If the PDF file does not exist.
        Exception: If image extraction fails.
    
    Example:
        >>> image_paths = extract_images("input/inspection_report.pdf", "images/")
        >>> print(f"Extracted {len(image_paths)} images")
    """
    try:
        # Ensure output folder exists
        Path(output_folder).mkdir(parents=True, exist_ok=True)
        
        # Open the PDF document
        pdf_document = fitz.open(pdf_path)
        
        extracted_images = []
        image_counter = 0
        
        # Iterate through all pages
        for page_number in range(len(pdf_document)):
            page = pdf_document[page_number]
            
            # Get list of images on the page
            image_list = page.get_images()
            
            # Extract each image
            for image_index, img in enumerate(image_list):
                try:
                    # Get the image reference
                    xref = img[0]
                    pix = fitz.Pixmap(pdf_document, xref)
                    
                    # Convert RGBA to RGB if necessary
                    if pix.n - pix.alpha < 4:
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    
                    # Generate filename
                    image_counter += 1
                    image_filename = f"page_{page_number + 1}_image_{image_index + 1}.png"
                    image_path = os.path.join(output_folder, image_filename)
                    
                    # Save the image
                    pix.save(image_path)
                    extracted_images.append(image_path)
                    
                except Exception as e:
                    print(f"Warning: Could not extract image on page {page_number + 1}: {str(e)}")
        
        # Close the document
        pdf_document.close()
        
        return extracted_images
    
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error extracting images from PDF: {str(e)}")

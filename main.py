"""
main.py

Main orchestrator script for the AI DDR Generator workflow.
Executes the complete pipeline: PDF extraction → AI analysis → DDR generation.
"""

import os
import sys
from pathlib import Path

# Import our custom modules
from extract_pdf import extract_text
from extract_images import extract_images
from generate_ddr import generate_ddr, save_ddr_report


def main():
    """
    Execute the complete DDR generation pipeline.
    
    Pipeline steps:
    1. Extract text from inspection report PDF
    2. Extract text from thermal report PDF
    3. Extract images from both PDFs
    4. Generate DDR using Gemini AI
    5. Save DDR to output folder
    """
    
    # Define file paths
    inspection_pdf = "input/sample_report.pdf"
    thermal_pdf = "input/thermal_images.pdf"
    images_folder = "images"
    output_file = "output/DDR_Report.md"
    
    print("\n" + "="*60)
    
    try:
        # Step 1: Extract inspection report text
        if os.path.exists(inspection_pdf):
            print("Extracting inspection report text...")
            inspection_text = extract_text(inspection_pdf)
            print(f"Extracted {len(inspection_text)} characters from inspection report\n")
        else:
            print(f"Warning: {inspection_pdf} not found. Using placeholder text.\n")
            inspection_text = "[Inspection report not found - placeholder data]"
        
        # Step 2: Extract thermal report text
        if os.path.exists(thermal_pdf):
            print("Extracting thermal report text...")
            thermal_text = extract_text(thermal_pdf)
            print(f"Extracted {len(thermal_text)} characters from thermal report\n")
        else:
            print(f"Warning: {thermal_pdf} not found. Using placeholder text.\n")
            thermal_text = "[Thermal report not found - placeholder data]"
        
        # Step 3: Extract images from inspection report
        if os.path.exists(inspection_pdf):
            print("Extracting images from inspection report...")
            inspection_images = extract_images(inspection_pdf, images_folder)
            print(f"Extracted {len(inspection_images)} images from inspection report\n")
        else:
            inspection_images = []
        
        # Step 4: Extract images from thermal report
        if os.path.exists(thermal_pdf):
            print("Extracting images from thermal report...")
            thermal_images = extract_images(thermal_pdf, images_folder)
            print(f" Extracted {len(thermal_images)} images from thermal report\n")
        else:
            thermal_images = []
        
        # Step 5: Generate DDR using Gemini AI
        print("Generating DDR using Gemini 2.5 Flash AI...")
        ddr_report = generate_ddr(inspection_text, thermal_text)
        print("DDR generated successfully\n")
        
        # Step 6: Save DDR report
        print(f"Saving DDR report to {output_file}...")
        
        # Ensure output directory exists
        Path("output").mkdir(parents=True, exist_ok=True)
        
        # Save the report
        save_ddr_report(ddr_report, output_file)
        print(f"DDR report saved to output folder\n")
        
    except FileNotFoundError as e:
        print(f"\nFile Error: {str(e)}")
        print("Please ensure PDF files are in the input/ folder")
        sys.exit(1)
    
    except ValueError as e:
        print(f"\nConfiguration Error: {str(e)}")
        print("Please set up your .env file with GEMINI_API_KEY")
        sys.exit(1)
    
    except Exception as e:
        print(f"\nUnexpected Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

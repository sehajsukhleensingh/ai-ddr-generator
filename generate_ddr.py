"""
generate_ddr.py

Module for generating a Detailed Diagnostic Report (DDR) using Gemini 2.5 Flash API.
This module orchestrates AI-powered analysis of inspection and thermal reports.
"""

import os
from dotenv import load_dotenv
import google.genai


# Load environment variables from .env file
load_dotenv()


def generate_ddr(inspection_text, thermal_text):
    """
    Generate a structured Detailed Diagnostic Report (DDR) using Gemini 2.5 Flash.
    
    Args:
        inspection_text (str): Extracted text from the inspection report PDF.
        thermal_text (str): Extracted text from the thermal report PDF.
    
    Returns:
        str: Formatted DDR report with all required sections.
    
    Raises:
        ValueError: If GEMINI_API_KEY is not set in environment variables.
        Exception: If API call fails.
    
    Example:
        >>> ddr = generate_ddr(inspection_text, thermal_text)
        >>> print(ddr)
    """
    
    # Get API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )
    
    # Initialize Gemini client
    client = google.genai.Client(api_key=api_key)
    
    # Craft the prompt for DDR generation
    prompt = f"""
        You are a professional building diagnostics engineer preparing a
        Detailed Diagnostic Report (DDR) for a property inspection client.

        Your task is to analyze two sources of information:

        1. Visual Inspection Report
        2. Thermal Imaging Report

        Your objective is to convert the raw inspection data into a clear,
        client-friendly diagnostic report.

        IMPORTANT ANALYSIS INSTRUCTIONS

        1. Extract all relevant observations from both reports.
        2. Combine inspection observations and thermal evidence logically.
        3. Remove duplicate observations if the same issue appears multiple times.
        4. If inspection and thermal findings contradict each other, clearly mention the conflict.
        5. Do NOT invent facts that are not present in the input documents.
        6. If required information is missing, explicitly write "Not Available".
        7. Use simple language suitable for a property owner (avoid heavy technical jargon).
        8. The report should generalize to similar inspection reports, not only this example.

        INPUT DATA

        INSPECTION REPORT
        ----------------
        {inspection_text[:12000]}

        THERMAL REPORT
        --------------
        {thermal_text[:12000]}

        Generate the Detailed Diagnostic Report using the following structure.

        # Detailed Diagnostic Report

        ## 1. Property Issue Summary
        Provide a concise summary of the major structural, moisture, or leakage issues observed.

        ## 2. Area-wise Observations
        Organize findings by area such as Hall, Bedroom, Kitchen, Bathroom, External Wall, Terrace, etc.

        For each area include:
        - Visual Observation (from inspection report)
        - Thermal Evidence (if available)
        - Image Reference (if available)

        Only reference images if they are provided in the AVAILABLE IMAGE FILES list.
        Do not reference photo numbers from the report unless they exist as extracted image files.
        If no matching image exists, write: Image Not Available.

        ## 3. Probable Root Cause
        Explain the most likely technical cause of the observed issues by connecting inspection and thermal findings.

        ## 4. Severity Assessment
        Classify each major issue as:
        Low / Moderate / High

        Provide reasoning based on the evidence in the reports.

        ## 5. Recommended Actions
        Provide practical repair or maintenance recommendations to address the identified issues.

        ## 6. Additional Notes
        Include any helpful contextual information that may assist the property owner.

        ## 7. Missing or Unclear Information
        List any important data points that were not available in the documents.

        Ensure the final report is structured, concise, and readable for a non-technical client.
        """
    
    try:
        # Call Gemini 2.5 Flash API
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Extract the generated text
        ddr_report = response.text
        
        return ddr_report
    
    except Exception as e:
        raise Exception(f"Error generating DDR from Gemini API: {str(e)}")


def save_ddr_report(ddr_text, output_path):
    """
    Save the DDR report to a markdown file.
    
    Args:
        ddr_text (str): The DDR report text to save.
        output_path (str): Path where the report should be saved.
    
    Returns:
        bool: True if save was successful.
    
    Raises:
        Exception: If file write fails.
    
    Example:
        >>> save_ddr_report(ddr, "output/DDR_Report.md")
    """
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(ddr_text)
        return True
    except Exception as e:
        raise Exception(f"Error saving DDR report: {str(e)}")

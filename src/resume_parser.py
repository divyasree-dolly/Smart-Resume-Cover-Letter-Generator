"""
Resume parsing utilities for extracting text from PDF and DOCX files.
"""

import streamlit as st
import PyPDF2
from docx import Document
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    """Extract text from PDF file bytes"""
    try:
        pdf_reader = PyPDF2.PdfReader(BytesIO(file_bytes))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading PDF: {str(e)}")
        return None

def extract_text_from_docx(file_bytes):
    """Extract text from DOCX file bytes"""
    try:
        doc = Document(BytesIO(file_bytes))
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        st.error(f"Error reading DOCX: {str(e)}")
        return None

def extract_text_from_file(uploaded_file):
    """
    Extract text from uploaded file (PDF or DOCX)
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        str: Extracted text or None if extraction fails
    """
    if uploaded_file is None:
        return None
    
    file_bytes = uploaded_file.read()
    file_type = uploaded_file.type
    
    if file_type == "application/pdf" or uploaded_file.name.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_bytes)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" or uploaded_file.name.lower().endswith('.docx'):
        return extract_text_from_docx(file_bytes)
    else:
        st.error(f"Unsupported file type: {file_type}")
        return None

def clean_resume_text(text):
    """
    Clean and format resume text for better AI processing
    
    Args:
        text (str): Raw resume text
        
    Returns:
        str: Cleaned resume text
    """
    if not text:
        return ""
    
    # Remove extra whitespace and normalize line breaks
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    cleaned_text = '\n'.join(lines)
    
    # Remove excessive blank lines
    while '\n\n\n' in cleaned_text:
        cleaned_text = cleaned_text.replace('\n\n\n', '\n\n')
    
    return cleaned_text

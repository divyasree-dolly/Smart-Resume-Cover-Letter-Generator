"""
AI generation utilities using OpenAI's GPT models for cover letters and resume enhancement.
"""

import os
import streamlit as st
from openai import OpenAI

def get_openai_client():
    """Initialize and return OpenAI client"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("❌ OpenAI API key not found. Please set it in the sidebar.")
        return None
    
    try:
        # Initialize OpenAI client with just the API key
        client = OpenAI(api_key=api_key)
        return client
    except Exception as e:
        st.error(f"❌ Failed to initialize OpenAI client: {str(e)}")
        st.error("💡 Try updating the OpenAI package: pip install --upgrade openai")
        return None

def generate_cover_letter(resume_text, job_description):
    """
    Generate a tailored cover letter based on resume and job description.
    
    Args:
        resume_text (str): Extracted resume content
        job_description (str): Job posting description
        
    Returns:
        str: Generated cover letter or None if generation fails
    """
    client = get_openai_client()
    if not client:
        return None
    
    prompt = f"""
    Based on the resume and job description provided below, write a professional, compelling cover letter that:
    
    1. Highlights relevant experience and skills from the resume that match the job requirements
    2. Shows enthusiasm for the specific role and company
    3. Demonstrates understanding of the job requirements
    4. Is personalized and specific (not generic)
    5. Is professional yet engaging in tone
    6. Is approximately 3-4 paragraphs long
    
    RESUME:
    {resume_text}
    
    JOB DESCRIPTION:
    {job_description}
    
    Please write a cover letter that makes a strong case for why this candidate is perfect for this role. Start with "Dear Hiring Manager," and end with "Sincerely," followed by a placeholder for the candidate's name.
    """
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),  # Use gpt-4o-mini as fallback
            messages=[
                {"role": "system", "content": "You are an expert career coach and professional writer specializing in creating compelling cover letters that help candidates stand out."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=int(os.getenv("MAX_TOKENS", 800)),
            temperature=float(os.getenv("TEMPERATURE", 0.7))
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"❌ Error generating cover letter: {str(e)}")
        if "rate_limit" in str(e).lower():
            st.error("💡 Rate limit exceeded. Please wait a moment and try again.")
        elif "quota" in str(e).lower():
            st.error("💡 API quota exceeded. Please check your OpenAI billing.")
        return None

def enhance_resume_bullets(resume_text, job_description):
    """
    Enhance resume bullet points to better match the job description.
    
    Args:
        resume_text (str): Extracted resume content
        job_description (str): Job posting description
        
    Returns:
        str: Enhanced resume suggestions or None if generation fails
    """
    client = get_openai_client()
    if not client:
        return None
    
    prompt = f"""
    Based on the resume and job description provided below, suggest improved bullet points for the resume that:
    
    1. Better align with the job requirements and keywords
    2. Use stronger action verbs and quantifiable achievements
    3. Highlight relevant skills and experiences
    4. Follow the STAR method (Situation, Task, Action, Result) where applicable
    5. Are concise yet impactful
    
    CURRENT RESUME:
    {resume_text}
    
    TARGET JOB DESCRIPTION:
    {job_description}
    
    Please provide:
    1. 5-8 enhanced bullet points that would strengthen this resume for the target role
    2. Focus on the most relevant experience sections
    3. Include specific keywords from the job description where appropriate
    4. Make each bullet point start with a strong action verb
    
    Format your response as a bulleted list with explanations for why each enhancement would be effective.
    """
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),  # Use gpt-4o-mini as fallback
            messages=[
                {"role": "system", "content": "You are an expert resume writer and career coach who specializes in optimizing resumes for specific job opportunities using industry best practices."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=int(os.getenv("MAX_TOKENS", 1000)),
            temperature=float(os.getenv("TEMPERATURE", 0.7))
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"❌ Error enhancing resume bullets: {str(e)}")
        if "rate_limit" in str(e).lower():
            st.error("💡 Rate limit exceeded. Please wait a moment and try again.")
        elif "quota" in str(e).lower():
            st.error("💡 API quota exceeded. Please check your OpenAI billing.")
        return None

def analyze_job_match(resume_text, job_description):
    """
    Analyze how well the resume matches the job description.
    
    Args:
        resume_text (str): Extracted resume content
        job_description (str): Job posting description
        
    Returns:
        dict: Match analysis with score and recommendations
    """
    client = get_openai_client()
    if not client:
        return None
    
    prompt = f"""
    Analyze how well this resume matches the job description and provide:
    
    1. A match score (0-100%)
    2. Top 5 strengths that align with the job
    3. Top 3 gaps or areas for improvement
    4. Specific keywords from the job description that should be added to the resume
    5. Overall recommendation
    
    RESUME:
    {resume_text}
    
    JOB DESCRIPTION:
    {job_description}
    
    Provide your analysis in a structured format.
    """
    
    try:
        response = client.chat.completions.create(
            model=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),  # Use gpt-4o-mini as fallback
            messages=[
                {"role": "system", "content": "You are an expert ATS (Applicant Tracking System) analyzer and career coach who helps optimize resumes for specific job opportunities."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=int(os.getenv("MAX_TOKENS", 800)),
            temperature=float(os.getenv("TEMPERATURE", 0.5))
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        st.error(f"❌ Error analyzing job match: {str(e)}")
        if "rate_limit" in str(e).lower():
            st.error("💡 Rate limit exceeded. Please wait a moment and try again.")
        elif "quota" in str(e).lower():
            st.error("💡 API quota exceeded. Please check your OpenAI billing.")
        return None

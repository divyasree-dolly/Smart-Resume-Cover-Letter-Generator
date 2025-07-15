"""
Utility functions for the Smart Resume & Cover Letter Generator.
"""

import streamlit as st

def display_results(result_type, content):
    """
    Display AI-generated results with formatting and download options.
    
    Args:
        result_type (str): Type of result ('cover_letter' or 'resume_bullets')
        content (str): Generated content to display
    """
    if not content:
        st.error("No content to display")
        return
    
    # Display the content
    if result_type == "cover_letter":
        st.text_area(
            "Generated Cover Letter",
            content,
            height=400,
            help="Review and edit as needed before using"
        )
        
        # Download button
        st.download_button(
            label="📥 Download Cover Letter",
            data=content,
            file_name="cover_letter.txt",
            mime="text/plain",
            use_container_width=True
        )
        
    elif result_type == "resume_bullets":
        st.markdown("### Enhanced Resume Bullet Points")
        st.markdown(content)
        
        # Download button
        st.download_button(
            label="📥 Download Enhanced Bullets",
            data=content,
            file_name="enhanced_resume_bullets.txt",
            mime="text/plain",
            use_container_width=True
        )
    
    # Feedback section
    st.markdown("---")
    st.markdown("### 💬 Feedback")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👍 Great!", use_container_width=True):
            st.success("Thanks for the feedback!")
    
    with col2:
        if st.button("👌 Good", use_container_width=True):
            st.info("Thanks! We'll keep improving.")
    
    with col3:
        if st.button("👎 Needs Work", use_container_width=True):
            st.warning("Thanks for the feedback. Try regenerating or adjusting your inputs.")

def format_text_for_download(content, file_type="txt"):
    """
    Format content for download based on file type.
    
    Args:
        content (str): Content to format
        file_type (str): Target file type ('txt', 'docx', etc.)
        
    Returns:
        str: Formatted content
    """
    if file_type == "txt":
        return content
    
    # Add more formatting options here as needed
    return content

def validate_inputs(resume_text, job_description):
    """
    Validate user inputs before processing.
    
    Args:
        resume_text (str): Resume content
        job_description (str): Job description
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not resume_text or len(resume_text.strip()) < 50:
        return False, "Resume text is too short. Please upload a complete resume."
    
    if not job_description or len(job_description.strip()) < 100:
        return False, "Job description is too short. Please provide a complete job posting."
    
    return True, ""

def show_tips():
    """Display helpful tips for users"""
    with st.expander("💡 Tips for Better Results"):
        st.markdown("""
        ### 📄 Resume Tips:
        - Upload a complete, well-formatted resume
        - Ensure your resume includes specific achievements and metrics
        - Use clear section headers (Experience, Education, Skills, etc.)
        
        ### 🎯 Job Description Tips:
        - Include the complete job posting, not just the title
        - Copy requirements, responsibilities, and company info
        - The more details you provide, the better the AI can tailor content
        
        ### ✍️ Cover Letter Tips:
        - Review and personalize the generated content
        - Add specific company names and details
        - Customize the greeting if you know the hiring manager's name
        
        ### 📈 Resume Enhancement Tips:
        - Focus on quantifiable achievements
        - Use keywords from the job description
        - Tailor your experience to match the role requirements
        """)

def show_about():
    """Display information about the application"""
    with st.expander("ℹ️ About This App"):
        st.markdown("""
        ### 🚀 Smart Resume & Cover Letter Generator
        
        This application uses OpenAI's GPT-4 to help you create tailored job application materials.
        
        **Features:**
        - ✍️ Generate personalized cover letters
        - 📈 Enhance resume bullet points
        - 🎯 Match your skills to job requirements
        - 📥 Download results in various formats
        
        **How it works:**
        1. Upload your resume (PDF or DOCX)
        2. Paste the job description
        3. Let AI generate tailored content
        4. Review, edit, and download
        
        **Privacy:**
        - Your data is processed securely
        - Content is not stored permanently
        - API calls are made directly to OpenAI
        
        **Tips:**
        - Always review and customize AI-generated content
        - Use specific job descriptions for better results
        - Keep your resume updated and comprehensive
        """)

def display_error_help():
    """Display help for common errors"""
    st.markdown("""
    ### 🆘 Common Issues & Solutions
    
    **API Key Issues:**
    - Make sure you have a valid OpenAI API key
    - Check that you have sufficient credits
    - Verify the key is entered correctly
    
    **File Upload Issues:**
    - Only PDF and DOCX files are supported
    - Ensure your file isn't corrupted
    - Try a different file format if needed
    
    **Generation Issues:**
    - Check your internet connection
    - Try with a shorter job description
    - Ensure your resume has enough content
    """)

def calculate_content_stats(text):
    """
    Calculate basic statistics for text content.
    
    Args:
        text (str): Input text
        
    Returns:
        dict: Statistics including word count, character count, etc.
    """
    if not text:
        return {"words": 0, "characters": 0, "lines": 0}
    
    words = len(text.split())
    characters = len(text)
    lines = len(text.split('\n'))
    
    return {
        "words": words,
        "characters": characters,
        "lines": lines
    }

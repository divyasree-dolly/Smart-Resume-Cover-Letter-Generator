import streamlit as st
import os
from dotenv import load_dotenv
from src.resume_parser import extract_text_from_file
from src.ai_generator import generate_cover_letter, enhance_resume_bullets
from src.utils import display_results

# Load environment variables
load_dotenv()

def main():
    """Main Streamlit application"""
    
    # Page configuration
    st.set_page_config(
        page_title="Smart Resume & Cover Letter Generator",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Header
    st.title("🚀 Smart Resume & Cover Letter Generator")
    st.markdown("*AI-powered career tools to help you land your dream job*")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Check for API key in environment
        api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key:
            st.success("✅ API Key configured!")
            st.info("🔒 Using environment API key")
        else:
            # Fallback to user input for development
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                help="Enter your OpenAI API key. Get one at https://platform.openai.com"
            )
            
            if api_key:
                os.environ["OPENAI_API_KEY"] = api_key
                st.success("✅ API Key set!")
            else:
                st.warning("⚠️ Please enter your OpenAI API key to continue")
            
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
        1. **Enter your OpenAI API key** above
        2. **Upload your resume** (PDF or DOCX)
        3. **Paste the job description** you're applying for
        4. **Choose what to generate** and click the button
        5. **Review and customize** the AI-generated content
        """)
    
    # Main content area
    if not api_key:
        st.info("👈 Please enter your OpenAI API key in the sidebar to get started")
        return
    
    # File upload section
    st.header("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Choose your resume file",
        type=['pdf', 'docx'],
        help="Upload your resume in PDF or DOCX format"
    )
    
    # Extract resume text
    resume_text = ""
    if uploaded_file:
        with st.spinner("📖 Reading your resume..."):
            resume_text = extract_text_from_file(uploaded_file)
            
        if resume_text:
            st.success(f"✅ Resume uploaded successfully! ({len(resume_text)} characters)")
            
            # Show preview in expander
            with st.expander("👀 Preview Resume Content"):
                st.text_area("Resume Text", resume_text, height=200, disabled=True)
        else:
            st.error("❌ Could not extract text from the resume. Please check the file format.")
            return
    
    # Job description input
    st.header("🎯 Job Description")
    job_description = st.text_area(
        "Paste the job description here",
        height=200,
        placeholder="Copy and paste the job posting you're applying for...",
        help="Include the full job description for best results"
    )
    
    # Generation options
    if resume_text and job_description:
        st.header("🤖 AI Generation Options")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("✍️ Generate Cover Letter", type="primary", use_container_width=True):
                with st.spinner("🤖 Generating your cover letter..."):
                    cover_letter = generate_cover_letter(resume_text, job_description)
                    
                if cover_letter:
                    st.header("📝 Generated Cover Letter")
                    display_results("cover_letter", cover_letter)
                else:
                    st.error("❌ Failed to generate cover letter. Please try again.")
        
        with col2:
            if st.button("📈 Enhance Resume Bullets", type="secondary", use_container_width=True):
                with st.spinner("🤖 Enhancing your resume..."):
                    enhanced_bullets = enhance_resume_bullets(resume_text, job_description)
                    
                if enhanced_bullets:
                    st.header("🎯 Enhanced Resume Bullets")
                    display_results("resume_bullets", enhanced_bullets)
                else:
                    st.error("❌ Failed to enhance resume bullets. Please try again.")
    
    elif not resume_text:
        st.info("📄 Please upload your resume to continue")
    elif not job_description:
        st.info("🎯 Please paste the job description to continue")
    
    # Footer
    st.markdown("---")
    st.markdown("*Built with ❤️ using Streamlit and OpenAI*")

if __name__ == "__main__":
    main()

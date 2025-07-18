import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import hashlib
from src.resume_parser import extract_text_from_file
from src.ai_generator import generate_cover_letter, enhance_resume_bullets
from src.utils import display_results

# Load environment variables
load_dotenv()

# Usage tracking functions
def get_user_id():
    """Generate a unique user ID based on session"""
    if 'user_id' not in st.session_state:
        # Create a unique identifier for this session
        import random
        import string
        user_info = f"{datetime.now().timestamp()}-{''.join(random.choices(string.ascii_letters, k=6))}"
        st.session_state.user_id = hashlib.md5(user_info.encode()).hexdigest()[:10]
    return st.session_state.user_id

def check_usage_limit(user_id, max_requests=10):
    """Check if user has exceeded daily usage limit"""
    today = datetime.now().strftime('%Y-%m-%d')
    usage_key = f"usage_{user_id}_{today}"
    
    if usage_key not in st.session_state:
        st.session_state[usage_key] = 0
    
    return st.session_state[usage_key] < max_requests

def increment_usage(user_id):
    """Increment user's daily usage count"""
    today = datetime.now().strftime('%Y-%m-%d')
    usage_key = f"usage_{user_id}_{today}"
    
    if usage_key not in st.session_state:
        st.session_state[usage_key] = 0
    
    st.session_state[usage_key] += 1
    return st.session_state[usage_key]

def get_remaining_requests(user_id, max_requests=10):
    """Get remaining requests for the user"""
    today = datetime.now().strftime('%Y-%m-%d')
    usage_key = f"usage_{user_id}_{today}"
    used = st.session_state.get(usage_key, 0)
    return max_requests - used

def main():
    """Main Streamlit application - Production version with API key options and usage limits"""
    
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
    
    # Get user ID for tracking
    user_id = get_user_id()
    remaining_requests = get_remaining_requests(user_id)
    
    # Sidebar for API key selection and configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key selection
        api_option = st.radio(
            "Choose API Key Option:",
            ["🆓 Use Free Service (10 requests/day)", "🔑 Use My Own API Key (Unlimited)"],
            help="Free service has daily limits. Use your own key for unlimited access."
        )
        
        api_key = None
        using_own_key = False
        
        if api_option == "🔑 Use My Own API Key (Unlimited)":
            user_api_key = st.text_input(
                "Enter Your OpenAI API Key:",
                type="password",
                help="Get your API key from https://platform.openai.com/api-keys"
            )
            if user_api_key:
                api_key = user_api_key
                using_own_key = True
                st.success("✅ Using your API key!")
            else:
                st.warning("⚠️ Please enter your OpenAI API key")
        else:
            # Use default API key
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                st.success("✅ Using free service!")
                st.info(f"🎯 {remaining_requests} requests remaining today")
                if remaining_requests <= 3:
                    st.warning("⚠️ Consider using your own API key for unlimited access")
            else:
                st.error("🚫 Free service temporarily unavailable")
        
        # Set the API key in environment
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        st.markdown("---")
        st.markdown("### 📋 Instructions")
        st.markdown("""
        1. **Choose your API option** above
        2. **Upload your resume** (PDF or DOCX)
        3. **Paste the job description** you're applying for
        4. **Generate content** and download results
        """)
        
        st.markdown("---")
        st.markdown("### 💡 Pro Tips")
        st.markdown("""
        - Use complete job descriptions for better results
        - Review and personalize all AI-generated content
        - Include metrics and achievements in your resume
        """)
        
        if not using_own_key:
            st.markdown("---")
            st.markdown("### � Upgrade Benefits")
            st.markdown("""
            **Use your own API key for:**
            - ✨ Unlimited requests
            - 🚀 Faster processing
            - 🎯 Priority support
            - 🔒 Enhanced privacy
            """)
    
    # Check if we can proceed
    if not api_key:
        st.warning("👈 Please configure your API key in the sidebar to continue")
        return
    
    # Check usage limits for free service
    if not using_own_key and not check_usage_limit(user_id):
        st.error("🚫 Daily limit reached! You've used all 10 free requests today.")
        st.info("💡 **Options to continue:**")
        st.markdown("""
        - 🔑 **Use your own OpenAI API key** (select in sidebar)
        - ⏰ **Wait until tomorrow** for fresh requests
        - 💰 **Costs only ~$0.01-0.02 per request** with your own key
        """)
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
                # Check usage limit for free service
                if not using_own_key and not check_usage_limit(user_id):
                    st.error("🚫 Daily limit reached! Please use your own API key or wait until tomorrow.")
                    return
                
                with st.spinner("🤖 Generating your cover letter..."):
                    cover_letter = generate_cover_letter(resume_text, job_description)
                    
                if cover_letter:
                    # Increment usage for free service
                    if not using_own_key:
                        used_count = increment_usage(user_id)
                        remaining = get_remaining_requests(user_id)
                        st.sidebar.info(f"🎯 {remaining} requests remaining today")
                    
                    st.header("📝 Generated Cover Letter")
                    display_results("cover_letter", cover_letter)
                else:
                    st.error("❌ Failed to generate cover letter. Please try again.")
        
        with col2:
            if st.button("📈 Enhance Resume Bullets", type="secondary", use_container_width=True):
                # Check usage limit for free service
                if not using_own_key and not check_usage_limit(user_id):
                    st.error("🚫 Daily limit reached! Please use your own API key or wait until tomorrow.")
                    return
                
                with st.spinner("🤖 Enhancing your resume..."):
                    enhanced_bullets = enhance_resume_bullets(resume_text, job_description)
                    
                if enhanced_bullets:
                    # Increment usage for free service
                    if not using_own_key:
                        used_count = increment_usage(user_id)
                        remaining = get_remaining_requests(user_id)
                        st.sidebar.info(f"🎯 {remaining} requests remaining today")
                    
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

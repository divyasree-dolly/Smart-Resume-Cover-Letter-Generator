<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Smart Resume & Cover Letter Generator - Copilot Instructions

## Project Overview
This is a Python-based Streamlit web application that generates tailored cover letters and enhances resume bullet points using OpenAI's GPT models.

## Key Technologies
- **Frontend**: Streamlit for web interface
- **AI/ML**: OpenAI GPT-4 for content generation
- **File Processing**: PyPDF2 for PDF parsing, python-docx for DOCX files
- **Environment**: python-dotenv for configuration management

## Code Style & Best Practices
- Follow PEP 8 Python style guidelines
- Use type hints where appropriate
- Include comprehensive docstrings for functions
- Handle errors gracefully with user-friendly messages
- Use Streamlit's caching mechanisms for performance

## Project Structure
- `app.py` - Main Streamlit application entry point
- `src/resume_parser.py` - File parsing utilities for PDF/DOCX
- `src/ai_generator.py` - OpenAI integration and prompt engineering
- `src/utils.py` - Helper functions and UI components

## AI Integration Guidelines
- Use specific, well-crafted prompts for consistent outputs
- Implement proper error handling for API calls
- Include fallback options for API failures
- Optimize token usage while maintaining quality

## UI/UX Considerations
- Keep the interface clean and intuitive
- Provide clear feedback during processing
- Include helpful tips and guidance for users
- Make generated content easily downloadable

## Security & Privacy
- Never log or store user's resume content
- Securely handle API keys through environment variables
- Validate file uploads to prevent security issues

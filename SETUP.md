# 🚀 Smart Resume & Cover Letter Generator - Setup Guide

## Quick Setup for New Users

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd "Smart Resume & Cover Letter Generator"
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-proj-your_actual_api_key_here
```

### 5. Get Your OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account and add billing information
3. Generate a new API key
4. Copy the key to your `.env` file

### 6. Run the Application
```bash
# Option 1: Use the startup script
./start.sh

# Option 2: Direct command
streamlit run app.py
```

### 7. Open in Browser
Navigate to `http://localhost:8501` and start generating!

## 🔧 Configuration Options

Edit your `.env` file to customize:
- `DEFAULT_MODEL`: Choose between `gpt-4o-mini` (cheaper) or `gpt-4` (higher quality)
- `MAX_TOKENS`: Adjust response length (1000 recommended)
- `TEMPERATURE`: Control creativity (0.7 recommended)

## 💰 Cost Estimation

Using `gpt-4o-mini`:
- Cover letter generation: ~$0.01-0.02 per request
- Resume enhancement: ~$0.01-0.03 per request
- $5-10 credit should last for hundreds of generations

## 🔒 Security Notes

- **NEVER** commit your `.env` file to GitHub
- Keep your OpenAI API key private
- Monitor your API usage on the OpenAI dashboard
- Consider setting spending limits

## 🚀 Deployment

See `README.md` for deployment instructions to Streamlit Cloud, Heroku, or other platforms.

## 📞 Support

If you encounter issues:
1. Check that your API key is valid and has credits
2. Ensure all dependencies are installed correctly  
3. Verify your internet connection
4. Try regenerating if the AI output seems off

Happy job hunting! 🎯

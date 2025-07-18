# 🚀 Streamlit Cloud Deployment Guide

## Step 1: Prepare Your Repository

### 1.1 Initialize Git Repository (if not done)
```bash
git init
git add .
git commit -m "Initial commit: Smart Resume & Cover Letter Generator"
```

### 1.2 Create GitHub Repository
1. Go to [GitHub](https://github.com) and click "New repository"
2. Repository name: `smart-resume-generator` (or your preferred name)
3. Description: `AI-powered resume and cover letter generator using OpenAI GPT`
4. Make it **Public** (required for free Streamlit Cloud)
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### 1.3 Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/smart-resume-generator.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Streamlit Cloud

### 2.1 Sign Up for Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Authorize Streamlit to access your repositories

### 2.2 Deploy Your App
1. Click **"New app"**
2. Select your repository: `YOUR_USERNAME/smart-resume-generator`
3. Choose branch: `main`
4. Main file path: `app_production.py`
5. App URL: Choose a custom URL (e.g., `smart-resume-generator`)

### 2.3 Configure Secrets (IMPORTANT!)
1. In your app dashboard, click **"⚙️ Settings"**
2. Go to **"Secrets"** tab
3. Add your secrets in TOML format:

```toml
# Paste your OpenAI API key here
OPENAI_API_KEY = "sk-proj-your-actual-api-key-here"

# Optional configurations
DEFAULT_MODEL = "gpt-4o-mini"
MAX_TOKENS = 1000
TEMPERATURE = 0.7
MAX_FREE_REQUESTS_PER_DAY = 10
```

### 2.4 Deploy!
1. Click **"Deploy!"**
2. Wait for deployment (usually 2-3 minutes)
3. Your app will be live at: `https://your-app-name.streamlit.app`

## Step 3: Post-Deployment

### 3.1 Test Your App
- ✅ Try uploading a resume
- ✅ Test cover letter generation
- ✅ Test resume enhancement
- ✅ Verify usage limits work
- ✅ Test both free and custom API key options

### 3.2 Monitor Usage
- Check your OpenAI usage at [platform.openai.com](https://platform.openai.com)
- Set up billing alerts to avoid surprises
- Monitor app performance in Streamlit Cloud dashboard

### 3.3 Share Your App
- Add the live URL to your GitHub README
- Share on social media/portfolio
- Add to your resume/CV projects section

## Step 4: Maintenance & Updates

### 4.1 Making Updates
```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push origin main
```
*Streamlit Cloud will automatically redeploy when you push to main*

### 4.2 Managing Costs
- **Free tier**: Uses your OpenAI credits but app hosting is free
- **Monitor usage**: Check OpenAI dashboard regularly
- **Usage limits**: Built-in 10 requests/day limit for free users

## 🎯 App Features After Deployment

### For Free Users:
- ✅ 10 AI requests per day
- ✅ Full functionality
- ✅ Download capabilities
- ✅ Professional interface

### For Users with API Keys:
- ✅ Unlimited requests
- ✅ Direct billing to their account
- ✅ Premium experience

## 🔧 Troubleshooting

### Common Issues:
1. **App won't start**: Check secrets are properly configured
2. **API errors**: Verify OpenAI API key is valid and has credits
3. **Usage tracking issues**: Clear browser cache and try again

### Getting Help:
- [Streamlit Community](https://discuss.streamlit.io)
- [Streamlit Documentation](https://docs.streamlit.io)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🚀 You're Live!

Once deployed, your app will be accessible worldwide at your custom Streamlit URL. Users can:
- Use the free service (limited)
- Add their own API keys for unlimited access
- Generate professional cover letters and resume enhancements
- Download their results

Perfect for showcasing your AI development skills! 🎉

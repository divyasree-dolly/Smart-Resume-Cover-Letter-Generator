# Smart Resume & Cover Letter Generator 🚀

An AI-powered web application that generates tailored cover letters and improves resume bullet points using OpenAI's GPT models.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- 📄 **Resume Upload**: Support for PDF and DOCX formats
- 🎯 **Job Description Analysis**: Paste job descriptions for tailored outputs
- ✍️ **Cover Letter Generation**: AI-generated, personalized cover letters
- 📝 **Resume Enhancement**: Improve existing bullet points with AI suggestions
- 🎨 **User-Friendly Interface**: Clean, intuitive Streamlit web interface
- 📥 **Download Options**: Save results in multiple formats

## 🚀 Quick Start

**New to this project?** Check out [SETUP.md](SETUP.md) for detailed setup instructions.

### Prerequisites
- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd "Smart Resume & Cover Letter Generator"

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run the application
streamlit run app.py
```

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── src/
│   ├── resume_parser.py   # Resume parsing utilities
│   ├── ai_generator.py    # OpenAI integration
│   └── utils.py          # Helper functions
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (create this)
└── README.md             # Project documentation
```

## Usage

1. **Upload Resume**: Choose your resume file (PDF or DOCX)
2. **Paste Job Description**: Copy the job posting you're applying for
3. **Generate Content**: Click to create your tailored cover letter
4. **Enhance Resume**: Get AI suggestions for better bullet points

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your API key in the app's "Secrets" section
4. Deploy with one click!

### Other Platforms
- **Heroku**: Use the included `Procfile`
- **Railway**: Set environment variables in dashboard
- **Render**: Configure environment in settings

See [SETUP.md](SETUP.md) for detailed deployment instructions.

## 💰 Cost Information

Using `gpt-4o-mini` (recommended):
- Cover letter: ~$0.01-0.02 per generation
- Resume enhancement: ~$0.01-0.03 per generation
- $5-10 in OpenAI credits = hundreds of generations

## 🔒 Security & Privacy

- 🔐 API keys are handled securely through environment variables
- 🚫 No user data is stored permanently
- 🛡️ All processing happens client-side or through OpenAI's secure API
- 👀 Always review and customize AI-generated content before use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

Having issues? Check out:
- [SETUP.md](SETUP.md) for setup troubleshooting
- [OpenAI API documentation](https://platform.openai.com/docs)
- [Streamlit documentation](https://docs.streamlit.io)

## ⭐ Show Your Support

If this project helped you land your dream job, please give it a star! ⭐

---

*Built with ❤️ using Streamlit and OpenAI GPT*

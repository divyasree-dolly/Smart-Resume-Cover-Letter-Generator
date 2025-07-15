#!/bin/bash

# Smart Resume & Cover Letter Generator Startup Script

echo "🚀 Starting Smart Resume & Cover Letter Generator..."

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found. Please run setup first."
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found. Creating from template..."
    cp .env.example .env
    echo "📝 Please edit .env file and add your OpenAI API key"
    echo "   Then run this script again."
    exit 1
fi

# Activate virtual environment and run the app
echo "✅ Starting Streamlit application..."
source .venv/bin/activate
streamlit run app.py

echo "🎉 Application started! Open http://localhost:8501 in your browser"

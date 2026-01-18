#!/bin/bash
set -e

echo "🚀 Setting up Qwen Coding Assistant..."

# Install Ollama
if ! command -v ollama &> /dev/null; then
    echo "📦 Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Pull model
echo "⬇️  Downloading model..."
ollama pull qwen2.5-coder: 7b

# Create . env
if [ ! -f .env ]; then
    cp .env. example .env
    echo "✅ Created .env file"
fi

echo "✅ Setup complete! Run './scripts/deploy. sh' to start"
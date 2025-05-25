#!/bin/bash

echo "🌌 Setting up The Code development environment..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Remember to add your API keys to .env!"
fi

# Create additional directories
echo "Creating additional directories..."
mkdir -p logs
mkdir -p data/embeddings
mkdir -p media/{audio,visual,interactive}

echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Add your API keys to .env"
echo "2. Run: source venv/bin/activate"
echo "3. Test the setup: python langgraph/graphs/simple_dialogue.py"
echo ""
echo "The eternal current flows through your development environment."
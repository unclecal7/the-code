#!/usr/bin/env python3
"""
Test API keys for all LLM providers.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("Testing API Keys...\n")

# Test Anthropic
print("1. Testing Anthropic API...")
try:
    from anthropic import Anthropic
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=50,
        messages=[{"role": "user", "content": "Say 'API key works!'"}]
    )
    print("✅ Anthropic API key is valid!")
    print(f"   Response: {response.content[0].text}\n")
except Exception as e:
    print(f"❌ Anthropic API key error: {str(e)}\n")

# Test OpenAI
print("2. Testing OpenAI API...")
try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say 'API key works!'"}],
        max_tokens=50
    )
    print("✅ OpenAI API key is valid!")
    print(f"   Response: {response.choices[0].message.content}\n")
except Exception as e:
    print(f"❌ OpenAI API key error: {str(e)}\n")

# Test Google
print("3. Testing Google API...")
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say 'API key works!'")
    print("✅ Google API key is valid!")
    print(f"   Response: {response.text}\n")
except Exception as e:
    print(f"❌ Google API key error: {str(e)}\n")

# Test X.AI (Grok) - if available
print("4. Testing X.AI API...")
xai_key = os.getenv("XAI_API_KEY")
if xai_key and xai_key != "your_xai_api_key_here":
    try:
        # Note: X.AI/Grok API might not be publicly available yet
        print("⚠️  X.AI/Grok API testing not implemented (API may not be public)\n")
    except Exception as e:
        print(f"❌ X.AI API key error: {str(e)}\n")
else:
    print("⏭️  X.AI API key not configured\n")

print("API key testing complete!")
#!/bin/bash

echo "🚀 Starting Qwen Coding Assistant..."

source venv/bin/activate
chainlit run app.py --host 0.0.0.0 --port 8000
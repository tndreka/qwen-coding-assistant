# 🤖 Qwen Coding Assistant

AI-powered coding assistant using Qwen2.5-Coder and Chainlit.

## Features

- 💻 Code generation and completion
- 🐛 Debugging assistance
- 📚 Code explanations
- ✅ Unit test generation
- 🔧 Code refactoring suggestions

## Quick Start

### 1. Setup
```bash
./scripts/setup.sh
```

### 2. Run
```bash
./scripts/deploy.sh
```

### 3. Access
Open your browser:  `http://localhost:8000`

## Requirements

- Python 3.8+
- Ollama
- 8GB RAM minimum

## Configuration

Edit `.env` to customize:
- `MODEL_NAME` - Ollama model to use
- `PORT` - Server port
- `LOG_LEVEL` - Logging verbosity

## Project Structure

```
qwen-coding-assistant/
├── app.py              # Main application
├── core/               # Core configuration
├── utils/              # Utilities
├── handlers/           # Request handlers
├── scripts/            # Setup & deploy scripts
└── requirements.txt    # Python dependencies
```

## License

MIT
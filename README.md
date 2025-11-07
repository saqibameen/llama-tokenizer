# Llama Tokenizer

Tokenization demo using the Llama 3.3 70B model tokenizer.

## Setup

1. Install uv (if not already installed):
```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv
```

   Verify installation:
```bash
uv --version
```

2. Install dependencies:
```bash
uv sync
```

3. Copy the example environment file and add your token:
```bash
cp .env.example .env
```
Then edit `.env` and replace `your_huggingface_token_here` with your actual token.

4. Run the demo:
```bash
uv run main.py
```

## Authentication

The Llama 3.3 70B model is gated. You need to:
1. Request access at https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct
2. Create a token at https://huggingface.co/settings/tokens (use read+write permissions)
3. Add your token to the `.env` file

## Requirements

- Python 3.11+
- transformers library
- torch library
- python-dotenv library

## Usage

The script loads the Llama 3.3 70B tokenizer and demonstrates tokenization of example text.

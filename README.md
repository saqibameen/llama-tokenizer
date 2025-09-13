# Llama Tokenizer Demo

A simple Python script to demonstrate tokenization using the Llama 3.3 70B model tokenizer.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Copy the example environment file and add your token:
```bash
cp .env.example .env
```
Then edit `.env` and replace `your_huggingface_token_here` with your actual token.

3. Run the demo:
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
import os
from dotenv import load_dotenv
from transformers import AutoTokenizer

# Load environment variables from .env file
load_dotenv()


def main():
    # Specify the model ID
    model_id = "meta-llama/Llama-3.3-70B-Instruct"
    
    # Get token from environment variable (loaded from .env file)
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        raise ValueError("Please set HF_TOKEN in your .env file or environment variable")

    # Load the Llama 3.3 70B tokenizer with authentication
    tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)

    # Example text to tokenize
    text = "This is an example sentence for tokenization."

    # Tokenize and print results
    tokens = tokenizer(text)

    # Total tokens
    print(f"Total tokens: {len(tokens['input_ids'])}")


if __name__ == "__main__":
    main()

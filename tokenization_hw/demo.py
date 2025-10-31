from tokenizer import TextTokenizer

def main():
    tokenizer = TextTokenizer()
    sample_text = "Hello, world! This is a test sentence. How are you today?"
    results = tokenizer.tokenize_all(sample_text)

    for method, tokens in results.items():
        print(f"{method}: {tokens}")

if __name__ == "__main__":
    main()
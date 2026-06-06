#GPT tokenizer like encoder and decoder

import tiktoken

def main():
    #Enconder
    encoded = Tokenizer.encode(text)
    print(f"Encoded: {encoded}")
    #Decoder
    decoded = Tokenizer.decode(encoded)
    print(f"Decoded: {decoded}")

if __name__ == "__main__":
    Tokenizer = tiktoken.encoding_for_model("gpt-4o")
    text="This is the test text im providing" #Text 
    main()
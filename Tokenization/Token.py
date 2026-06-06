#GPT tokenizer like encoder and decoder

import tiktoken

def main():
    #Encoded Text
    encoded = Tokenizer.encode(text)
    print(f"Encoded: {encoded}")
    #Decoded Text
    decoded = Tokenizer.decode(encoded)
    print(f"Decoded: {decoded}")

if __name__ == "__main__":
    Tokenizer = tiktoken.encoding_for_model("gpt-4o")
    text="Wht is chatGPT" #Text 
    main()
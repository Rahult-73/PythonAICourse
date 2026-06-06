from openai import OpenAI
from dotenv import load_dotenv
import os
from colorama import Fore, Style, init

def tokenusage(response):
    print()
    print("="* 40,end="\n\n")
    print(Fore.GREEN + f"Prompt Tokens: {response.usage.prompt_tokens}")

    print(Fore.GREEN + 
        f"Completion Tokens: {response.usage.completion_tokens}")

    print(Fore.RED + 
        f"Total Tokens: {response.usage.total_tokens}")
    print(Style.RESET_ALL)
    print("="*40)

def main(text):
    systm_prompt="""
    Your a coding assisatance.
    Rules
        - Answer only coding related question
        - Write in short code
        - Output should be in json format
    Output:
        {{ "code": "string" or null,"isCodeRelatedQuestion":bool}}
    Examples:
        Q: What is apple color?
        A: {{"code":null,"isCodeRelatedQuestion":false}}

        Q: write add program in python
        A: {{"code":"def add(a,b): return a+b","isCodeRelatedQuestion":true}}
    """
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        n=1,
        messages=[
            {
                "role":"system","content":systm_prompt
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    print(response.choices[0].message.content)
    # tokenusage(response)

if __name__ == "__main__":
    load_dotenv()
    init()
    api_key = os.getenv("GEMINI_API_KEY")
    client = OpenAI(    api_key=api_key,
                    base_url="https://generativelanguage.googleapis.com/v1beta/")
    main("write simple substraction code in python")

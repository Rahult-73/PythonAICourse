from openai import OpenAI
from dotenv import load_dotenv
import os

def main(text):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        n=1,
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = OpenAI(    api_key=api_key,
                    base_url="https://generativelanguage.googleapis.com/v1beta/")
    main("What is GPT?, context: exactly 10 words, don't use more tokens, any answer is fine")
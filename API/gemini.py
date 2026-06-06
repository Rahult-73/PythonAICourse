import os
from dotenv import load_dotenv
from google import genai

def main(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )

    print(response.text)

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    main("What is GPT?")
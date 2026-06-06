from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def main(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    main("What is GPT?")
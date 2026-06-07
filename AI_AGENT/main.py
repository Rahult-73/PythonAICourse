from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

def getweather(city: str):
    url = f"https://wttr.in/{city}?format=%c+%t"
    response=requests.get(url)

    if response.status_code == 200:
        return f"The weather for the {city} is {response.text}"
    
    return "Something went wrong"

def main():
    text=input("Enter you query 👉 ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )
    print(response.choices[0].message.content)

print(getweather("Chennai"))

#https://wttr.in/goa?format=%c+%t


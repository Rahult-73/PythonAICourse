from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPEN_AI_API_KEY")



def main():
    print("Hello")

if __name__ == "__main__":
    main()
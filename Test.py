from dotenv import load_dotenv
import os
from colorama import Fore, Style, init
import json

def main():
    result=json.dumps({"step":"Plan","Contant":"javascript"})
    print(result)

if __name__ == "__main__":
    init()
    main()
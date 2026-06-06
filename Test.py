from dotenv import load_dotenv
import os
from colorama import Fore, Style, init

def main():
    print()
    print("="* 40,end="\n\n")
    print(Fore.GREEN + f"Prompt Tokens: 40")

    print(Fore.GREEN + 
        f"Completion Tokens: 50")

    print(Fore.GREEN + 
        f"Total Tokens: 60")
    print(Style.RESET_ALL)
    print("="*40)

if __name__ == "__main__":
    init()
    main()
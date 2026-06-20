from ollama import Client
from colorama import Fore, Style, init
import json

client = Client(host="http://localhost:11434")

SYSTEM_PROMPT = """
You are a JSON reasoning assistant.

Rules:

* Return ONLY valid JSON
* Never explain outside JSON
* Never wrap JSON in markdown
* Generate EXACTLY one step at a time
* If you generate ANY text outside JSON, your response is invalid

Allowed steps:

* PLAN
* OUTPUT

IMPORTANT:

* You MUST generate AT LEAST 3 PLAN steps before OUTPUT
* Each PLAN must contain NEW reasoning
* Do not skip directly to OUTPUT

Output format:
{
"step": "PLAN" | "OUTPUT",
"content": "string"
}

Example:

{
"step": "PLAN",
"content": "Need subtraction logic."
}

{
"step": "PLAN",
"content": "Function should accept two parameters."
}

{
"step": "PLAN",
"content": "Return difference of both numbers."
}

{
"step": "OUTPUT",
"content": "def subtract(a, b): return a - b"
}
"""

messages = [
{
"role": "system",
"content": SYSTEM_PROMPT
},
{
"role": "user",
"content": "write a browser javascript to autofill form by running the script in the browser console"
}
]

plan_count = 0

while True:


    response = client.chat(
        model="qwen2.5:1.5b",
        messages=messages,
        options={
            "temperature": 0
        }
    )

    output = response["message"]["content"]

    print(Fore.GREEN + "\nRAW OUTPUT:")
    print(output)
    print(Style.RESET_ALL)

    try:

        # safer JSON extraction
        start = output.find("{")
        end = output.rfind("}") + 1

        if start == -1 or end == -1:
            raise Exception("No JSON object found")

        cleaned_output = output[start:end]

        parsed = json.loads(cleaned_output)

        print(Fore.CYAN + "\nPARSED:")
        print(parsed)
        print(Style.RESET_ALL)

    except Exception as e:

        print(Fore.RED + "\nJSON ERROR:")
        print(e)

        print(Fore.YELLOW + "\nRAW MODEL OUTPUT:")
        print(output)
        print(Style.RESET_ALL)

        # retry reasoning
        messages.append({
            "role": "user",
            "content": "Your previous response was invalid JSON. Return ONLY valid JSON."
        })

        continue

    # append assistant reasoning history
    messages.append({
        "role": "assistant",
        "content": cleaned_output
    })

    # count PLAN steps
    if parsed["step"] == "PLAN":
        plan_count += 1

    # validate OUTPUT
    if parsed["step"] == "OUTPUT":

        if plan_count < 3:

            print(
                Fore.YELLOW +
                "\nOUTPUT rejected. Minimum 3 PLAN steps required."
            )

            print(Style.RESET_ALL)

            messages.append({
                "role": "user",
                "content": "Continue reasoning. Minimum 3 PLAN steps required."
            })

            continue

        print(Fore.MAGENTA + "\nFINAL OUTPUT:")
        print(parsed["content"])
        print(Style.RESET_ALL)

        break

    # continue reasoning
    messages.append({
        "role": "user",
        "content": "Continue reasoning"
    })


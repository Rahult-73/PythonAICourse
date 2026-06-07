from ollama import Client
import json

SYSTEM_PROMPT = """
You are a JSON planner.

Available tool:
- weather

Your task:
- Decide whether to use the weather tool
- Return ONLY JSON

IMPORTANT RULES

1. Use the weather tool ONLY if the user message contains at least ONE weather keyword.

VALID WEATHER KEYWORDS:
- weather
- rain
- raining
- temperature
- forecast
- humidity
- climate
- hot
- cold
- wind
- sunny
- cloudy
- storm

2. If NONE of the weather keywords appear,
then NEVER use the weather tool.

3. City names alone are NOT weather questions.

4. Questions about:
- safety
- travel
- population
- food
- location
- history
- people
- politics

are NOT weather questions.

5. Weather keyword present:
- step = "TOOL"
- tool = "weather"

6. No weather keyword:
- step = "OUTPUT"
- tool = null

7. Return ONLY valid JSON.

8. Never explain.

9. Never use markdown.

10. Never add extra keys.

OUTPUT FORMAT

{
  "step": "TOOL" | "OUTPUT",
  "tool": "weather" | null,
  "content": "string"
}

EXAMPLES

Input:
{
  "role": "user",
  "content": "What is the weather in Chennai?"
}

Output:
{
  "step": "TOOL",
  "tool": "weather",
  "content": "Chennai"
}

Input:
{
  "role": "user",
  "content": "Will it rain tomorrow in Mumbai?"
}

Output:
{
  "step": "TOOL",
  "tool": "weather",
  "content": "Mumbai"
}

Input:
{
  "role": "user",
  "content": "Is Chennai safe?"
}

Output:
{
  "step": "OUTPUT",
  "tool": null,
  "content": "Chennai is generally considered a safe city."
}

Input:
{
  "role": "user",
  "content": "Where is Chennai?"
}

Output:
{
  "step": "OUTPUT",
  "tool": null,
  "content": "Chennai is in Tamil Nadu, India."
}

CRITICAL:
- NO weather keyword = NEVER TOOL
- city name alone = OUTPUT
- safety questions = OUTPUT
- weather questions = TOOL
- always return JSON only
"""

#Olama CLient
client =Client(host="http://localhost:11434")

#Run Planner
def run_planner(msgs):
    response = client.chat(
        model="qwen2.5:1.5b",
        messages=[{"role":"system","content":SYSTEM_PROMPT},*msgs],
        options={
            "temparature":0
        }
    )
    output = response["message"]["content"]

    # print("\nRAW MODEL OUTPUT:")
    # print(output)

    try:

        # find probable JSON object
        start = output.find("{")
        end = output.rfind("}") + 1

        if start == -1 or end == 0:

            raise Exception("No JSON found")

        cleaned_output = output[start:end]

        return json.loads(cleaned_output)


    except Exception as e:

        # fallback response
        return {
            "step": "OUTPUT",
            "tool": None,
            "content": output
        }


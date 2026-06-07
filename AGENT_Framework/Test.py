from planner import run_planner

messages = [
{
"role": "user",
"content": "Wht is the climate in delhi now"
}
]
runplan = run_planner(messages)
print(runplan)
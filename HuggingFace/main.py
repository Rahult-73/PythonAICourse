from transformers import pipeline
from transformers.utils import logging

logging.set_verbosity_error()

pipe = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-135M-Instruct"
)

messages = [
    {"role": "user", "content": "Who are you?"}
]

output = pipe(
    messages,
    max_new_tokens=50,
    return_full_text=False
)

print(output[0]["generated_text"])
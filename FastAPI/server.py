from fastapi import FastAPI, Body
from ollama import Client
app=FastAPI()

#Local Ollama upda nd runnin in this port
client = Client(host="http://localhost:11434")

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/contact")
def read_contact():
    return{"email":"rt2@gmail.com"}

@app.post("/chat")
def chat(message: str = Body(..., description="message")):
    response=client.chat(
        model="tinyllama:latest",
        messages=[{"role":"user","content":message}]
    )
    return {"response":response.message.content}
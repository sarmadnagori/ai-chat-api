from fastapi import FastAPI
from pydantic import BaseModel
import requests
from savestorage import save_chat,load_chat


app = FastAPI()

class Message(BaseModel):
    text: str
    conversation_id: str

conversations=load_chat()


def ask_model(history):
    try:
        response = requests.post("http://localhost:11434/api/chat", json={
            "model": "llama3.2",
            "messages":history,
            "stream": False
        })
        return response.json()["message"]["content"]
    except Exception:
        return "Could not reach Ollama — is the server running?"


@app.post("/chat")

def chat(message: Message):
    history = conversations.get(message.conversation_id, [])   
    history.append({"role": "user", "content": message.text})
    reply = ask_model(history)                                  
    history.append({"role": "assistant", "content": reply})
    conversations[message.conversation_id] = history            
    save_chat(conversations)
    return {"reply": reply}


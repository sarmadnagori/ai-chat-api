import json
from json import JSONDecodeError


def save_chat(conversations):
    with open("chat.json", "w") as f:
        json.dump(conversations, f)


def load_chat():
    try:
        with open("chat.json", "r") as f:
            conversations = json.load(f)
            return conversations
           
            
    except (FileNotFoundError, JSONDecodeError):
    
        return {}

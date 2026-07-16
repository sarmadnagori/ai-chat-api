# AI Chat API

A REST API that provides conversational AI with persistent memory, built with FastAPI and Ollama.

## Features

- Chat with a local LLM (llama3.2) over HTTP
- Conversation memory — the model remembers earlier messages
- Multiple separate conversations, isolated by conversation ID
- History persists to disk (survives server restarts)

## Tech Stack

- **FastAPI** — web framework
- **Ollama** — local LLM runtime (llama3.2)
- **Pydantic** — request validation

## Setup

1. Install [Ollama](https://ollama.com) and pull the model:
ollama pull llama3.2
2. Install dependencies:
pip install fastapi uvicorn requests
3. Run the server:
python3 -m uvicorn main:app --reload

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat` | Send a message, get an AI reply |

**Request body:**
```json
{
  "text": "my name is Ali",
  "conversation_id": "a"
}
```

Messages sharing a `conversation_id` form one conversation with shared memory. Different IDs are fully separate.
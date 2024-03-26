from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# 共用函數處理回應
def generate_response(user_message: str) -> str:
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "你好": "早安你好",
    }
    return responses.get(user_message.lower().strip(), "Sorry, I don't understand that.")

@app.get("/")
async def root(name: str = Query(None, description="What's your name?")):
    welcome_message = "立宇你好呀！從今天開始我就是你的可愛女友了"
    if name:
        welcome_message += f"，{name}"
    welcome_message += "，你叫什麼名字呀？"
    return {"message": welcome_message}

@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    return {"response": generate_response(chat_request.message)}

@app.get("/chat_get/")
async def chat_get(message: str = Query(None, description="Enter your message")):
    return {"response": generate_response(message)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

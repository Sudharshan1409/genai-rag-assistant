from fastapi import APIRouter

from utils.db import GenAIRag
from utils.request_formats import ChatCreateRequest

session_router = APIRouter(prefix="/session", tags=["chat"])
db = GenAIRag()


@session_router.post("/create", status_code=201)
def create_chat(payload: ChatCreateRequest):
    chat_id = db.createChat(payload.name)

    return {
        "chat_id": chat_id,
        "message": "Chat created successfully",
    }


@session_router.get("/list", status_code=200)
def list_chat():
    chats = db.listChats()
    return {"message": "Chats fetched successfully", "chats": chats}

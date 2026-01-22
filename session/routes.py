import uuid
from datetime import datetime

from fastapi import APIRouter

from utils.db import GenAIRag
from utils.requestFormats import ChatCreateRequest

router = APIRouter(prefix="/chat", tags=["chat"])
db = GenAIRag()


@router.post("/create", status_code=201)
def create_chat(payload: ChatCreateRequest):
    chat_id = str(uuid.uuid4())

    db.cursor.execute(
        """
        INSERT INTO chats (id, name, created_at)
        VALUES (?, ?, ?)
        """,
        (chat_id, payload.name, datetime.now().isoformat()),
    )

    db.connection.commit()

    return {
        "chat_id": chat_id,
        "message": "Chat created successfully",
    }


@router.get("/list", status_code=200)
def list_chat():
    cursor = db.cursor.execute("SELECT * FROM chats")
    chats = cursor.fetchall()
    print(chats)
    return chats

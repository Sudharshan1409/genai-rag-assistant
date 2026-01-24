from pydantic import BaseModel


class ChatCreateRequest(BaseModel):
    name: str


class QuestionRequest(BaseModel):
    question: str

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from ollama import chat
from pydantic import BaseModel

app = FastAPI(title="GenAI RAG Assistant")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health_check():
    return {"status": "ok"}


def stream_answer(question: str):
    stream = chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        stream=True,
    )

    for chunk in stream:
        if chunk.get("message") and chunk["message"].get("content"):
            yield chunk["message"]["content"]


@app.post("/ask")
def ask_question(payload: QuestionRequest):
    return StreamingResponse(stream_answer(payload.question), media_type="text/plain")

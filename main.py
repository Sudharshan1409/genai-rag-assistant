from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from session.routes import session_router
from utils.basic import stream_answer
from utils.request_formats import QuestionRequest

app = FastAPI(title="GenAI RAG Assistant")


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(payload: QuestionRequest):
    return StreamingResponse(
        stream_answer(payload.question),
        media_type="text/plain",
    )


# 🔑 THIS IS THE IMPORTANT LINE
app.include_router(session_router)

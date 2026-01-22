from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from session.routes import router as chat_router
from utils.basic import stream_answer
from utils.requestFormats import QuestionRequest

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
app.include_router(chat_router)

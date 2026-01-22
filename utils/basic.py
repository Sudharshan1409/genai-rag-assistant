from ollama import chat


def stream_answer(question: str):
    stream = chat(
        model="llama3.1",
        messages=[{"role": "user", "content": question}],
        stream=True,
    )

    for chunk in stream:
        if chunk.get("message") and chunk["message"].get("content"):
            yield chunk["message"]["content"]

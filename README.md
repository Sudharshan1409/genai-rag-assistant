# GenAI RAG Assistant (Local, Free Stack)

This project is a **local-first Retrieval Augmented Generation (RAG) assistant** built using open-source tools.
It demonstrates how to store text as embeddings in a vector database (FAISS) and retrieve relevant context using semantic similarity.

No paid APIs.
No cloud dependency.
Everything runs locally.

---

## ✨ What This Project Demonstrates

- How text is converted into **embeddings**
- How embeddings are stored in **FAISS**
- How user queries are embedded and matched semantically
- How vector search differs from keyword search
- How this forms the foundation of **RAG systems**

This project is intentionally minimal and educational.

---

## 🧠 Core Concepts

### 1. Embeddings
Text is converted into high-dimensional numerical vectors using a sentence transformer model.

Example:
```
"AWS Lambda allows you to run code without managing servers"
→ [0.12, -0.98, 0.44, ...]
```

### 2. Vector Database (FAISS)
FAISS stores **only vectors**, not text.
It performs fast similarity search to find the closest vectors to a query.

### 3. Retrieval Flow
```
Documents → Embeddings → FAISS
Query → Embedding → Similarity Search → Relevant Documents
```

---

## 🧰 Tech Stack (100% Free)

- Python
- LangChain
- FAISS (local vector database)
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FastAPI (API layer)
- Ollama (local LLM runtime)

---

## 📁 Project Structure (Simplified)

```
genai-rag-assistant/
├── vector_test.py        # FAISS + embedding example
├── data/                # Documents (future use)
├── vector_store/         # Saved FAISS index (future use)
├── venv/
└── README.md
```

---

## 🚀 Example: Vector Search with FAISS

The current example:
- Creates multiple documents
- Converts them into embeddings
- Stores them in FAISS
- Runs semantic similarity search on user input

Example query:
```
What is serverless computing?
```

Expected result:
- Documents related to AWS Lambda and serverless architecture
- Not exact keyword matches, but **semantic relevance**

---

## 🔍 Why FAISS?

- Extremely fast similarity search
- Runs fully in-process
- No server or setup required
- Industry-accepted for RAG systems

FAISS does **not**:
- Understand text
- Store metadata natively
- Act like a traditional database

---

## 🧭 Future Improvements

- Document ingestion from PDFs
- Metadata-based filtering (session/user scoped search)
- RAG answer generation using Ollama
- Streaming responses via FastAPI
- Saving and loading FAISS indexes

---

## 🎯 Goal

This repository is designed as a **learning-first GenAI project** to deeply understand how RAG systems work under the hood before moving to production-grade tools.

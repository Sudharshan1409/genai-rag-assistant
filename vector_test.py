from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    Document(
        page_content="AWS Lambda allows you to run code without managing servers.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="AWS EC2 provides virtual machines that you manage yourself.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Serverless architecture removes the need to provision infrastructure.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="FAISS enables fast similarity search over high-dimensional vectors.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Vector databases store embeddings for semantic search.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Cosine similarity is commonly used to compare text embeddings.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Retrieval Augmented Generation combines search with language models.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="RAG reduces hallucinations by grounding answers in documents.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Large Language Models generate text by predicting the next token.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Embeddings convert text into numerical vector representations.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Sentence transformers are popular models for generating embeddings.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Chunking documents improves retrieval accuracy in RAG systems.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="FastAPI is a Python framework for building APIs quickly.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Streaming responses allow tokens to be sent as they are generated.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Ollama runs large language models locally on your machine.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Local LLMs help reduce cost and improve data privacy.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Similarity search finds the most relevant documents for a query.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Vector search is different from traditional keyword search.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Metadata can be attached to documents for filtering results.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Production RAG systems often use hybrid search techniques.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="PostgreSQL with pgvector can be used as a vector database.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="FAISS is optimized for fast nearest neighbor search.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Embeddings capture semantic meaning rather than exact words.",
        metadata={
            "session_id": "chat_123",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="AWS is awesome",
        metadata={
            "session_id": "chat_321",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
    Document(
        page_content="Serverless is my thing",
        metadata={
            "session_id": "chat_321",
            "source": "aws_docs",
            "user_id": "sudharshan",
        },
    ),
]

vector_store = FAISS.from_documents(documents, embeddings)

query = input("Enter the query: ")
results = vector_store.similarity_search(query, k=3, filter={"session_id": "chat_123"})

for doc in results:
    print(doc.page_content)

import sqlite3


class GenAIRag:
    def __init__(self):
        self.connection = sqlite3.connect("genai.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        # Enable foreign keys (IMPORTANT)
        self.cursor.execute("PRAGMA foreign_keys = ON;")

        # Chats table
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS chats (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )

        # Messages table
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                chat_id TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('USER', 'ASSISTANT')),
                content TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (chat_id) REFERENCES chats(id)
            )
            """
        )

        self.connection.commit()

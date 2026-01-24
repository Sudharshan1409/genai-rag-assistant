import sqlite3
import uuid
from datetime import datetime


class GenAIRag:
    connection = sqlite3.connect("genai.db", check_same_thread=False)
    cursor = connection.cursor()

    def __init__(self):
        # Enable foreign keys (IMPORTANT)
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self.connection.commit()
        self.__init_chats_table()
        self.__init_messages_table()

    def __init_chats_table(self):
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

        # Index for Chats table
        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_chats_created_at
            ON chats (created_at);
            """
        )

    def __init_messages_table(self):
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

        # Index for Messages table
        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_messages_created_at
            ON messages (created_at);
            """
        )

        self.cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_messages_chat_time
            ON messages (chat_id, created_at);
            """
        )

    def createChat(self, name):
        chat_id = str(uuid.uuid4())
        current_time = datetime.now().isoformat()

        self.cursor.execute(
            """
            INSERT INTO chats (id, name, created_at)
            VALUES (?, ?, ?)
            """,
            (chat_id, name, current_time),
        )

        self.connection.commit()
        return chat_id

    def listChats(self):
        cursor = self.cursor.execute("SELECT * FROM chats")
        chats = cursor.fetchall()
        return chats

    def createMessage(self, chat_id, role, content):
        message_id = str(uuid.uuid4())
        current_time = datetime.now().isoformat()

        self.cursor.execute(
            """
            INSERT INTO messages (id, chat_id, role, content, created_at)
            VALUES(?, ?, ?, ?, ?)
            """,
            (message_id, chat_id, role, content, current_time),
        )

        return message_id

    def listMessages(self, chat_id):
        self.cursor.execute(
            """
            SELECT * FROM messages where chat_id = ?
            """,
            chat_id,
        )

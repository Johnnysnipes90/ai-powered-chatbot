from sqlalchemy import Column, Integer, String, DateTime, func
from .db import Base

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), index=True)  # Define max length
    message = Column(String(500))  # Increased length to store long messages
    response = Column(String(500))  # Increased length for chatbot responses
    timestamp = Column(DateTime, server_default=func.now(), index=True)  # More efficient timestamp indexing
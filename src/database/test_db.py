from src.database.db import get_db 
from src.database.models import ChatMessage 

db = next(get_db())

# Test inserting a chat message
new_message = ChatMessage(user_id="123", message="Hello, bot!", response="Hello, user!")
db.add(new_message)
db.commit()

# Test retrieving messages
messages = db.query(ChatMessage).all()
for msg in messages:
    print(msg.message, "=>", msg.response)
from pydantic import BaseModel
from src.models.user import User
from src.models.message import Message

class Chat(BaseModel):
    name: str
    participants: list[User]
    messages: list[Message]
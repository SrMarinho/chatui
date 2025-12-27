from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Container, Vertical
from src.models.chat import Chat

class ChatItem(Widget):
    def __init__(self, chat: Chat) -> None:
        super().__init__()
        self.chat = chat
    
    def compose(self) -> ComposeResult:
        with Container():
            with Vertical():
                yield Label(self.chat.name, id="chat_name")
            
                yield Label(self.chat.messages[-1].content if self.chat.messages else "No messages yet.", id="last_message")
            
            yield Label(self.chat.messages[-1].timestamp if self.chat.messages else "", id="timestamp") 

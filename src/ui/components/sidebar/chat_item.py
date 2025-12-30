from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Container, Vertical
from src.models.chat import Chat

class ChatItem(Widget):
    DEFAULT_CSS = """
        .chat_item_container {
            height: 6;
            border: outer $background;
            background: $background;
        }
        #last_message {
            color: $text-muted;
        }
    """
    def __init__(self, chat: Chat, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.chat = chat
    
    def compose(self) -> ComposeResult:
        with Container(classes="chat_item_container"):
            with Vertical():
                yield Label(self.chat.name, id="chat_name")
            
                yield Label(self.chat.messages[-1].content if self.chat.messages else "No messages yet.", id="last_message")
            
            yield Label(self.chat.messages[-1].timestamp if self.chat.messages else "", id="timestamp") 

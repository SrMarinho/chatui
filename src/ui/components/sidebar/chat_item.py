from datetime import datetime, timedelta
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Container, Vertical, Horizontal
from src.models.chat import Chat

class ChatItem(Widget):
    DEFAULT_CSS = """
        .chat_item_container {
            height: 6;
            border: solid $foreground;
            background: $background;
        }
        #chat_content {
            width: 80%;
        }
        #chat_info {
            width: 20%;
            background: blue;
            align: center middle;
            content-align: center middle;
        }
        #last_message {
            color: $text-muted;
        }
    """
    def __init__(self, chat: Chat, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.chat = chat
    
    def compose(self) -> ComposeResult:
        with Horizontal(classes="chat_item_container"):
            with Container():
                with Vertical(id="chat_content"):
                    yield Label(self.chat.name, id="chat_name")
                
                    yield Label(self.chat.messages[-1].content if self.chat.messages else "No messages yet.", id="last_message")
            with Container(id="chat_info"):
                if date := datetime.fromisoformat(self.chat.messages[-1].timestamp):
                    today = datetime.now()
                    yesterday = datetime.now() - timedelta(days=1)

                    if date.date() == today.date():
                        yield Label(str(date.strftime("%H:%M")), id="timestamp")
                    elif date.date() == yesterday.date():
                        yield Label("Yesterday", id="timestamp") 
                    else:
                        yield Label(str(date.date()) if self.chat.messages else "", id="timestamp") 
                else:
                    yield Label("" if self.chat.messages else "", id="timestamp") 
                
                yield Label(str(1), id="notification")
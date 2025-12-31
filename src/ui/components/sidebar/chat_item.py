from typing import Callable
from datetime import datetime, timedelta
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Vertical, Horizontal
from textual.events import Click
from textual.message import Message
from src.models.chat import Chat

class ChatItem(Widget):
    class Selected(Message):
        def __init__(self, chat: Chat):
            self.chat = chat
            super().__init__()

    DEFAULT_CSS = """
        .chat_item_container {
            width: 100%;
            height: 4;
            border: solid $primary;
            background: transparent;
        }

        #chat_name {
            height: 1fr;
            width: 1fr;
        }

        #last_message {
            height: 1fr;
            width: 1fr;
            color: $text-muted;
            content-align: left bottom;
        }

        #chat_content {
            width: 4fr;
            height: 1fr;
        }

        #chat_info {
            width: 1fr;
            height: 1fr;
        }

        #timestamp {
            width: 100%;
            height: 1fr;
            content-align: right top;
            color: $accent;
        }

        #notification {
            width: 100%;
            height: 1fr;
            content-align: right bottom;
            color: $accent;
        }
    """
    def __init__(self, chat: Chat, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.chat = chat
    
    def compose(self) -> ComposeResult:
        with Horizontal(classes="chat_item_container"):
            with Vertical(id="chat_content"):
                yield Label(self.chat.name, id="chat_name")
                yield Label(self.chat.messages[-1].content if self.chat.messages else "No messages yet.", id="last_message")

            with Vertical(id="chat_info"):
                if date := datetime.fromisoformat(self.chat.messages[-1].timestamp):
                    today = datetime.now()
                    yesterday = datetime.now() - timedelta(days=1)

                    if date.date() == today.date():
                        # yield Label("Yesterday", id="timestamp") 
                        yield Label(str(date.strftime("%H:%M")), id="timestamp")
                    elif date.date() == yesterday.date():
                        yield Label("Yesterday", id="timestamp") 
                    else:
                        yield Label(str(date.date()) if self.chat.messages else "", id="timestamp") 
                else:
                    yield Label("" if self.chat.messages else "", id="timestamp") 
                
                yield Label(str(1), id="notification")
    
    def on_click(self, event: Click):
        self.post_message(ChatItem.Selected(self.chat))

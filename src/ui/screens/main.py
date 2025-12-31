from typing import AsyncGenerator
from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal
from textual.reactive import reactive
from textual import getters
from src.ui.components.chat.chat_view import ChatView
from src.ui.components.sidebar.sidebar import Sidebar
from src.models.chat import Chat
from src.models.user import User
from src.models.message import Message
from datetime import datetime


class MainScreen(Screen):
    """Main screen class."""
    DEFAULT_CSS = """
        #sidebar {
            width: 25%;
            background: $panel;
        }
    """
    chats: reactive[list[Chat]] = reactive([])
    current_chat = None

    def compose(self) -> ComposeResult:
        """Compose the main screen UI components."""
        with Horizontal():
            yield Sidebar(id="sidebar")
    
    def on_mount(self):
        temp_chats: list[Chat] = []
        for chat in self._get_chats():
            temp_chats.append(chat)
        self.chats = temp_chats
    
    def watch_chats(self, old_chats: list[Chat], new_chats: list[Chat]) -> None:
        """Watch for changes in the chats reactive variable."""
        sidebar = self.query_one("#sidebar", Sidebar)
        sidebar.chats = new_chats
        self.notify(f"Chats updated: {len(new_chats)} chats available.")
    
    def _get_chats(self):
        user1 = User(username="DefaultUser")
        for chat in range(5):
            user2 = User(username=f"Usurário {str(chat)}")
            message1 = Message(sender=user1.username, content="Hello", timestamp=str(datetime.now())) 
            message2 = Message(sender=user2.username, content="Hi! How are you?", timestamp=str(datetime.now()))
            yield Chat(
                name=f"Chat {chat}",
                participants=[user1, user2],
                messages=[message1, message2]
            )
    
    def on_chat_item_selected(self, selected):
        self.current_chat = selected.chat
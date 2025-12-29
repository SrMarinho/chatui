from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal
from textual.reactive import reactive
from src.ui.components.chat.chat_view import ChatView
from src.ui.components.sidebar.sidebar import Sidebar
from src.models.chat import Chat
from src.models.user import User
from src.models.message import Message
from datetime import datetime


class MainScreen(Screen):
    """Main screen class."""
    DEFAULT_CSS = """
        Sidebar {
            width: 25%;
            background: $panel;
        }
    """
    chats: reactive[list[Chat]] = reactive([])
    current_chat = None

    
    def compose(self) -> ComposeResult:
        """Compose the main screen UI components."""
        with Horizontal():
            yield Sidebar(id="sidebar", chats=self.chats)
            if self.current_chat:
                yield ChatView(chat=self.current_chat, id="chat_view")
    
    def on_mount(self):
        user1 = User(username="alice")
        temp_chats = []
        for chat in range(5):
            user2 = User(username=f"Usurário {str(chat)}")
            message1 = Message(sender=user1.username, content="Hello", timestamp=str(datetime.now())) 
            message2 = Message(sender=user2.username, content="Hi! How are you?", timestamp=str(datetime.now()))
            temp_chats.append(
                Chat(
                    name=f"Chat {chat}",
                    participants=[user1, user2],
                    messages=[message1, message2]
                )
            )
        self.chats = temp_chats
    
    def watch_chats(self, old_chats: list[Chat], new_chats: list[Chat]) -> None:
        """Watch for changes in the chats list."""
        try:
            sidebar = self.query("#sidebar").first()
            sidebar.chats = new_chats
        except Exception as e:
            self.notify(f"Error updating sidebar chats: {e}", severity="error")
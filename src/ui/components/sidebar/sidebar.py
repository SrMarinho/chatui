import logging
from textual.app import ComposeResult
from textual.widgets import Label
from textual.widget import Widget
from textual.message import Message
from src.ui.components.sidebar.chat_item import ChatItem
from src.models.chat import Chat


class Sidebar(Widget):
    """Sidebar component for the UI."""
    def __init__(self, chats: list[Chat], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.chats = chats
        self.current_chat = None
    
    def compose(self) -> ComposeResult:
        """Compose the sidebar UI components."""
        logging.info("Composing Sidebar with chats.")
        for chat in list(self.chats):
            yield Label("Chats", id="sidebar_title")
            yield ChatItem(chat)
    
    def on_mount(self):
        self.notify(f"Sidebar mounted with {len(self.chats)} chats.")

    def on_chat_item_selected(self) -> None:
        """Handle chat item selection events."""
        self.post_message(self.ChatSelected(self.current_chat))

from textual.app import ComposeResult
from textual.widget import Widget
from src.ui.components.sidebar.chat_item import ChatItem


class Sidebar(Widget):
    """Sidebar component for the UI."""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.chats = []
    
    def compose(self) -> ComposeResult:
        """Compose the sidebar UI components."""
        for chat in self.chats:
            yield ChatItem(chat)
    
    def on_mount(self):
        self.chats = []

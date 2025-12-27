from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal
from src.ui.components.chat.chat_view import ChatView
from src.ui.components.sidebar.sidebar import Sidebar


class MainScreen(Screen):
    """Main screen class."""
    DEFAULT_CSS = """
        Sidebar {
            width: 25%;
            background: $panel;
        }
    """
    def __init__(self):
        super().__init__()
    
    def compose(self) -> ComposeResult:
        """Compose the main screen UI components."""
        with Horizontal():
            yield Sidebar(id="sidebar")
            yield ChatView()
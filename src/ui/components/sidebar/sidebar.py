import logging
from textual.app import ComposeResult
from textual.widgets import Label, Input
from textual.widget import Widget
from textual.reactive import reactive
from textual.containers import VerticalScroll
from src.ui.components.sidebar.chat_item import ChatItem
from src.models.chat import Chat


class Sidebar(Widget):
    DEFAULT_CSS = """
        #chats_container > * {
            height: 6;
        }
    """
    """Sidebar component for the UI."""
    # Remova o setter customizado e use reactive diretamente
    chats: reactive[list[Chat]] = reactive([])
    current_chat = reactive(None)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def compose(self) -> ComposeResult:
        """Compose the sidebar UI components."""
        self.notify("Composing Sidebar with chats.")
        
        yield Label("Chats", id="sidebar_title")
        yield Input(placeholder="Search chats...", id="chat_search_input")
        with VerticalScroll(id="chats_container"):
            ...
    
    def on_mount(self):
        """Handle mount events."""
        # Carregue os chats iniciais se houver
        if self.chats:
            self.load_chats()

    def watch_chats(self, old_chats: list[Chat], new_chats: list[Chat]) -> None:
        """Watch for changes in the chats list."""
        self.notify(f"Sidebar detected chat list change: {len(old_chats)} -> {len(new_chats)}")
        self.load_chats()
    
    def load_chats(self) -> None:
        """Load chats into the sidebar."""
        chats_container = self.query_one("#chats_container", VerticalScroll)
        
        # Limpe o container
        chats_container.remove_children()
        
        # Adicione os novos chats
        for index, chat in enumerate(self.chats):
            self.notify(f"Loading chat item: {chat.name}")
            chats_container.mount(ChatItem(chat, id=f"chat_item_{index}"))
        
        # Se necessário, force um refresh
        self.refresh()
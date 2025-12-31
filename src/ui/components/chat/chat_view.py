from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Static, Label, Input, Button
from textual.containers import VerticalScroll, HorizontalGroup
from src.models.message import Message
from src.models.chat import Chat


class ChatView(Widget):
    """Chat view component for displaying messages."""
    DEFAULT_CSS = """
        #message_input {
            width: 1fr;
        }
    """

    def __init__(self, chat: Chat, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.current_text = ""
        self.messages: list[Message] = []
    
    def compose(self) -> ComposeResult:
        """Compose the chat view UI components."""
        yield Label("Chat View", id="chat_view_title")
        with VerticalScroll(id="messages_container"):
            for message in self.messages:
                yield Static(message.content)
        with HorizontalGroup(id="message_input_container"):
            yield Input(placeholder="Type your message here...", id="message_input")
            yield Button("Send", id="send_button", disabled=True)
    
    def on_mount(self):
        message_input = self.query_one("#message_input", Input)
        message_input.focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input change events."""
        self.current_text = event.value
        send_button = self.query_one("#send_button", Button)
        send_button.disabled = len(self.current_text.strip()) == 0
        send_button.variant = "primary" if not send_button.disabled else "default"
    
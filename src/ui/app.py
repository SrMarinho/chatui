from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from src.ui.screens.main import MainScreen

class MainApp(App):
    """Main application class."""
    SCREENS = {
        "main": MainScreen,
    }

    def __init__(self):
        super().__init__()
    
    def compose(self) -> ComposeResult:
        """Compose the UI components."""
        yield Header()
        yield Footer()
    
    def on_mount(self):
        """Actions to perform when the app is mounted."""
        self.theme = "textual-dark"
        self.push_screen("main")

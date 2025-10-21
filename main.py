import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

# Proxy state (enabled / disabled)
proxy_enabled = True

# Proxy settings
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 8808

class SearchLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chrome Search")
        self.resize(600, 128)

        layout = QVBoxLayout()

        # Label
        self.label = QLabel("Type what you want to search on Google:")
        layout.addWidget(self.label)

        # Input field
        self.input = QLineEdit()
        self.input.setPlaceholderText("Type your search here...")
        layout.addWidget(self.input)

        # Search button
        self.search_button = QPushButton("Search in Chrome")
        self.search_button.clicked.connect(self.open_chrome)
        layout.addWidget(self.search_button)

        # Proxy control button
        self.proxy_button = QPushButton("Disable Proxy" if proxy_enabled else "Enable Proxy")
        self.proxy_button.clicked.connect(self.toggle_proxy)
        layout.addWidget(self.proxy_button)

        self.setLayout(layout)

    def open_chrome(self):
        query = self.input.text()
        if query:
            cmd = ["google-chrome", f"https://www.google.com/search?q={query}"]
            if proxy_enabled:
                cmd.append(f"--proxy-server=http://{PROXY_HOST}:{PROXY_PORT}")
            subprocess.Popen(cmd)

    def toggle_proxy(self):
        global proxy_enabled
        proxy_enabled = not proxy_enabled
        self.proxy_button.setText(f"{'Disable' if proxy_enabled else 'Enable'} Proxy")

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchLauncher()
    window.show()
    sys.exit(app.exec_())

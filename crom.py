import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineCore import QWebEngineProfile

# Proxy state
proxy_enabled = True
PROXY_HOST = "127.0.0.1"
PROXY_PORT = 8808

class MiniChrome(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Chrome with Proxy")
        self.resize(1000, 700)

        layout = QVBoxLayout()

        # URL / Search bar
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Type URL or search query...")
        layout.addWidget(self.url_input)

        # Buttons: Go, Back, Forward, Refresh
        btn_layout = QHBoxLayout()
        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate)
        btn_layout.addWidget(self.go_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(lambda: self.browser.back())
        btn_layout.addWidget(self.back_button)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(lambda: self.browser.forward())
        btn_layout.addWidget(self.forward_button)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(lambda: self.browser.reload())
        btn_layout.addWidget(self.refresh_button)

        # Proxy toggle button
        self.proxy_button = QPushButton("Disable Proxy" if proxy_enabled else "Enable Proxy")
        self.proxy_button.clicked.connect(self.toggle_proxy)
        btn_layout.addWidget(self.proxy_button)

        layout.addLayout(btn_layout)

        # Web view
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # Set layout
        self.setLayout(layout)

        # Configure profile for proxy
        self.profile = QWebEngineProfile.defaultProfile()
        self.set_proxy()

    def set_proxy(self):
        global proxy_enabled
        if proxy_enabled:
            proxy_str = f"http://{PROXY_HOST}:{PROXY_PORT}"
            self.profile.setHttpProxy(proxy_str)
        else:
            self.profile.setHttpProxy("")

    def navigate(self):
        text = self.url_input.text().strip()
        if text:
            if not (text.startswith("http://") or text.startswith("https://")):
                # إذا لم يكن رابط كامل، اعتبره بحث على جوجل
                text = f"https://www.google.com/search?q={text}"
            self.browser.load(text)

    def toggle_proxy(self):
        global proxy_enabled
        proxy_enabled = not proxy_enabled
        self.proxy_button.setText(f"{'Disable' if proxy_enabled else 'Enable'} Proxy")
        self.set_proxy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniChrome()
    window.show()
    sys.exit(app.exec_())

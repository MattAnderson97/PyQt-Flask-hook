from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flask hook")
        self.web_engine_view = QWebEngineView()
        self.web_engine_view.setUrl(QUrl("http://127.0.0.1:5000"))
        self.web_engine_view.reload()
        self.setCentralWidget(self.web_engine_view)

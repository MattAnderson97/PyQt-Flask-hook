from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, port):
        super().__init__()
        self.setWindowTitle("Flask hook")

        self.web_engine_view = QWebEngineView()
        self.web_engine_view.setUrl(QUrl("http://127.0.0.1:{}".format(port)))
        self.web_engine_view.reload()

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.web_engine_view)
        self.main_layout.setContentsMargins(5, 40, 5, 5)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.central_widget)

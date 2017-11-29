from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget


# Create new window
class MainWindow(QMainWindow):
    """Main window for the GUI - displays flask webpage"""

    # constructor
    def __init__(self, port):
        # call parent constructor
        # hide window border
        super().__init__(flags=Qt.FramelessWindowHint)
        # window name
        self.setWindowTitle("Flask hook")

        # create view for web page
        self.web_engine_view = QWebEngineView()
        # load flask page
        self.web_engine_view.setUrl(QUrl("http://127.0.0.1:{}".format(port)))
        # update view
        self.web_engine_view.reload()

        # create main layout
        self.main_layout = QVBoxLayout()
        # add web view to layout
        self.main_layout.addWidget(self.web_engine_view)
        # self.main_layout.setContentsMargins(5, 40, 5, 5)
        # clear margins
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # create main widget
        self.central_widget = QWidget()
        # apply layout to main widget
        self.central_widget.setLayout(self.main_layout)

        # apply main widget to window
        self.setCentralWidget(self.central_widget)

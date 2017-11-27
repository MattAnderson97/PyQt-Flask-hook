from PyQt5.QtWidgets import QApplication

import sys
import threading

from UI.MainWindow import MainWindow
from Flask.app import app


class FlaskThread(threading.Thread):
    def __init__(self, threadID, name, port=5000):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.port = port

    def run(self):
        print("Starting " + self.name)
        app.run(port=self.port)
        print("Exiting thread " + self.name)


class UIThread(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    def run(self):
        print("Starting thread " + self.name)
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        window.raise_()
        app.exec_()
        print("Exiting thread " + self.name)


if __name__ == "__main__":
    flaskThread = FlaskThread(1, "flaskThread")
    uiThread = UIThread(2, "uiThread")
    flaskThread.start()
    uiThread.start()
    print("Exiting main thread")

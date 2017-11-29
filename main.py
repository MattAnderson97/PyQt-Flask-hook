from PyQt5.QtWidgets import QApplication

import sys
import threading

from UI.MainWindow import MainWindow
from Flask.app import app


# create new thread for flask application
class FlaskThread(threading.Thread):
    """Thread for flask application"""

    # constructor
    # takes threadid, thread name and port (Default: 5000)
    def __init__(self, threadID, name, port=5000):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.port = port

    # override run() method in parent class
    def run(self):
        print("Starting " + self.name)
        # start flask with the given port
        app.run(port=self.port)
        print("Exiting thread " + self.name)


# create new thread for GUI
class UIThread(threading.Thread):
    """Thread for the GUI"""

    # constructor
    # takes thread id, thread name and port (Default: 5000)
    def __init__(self, id, name, port=5000):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name
        self.port = port

    # override run() method in parent class
    def run(self):
        print("Starting thread " + self.name)
        # instantiate QApplication for PyQt framework
        app = QApplication(sys.argv)
        # instantiate main window
        window = MainWindow(self.port)
        # show the main window
        window.show()
        # bring the main window to the front
        window.raise_()
        # execute the application - start watching for events etc.
        app.exec_()
        print("Exiting thread " + self.name)


# constant value for the port of the flask application
PORT = 5000


# make sure this is the main program that is launched
if __name__ == "__main__":
    # instantiate thread for flask
    flaskThread = FlaskThread(1, "flaskThread", PORT)
    # instantiate thread for gui
    uiThread = UIThread(2, "uiThread", PORT)
    # start flask thread
    flaskThread.start()
    # start gui thread
    uiThread.start()

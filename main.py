import sys
import signal
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication
from qtapp.model import Model
from qtapp.view import View


class Controller:
    def __init__(self):
        self.qt_app = QApplication(sys.argv)
        self.model = Model()
        self.view = View()
        self.view.button.clicked.connect(self.update_model)
        self.model.signal.connect(self.update_view)

        signal.signal(signal.SIGINT, self.keyboardInterruptHandler)
        self.time = QTime()
        timer = QTimer()
        timer.timeout.connect(lambda: None)
        timer.start(100)

        self.qt_app.exec()

    def update_model(self):
        self.time.start()
        self.model.setdata(self.view.getdata())

    def update_view(self):
        print("--- DONE IN {}ms ---".format(self.time.elapsed()))
        self.time.restart()
        self.view.setdata(self.model.getdata())

    def keyboardInterruptHandler(self, signal, frame):
        self.qt_app.exit()

if __name__ == "__main__":
	my_controller = Controller()

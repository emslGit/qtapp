from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):

    signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.data = None
        self.classified = "classified"

    def setdata(self, data):
        self.data = data
        self.signal.emit()

    def getdata(self):
        return self.data

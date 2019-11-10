from PyQt5.QtWidgets import *


class View(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Push button to edit.")
        self.lineedit = QLineEdit()
        self.button = QPushButton("Update")

        with open("qtapp/style.css") as style:
            self.setStyleSheet(style.read())

        wrapper = QVBoxLayout()
        wrapper.addWidget(self.label)
        wrapper.addWidget(self.lineedit)
        wrapper.addWidget(self.button)
        self.setLayout(wrapper)
        self.setWindowTitle("Title")
        self.show()

    def getdata(self):
        assert(self.lineedit.text().isalnum()), "User input must be alnum."
        return self.lineedit.text()

    def setdata(self, data):
        self.label.setText(data)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget

from color import Color

class MainWindow5(QMainWindow):
    def __init__(self):
        super(MainWindow5, self).__init__()
        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        layout.setContentsMargins(10,0,0,10)
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("yellow"))
        layout.addWidget(Color("pink"))
        layout.addWidget(Color("orange"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
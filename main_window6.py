from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction

from main_window4 import MainWindow4


class MainWindow6(QMainWindow):

    def __init__(self):
        super(MainWindow6, self).__init__()

        self.setWindowTitle("MainWindow6")
        self.setGeometry(0, 0, 600, 400)

        self.label1 = QLabel("Nome", self)
        self.label1.move(100, 200)

        self.toolbar1 = QToolBar("Toolbar1", self)
        self.addToolBar(self.toolbar1)

        self.button_action = QAction("My Action", self)
        self.button_action.setToolTip("Azione")
        self.button_action.triggered.connect(self.button_action_click)
        self.toolbar1.addAction(self.button_action)

        self.secondForm = MainWindow4()

    def button_action_click(self, s):

        print("Azione", s)
        self.label1.setText("Azione")
        self.secondForm.show()
        print('aspetta un attimo')

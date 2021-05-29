from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction, QStatusBar

from main_window4 import MainWindow4


class MainWindow6(QMainWindow):

    def __init__(self):
        super(MainWindow6, self).__init__()

        self.setWindowTitle("MainWindow6")
        self.setGeometry(0, 0, 600, 400)

        self.label1 = QLabel("Nome", self)
        self.label1.move(100, 200)

        self.toolbar1 = QToolBar("Toolbar1", self)
        self.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar1)

        self.icon1 = QIcon("/home/roberto/prg/python/test_V/img/bug.png")
        self.icon2 = QIcon("/home/roberto/prg/python/test_V/img/new.png")

        self.button_action = QAction("My Action", self)
        self.button_action.setIcon(self.icon1)
        self.button_action.setToolTip("Azione")
        self.button_action.setStatusTip("Tasto di azione")
        self.button_action.setCheckable(True)
        self.button_action.triggered.connect(self.button_action_click)
        self.button_action.toggled.connect(self.button_action_click)
        self.toolbar1.addAction(self.button_action)

        self.toolbar1.addSeparator()

        self.button_action2 = QAction("My Action2", self)
        self.button_action2.setIcon(self.icon2)
        self.button_action2.setToolTip("Azione2")
        self.button_action2.setStatusTip("Tasto di azione2")
        self.button_action2.triggered.connect(self.button_action2_click)

        self.toolbar1.addAction(self.button_action2)

        self.setStatusBar(QStatusBar(self))

        self.secondForm = MainWindow4()

    def button_action_click(self, s):

        print("Azione", s)
        if s:
            self.label1.setText("Azione")
            self.secondForm.show()
            print('aspetta un attimo')
        else:
            self.secondForm.close()

    def button_action2_click(self):

        self.close()
        self.secondForm.close()
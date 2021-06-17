from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QToolBar, QAction, QStatusBar, QPushButton, QDialog, \
    QDialogButtonBox, QVBoxLayout

from main_window4 import MainWindow4


class CustomerDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("HELLO")

        self.message = QLabel("Something happend, is that OK ?", self)

        btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(btn)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)


class MainWindow6(QMainWindow):

    def __init__(self):
        super(MainWindow6, self).__init__()

        self.setWindowTitle("MainWindow6")
        self.setGeometry(0, 0, 600, 400)

        self.label1 = QLabel("Nome", self)
        self.label1.move(100, 200)

        self.button1 = QPushButton("Press me", self)
        self.button1.move(200, 200)
        self.button1.clicked.connect(self.button1_clicked)

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
        self.button_action.setShortcut("Ctrl+n")
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

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("&File")
        self.file_menu.addAction(self.button_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.button_action2)
        self.sub_menu = self.file_menu.addMenu("Sub")
        self.sub_menu.addAction(self.button_action2)

        self.secondForm = MainWindow4(self)

    def button_action_click(self, s):

        print("Azione", s)
        if s:
            self.label1.setText("Azione")
            self.secondForm.move(600, 300)
            self.secondForm.show()
            print('aspetta un attimo')
            self.setWindowTitle("Ho aperto seconda form")
        else:
            self.secondForm.close()
            self.setWindowTitle("Ho chiuso la seconda form")

    def button_action2_click(self):

        self.close()
        self.secondForm.close()

    def button1_clicked(self, s):
        print("clicked", s)
        # dlg = QDialog(self)
        # dlg.setWindowTitle("HELLO")
        # dlg.move(50, 50)
        # dlg.exec_()
        dlg = CustomerDialog(self)
        if dlg.exec_():
            print("OK")
            self.label1.setText("Accepted")
            self.close()
        else:
            print("KO")
            self.label1.setText("Not Accepted")

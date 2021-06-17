from PyQt5.QtWidgets import QMainWindow, QComboBox, QLabel, QListWidget, QLineEdit
import re

class MainWindow4(QMainWindow):

    lista = ['Vittoria', 'Roberta', 'Federica', 'Alessia', 'Carla', 'Ylenia', 'Lorenzo']

    def __init__(self, parent=None):
        super(MainWindow4, self).__init__(parent)

        self.setWindowTitle("Main Window4")
        self.setGeometry(150, 150, 600, 300)

        self.label = QLabel('Nome', self)
        self.label.move(50, 50)

        self.label2 = QLabel('xx', self)
        self.label2.move(250, 50)

        self.lnEdit = QLineEdit(self)
        self.lnEdit.setGeometry(300, 50, 200, 20)
        #self.lnEdit.setInputMask('[A-Z]')
        self.lnEdit.returnPressed.connect(self.addToList)

        self.cmbBox = QComboBox(self)
        self.cmbBox.setEditable(True)
        self.cmbBox.move(50, 100)
        self.cmbBox.addItems(self.lista)
        self.cmbBox.model().sort(0)
        self.cmbBox.currentTextChanged.connect(self.label.setText)

        self.lst=QListWidget(self)
        self.lst.move(200, 100)
        self.lst.setGeometry(200, 100, 100, 150)
        self.lst.addItems(self.lista)
        print(self.lst.count())

        self.lst.itemSelectionChanged.connect(self.itemEntered)
        self.lst.model().rowsInserted.connect(self.itemEntered)
        self.lst.insertItem(2, 'Paola')
        self.lst.insertItem(4,'Giovanna')
        self.lst.setCurrentRow(4)

    def itemEntered(self):
        print(f"item entered")
        self.label2.setText(str(self.lst.count()))

    def addToList(self):
        s = self.lnEdit.text()
        if s.isalpha():
            self.lst.addItem(self.lnEdit.text())
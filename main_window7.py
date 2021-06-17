import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow7 import Ui_MainWindow
from codfisc.codFiscale import CodFiscale

class MainWindow7(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.show()

        self.label.setText('Ciao')

        self.rdbMas.setChecked(True)

        self.pushButton.setText('Premimi')
        self.pushButton.clicked.connect(self.pushButton_clicked)

        #self.dataNas.setDisplayFormat("dd/MM/yyyy")

    def pushButton_clicked(self):
        self.label.setText('Mi hai premuto !')
        dt = self.dataNas.date()

        if self.rdbMas.isChecked():
            self.lnSesso.setText('M')
        else:
            self.lnSesso.setText('F')

        cf = CodFiscale(self.lnCogn.text(), self.lnNome.text(), self.lnSesso.text(), dt.toPyDate(), self.lnLuogo.text())
        self.setWindowTitle(cf.stampaCF())
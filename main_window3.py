from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QCheckBox

class MainWindow3(QMainWindow):
    def __init__(self):
        super(MainWindow3, self).__init__()

        self.setWindowTitle('Main Window 3')
        self.setGeometry(0, 0, 400, 400)

        self.label = QLabel('Ciaooo', self)
        font = self.label.font()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignVCenter)
        self.label.setStyleSheet("border-radius: 100px; border: 1px solid black; color: green")
        self.label.move(100, 200)

        self.ckBox = QCheckBox('Check', self)
        self.ckBox.setCheckState(Qt.Checked)
        self.ckBox.setTristate(True)
        self.ckBox.move(50, 300)
        self.ckBox.stateChanged.connect(self.chkBox_changed)

    def chkBox_changed(self, g):

        print(g == Qt.Checked)
        if g == Qt.Checked:
            h='green'
            self.label.setStyleSheet(f"color: {h}")
        elif g == Qt.PartiallyChecked:
            self.label.setStyleSheet("color: orange")
        else:
            self.label.setStyleSheet("color: red")

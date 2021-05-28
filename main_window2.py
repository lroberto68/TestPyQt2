from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QVBoxLayout, QWidget


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Seconda finestra')
        self.setFixedSize(600, 300)

        self.label = QLabel()

        self.lineEdit = QLineEdit()
        self.lineEdit.textChanged.connect(self.label.setText)
        
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.label)

        container=QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
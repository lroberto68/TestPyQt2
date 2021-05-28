from PyQt5.QtWidgets import QMainWindow, QPushButton
from random import choice

window_titles = ['Finestra_1', 'Finestra_2', 'Finestra_3', 'Finestra_4', 'Finestra_5', 'X']


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.the_button_is_checked = False

        self.setWindowTitle("My App")
        self.setFixedSize(600, 300)
        self.windowTitleChanged.connect(self.window_title_changed)

        self.button = QPushButton('ciao')
        self.button.setCheckable(True)
        self.setCentralWidget(self.button)
        self.button.setChecked(self.the_button_is_checked)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toggled)
        self.button.released.connect(self.button_released)

    def button_clicked(self):
        print("button clicked")
        self.button.setText('Cliccato')
        new_title = choice(window_titles)
        self.setWindowTitle(new_title)

    def button_toggled(self, checked):
        print('test')
        self.the_button_is_checked = checked
        if not checked:
            self.button.setText('Ciao')
        print("Checked ?", checked)

    def button_released(self):
        self.the_button_is_checked=self.button.isChecked()
        print('stato button= ', self.the_button_is_checked)

    def window_title_changed(self, window_title):
        if window_title=='X':
            print ('Disabilito')
            self.button.setText('Disabilitato')
            self.button.setEnabled(False)
        print('Title changed as: ', window_title)
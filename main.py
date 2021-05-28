from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from main_window2 import MainWindow2
from main_window3 import MainWindow3
from main_window4 import MainWindow4
from main_window5 import MainWindow5

def main():
    print('Hello World')
    app=QApplication([])
    window=MainWindow()
    window.show()

    app.exec_()

def main2():
    app = QApplication([])
    window = MainWindow2()
    window.show()

    app.exec_()

def main3():
    app = QApplication([])
    window = MainWindow3()
    window.show()

    app.exec_()

def main4():
    app = QApplication([])
    window = MainWindow4()
    window.show()
    print(window.lista)
    app.exec_()

def main5():
    app=QApplication([])
    window = MainWindow5()
    window.show()

    app.exec_()

if __name__=='__main__':
    #main()
    #main2()
    #main3()
    #main4()
    main5()

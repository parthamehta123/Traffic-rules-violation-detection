import sys
# import qdarkstyle
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from PyQt5 import QtWidgets

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    #w = QtWidgets.QMainWindow()
    #main_window.setupUi(w)
    #w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
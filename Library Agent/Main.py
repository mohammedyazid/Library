from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from Gui import Ui_Gui


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Gui()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('Ui/Assets/Ui/milky-way.png'))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
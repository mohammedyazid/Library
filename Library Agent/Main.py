from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from Gui import Agent
import threading
from Path import path

class MainWindow(QMainWindow):
    
    def __init__(self):
        self.path = path()
        super(MainWindow, self).__init__()
        self.ui = Agent()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(self.path+'businessman.png'))
        client_handler = threading.Thread( target=self.ui.with_clients,args=()  )
        client_handler.start()
if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
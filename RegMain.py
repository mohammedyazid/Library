from PyQt5 import QtWidgets
from Login import Ui_LoginWindow
from Register import Ui_RegisterWindow
from Mehtods import meth
import sys
#Register Main class used to run Sign Up window
class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = RegisterWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
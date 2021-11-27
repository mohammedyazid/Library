from PyQt5 import QtWidgets
from Login import Ui_LoginWindow
from Register import Ui_RegisterWindow
from RegMain import RegisterWindow
from Mehtods import meth
import sys

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        #Buttons actions

                                            #Affect RegisterWindow class as a parameter in the method push_signup
        self.ui.log_SignUp.clicked.connect(lambda:meth.push_signup(RegisterWindow()))

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
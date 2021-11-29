
from lib_tabs import*



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.setWindowIcon(QtGui.QIcon('/home/yassine/repo/Icons/Main.png'))## make an icon for our app

    sys.exit(app.exec_())
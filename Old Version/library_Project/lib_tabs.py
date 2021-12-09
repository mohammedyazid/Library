

from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_RegisterWindow
from Login import Ui_LoginWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(978, 615)
        self.library_tab = QtWidgets.QTabWidget(Form)
        self.library_tab.setGeometry(QtCore.QRect(-2, -32, 980, 650))
        self.library_tab.setStyleSheet("")
        self.library_tab.setObjectName("library_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        
        self.login=Ui_LoginWindow()
        self.login.setupUi(self.tab)
        self.login.log_SignUp.clicked.connect(self.toOne)


        self.library_tab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        self.register=Ui_RegisterWindow()
        self.register.setupUi(self.tab_2)
        self.register.btn_of_return.clicked.connect(self.toZero)

        self.library_tab.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.library_tab.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab_3), _translate("Form", "Page"))
    
    def toOne(self):
        self.library_tab.setCurrentIndex(1)
    
    def toZero(self):
        self.library_tab.setCurrentIndex(0)

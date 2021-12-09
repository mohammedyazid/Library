

from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_RegisterWindow
from Login import Ui_LoginWindow
from Library1 import Ui_MainWindow
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(978, 615)
        self.library_tab = QtWidgets.QTabWidget(Form)
        self.library_tab.setGeometry(QtCore.QRect(-2, -32, 980, 650))
        self.library_tab.setStyleSheet("")
        self.library_tab.setObjectName("library_tab")# creatino of library_tab object
        
        self.tab = QtWidgets.QWidget()# #########creation of tab object
        self.tab.setObjectName("tab")
        self.login=Ui_LoginWindow()# for Login module
        self.login.setupUi(self.tab)
        self.login.log_SignUp.clicked.connect(self.toOne)
        self.login.log_SignIn.clicked.connect(self.toTow)
        self.library_tab.addTab(self.tab, "")# ############ add tab object to library_tab object
        #-------------------------------------------------------------------------
        #-------------------------------------------------------------------------
        self.tab_2 = QtWidgets.QWidget()# ##########creation of tab_2 object
        self.tab_2.setObjectName("tab_2")
        self.register=Ui_RegisterWindow()# for Register module
        self.register.setupUi(self.tab_2)
        self.register.btn_of_return.clicked.connect(self.toZero)
        self.register.reg_SignUp.clicked.connect(self.toTow)
        self.library_tab.addTab(self.tab_2, "")# ########## add tab_2 object to library_tab object
        #-------------------------------------------------------------------------
        #-------------------------------------------------------------------------

        self.tab_3 = QtWidgets.QWidget()# ##########creation of tab_3 object
        self.tab_3.setObjectName("tab_3")
        self.library=Ui_MainWindow()# for Library module
        self.library.setupUi(self.tab_3)
        self.library.logout_button_2.clicked.connect(self.toZero)
        self.library_tab.addTab(self.tab_3, "")# ########## add tab_2 object to library_tab object

        self.retranslateUi(Form)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab_3), _translate("Form", "Page"))
    

    
    def toZero(self):
        self.library_tab.setCurrentIndex(0)

    def toOne(self):
        self.library_tab.setCurrentIndex(1)

    def toTow(self):
        self.library_tab.setCurrentIndex(2)


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('Windows_Ui/')
from register import Ui_RegisterWindow
from login import Ui_LoginWindow
from help import Ui_HelpWindow
from books import Ui_BooksWindow
from request import Ui_RequestWindow
from myacc import Ui_MyaccWindow

class Ui_Gui(object):
    def setupUi(self, Gui):

        '''Tab Widget Size & Postition intialisation'''
        Gui.setObjectName("Library")
        Gui.resize(1128, 615)
        self.library_tab = QtWidgets.QTabWidget(Gui)
        self.library_tab.setGeometry(QtCore.QRect(-2, -32, 1128, 629))
        self.library_tab.setStyleSheet("")
        self.library_tab.setObjectName("library_tab")
        
        ################Tabs#####################
        #TAB 1
        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")
        self.login=Ui_LoginWindow()
        self.login.setupUi(self.tab0)
        self.library_tab.addTab(self.tab0,"")


        #TAB 2
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.register=Ui_RegisterWindow()
        self.register.setupUi(self.tab1)
        self.library_tab.addTab(self.tab1,"")
        
        #TAB 3 
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.help=Ui_HelpWindow()
        self.help.setupUi(self.tab2)
        self.library_tab.addTab(self.tab2,"")

        #TAB 4
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.books= Ui_BooksWindow()
        self.books.setupUi(self.tab3)
        self.library_tab.addTab(self.tab3,"")

        #TAB 5
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.myacc= Ui_MyaccWindow()
        self.myacc.setupUi(self.tab4)
        self.library_tab.addTab(self.tab4,"")

        #TAB 6
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.reqbook= Ui_RequestWindow()
        self.reqbook.setupUi(self.tab5)
        self.library_tab.addTab(self.tab5,"")

        #########################################

        #Actions
        self.register.re_backbtn.clicked.connect(self.toLogin)
        self.help.help_backbtn.clicked.connect(self.toLogin)

        self.login.lg_signupbtn.clicked.connect(self.toRegister)
        
        self.login.lg_helpbtn.clicked.connect(self.toHelp)
        self.register.re_helpbtn.clicked.connect(self.toHelp)


        #####Main Page Actions "After Logging in"#####
        self.books.main_accbtn.clicked.connect(self.toAcc)
        self.books.main_reqbtn.clicked.connect(self.toRequest)

        self.myacc.main_booksbtn.clicked.connect(self.toBooks)
        self.myacc.main_reqbtn.clicked.connect(self.toRequest)

        self.reqbook.main_accbtn.clicked.connect(self.toAcc)
        self.reqbook.main_booksbtn.clicked.connect(self.toBooks)

        '''Setting initial index to Zero which means 
        when you run the code the first page u will see is the login page'''
        ################################################
        self.retranslateUi(Gui)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gui)
        ################################################


    def retranslateUi(self, Gui):
        _translate = QtCore.QCoreApplication.translate
        Gui.setWindowTitle(_translate("Gui", "Gui"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab0), _translate("Gui", "Login"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab1), _translate("Gui", "Register"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab2), _translate("Gui", "Help"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab3), _translate("Gui", "Books"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab4), _translate("Gui", "My Account"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab5), _translate("Gui", "Request"))

    #Fonctions
    def toLogin(self):
        self.library_tab.setCurrentIndex(0)
    def toRegister(self):
        self.library_tab.setCurrentIndex(1)
    def toHelp(self):
        self.library_tab.setCurrentIndex(2)
    def toBooks(self):
        self.library_tab.setCurrentIndex(3)
    def toAcc(self):
        self.library_tab.setCurrentIndex(4)
    def toRequest(self):
        self.library_tab.setCurrentIndex(5)


from PyQt5 import QtCore, QtGui, QtWidgets
from register import Ui_RegisterWindow
from login import Ui_LoginWindow
from help import Ui_HelpWindow

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
        #########################################

        #Actions
        self.register.re_backbtn.clicked.connect(self.toLogin)
        self.help.help_backbtn.clicked.connect(self.toLogin)

        self.login.lg_signupbtn.clicked.connect(self.toRegister)
        
        self.login.lg_helpbtn.clicked.connect(self.toHelp)
        self.register.re_helpbtn.clicked.connect(self.toHelp)

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
    

    #Fonctions
    def toLogin(self):
        self.library_tab.setCurrentIndex(0)
    def toRegister(self):
        self.library_tab.setCurrentIndex(1)
    def toHelp(self):
        self.library_tab.setCurrentIndex(2)

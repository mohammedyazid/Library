import socket
import hashlib
from typing import Text


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('Windows_Ui/')
from register import Ui_RegisterWindow
from login import Ui_LoginWindow
from help import Ui_HelpWindow
from books import Ui_BooksWindow
from request import Ui_RequestWindow
from myacc import Ui_MyaccWindow
import psycopg2
from psycopg2 import extras
import time

#DB_HOST=""
#DB_NAME=""
#DB_USER=""
#DB_PASS=""





class Ui_Gui(object):
    #conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
    #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
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
        self.LoginWindow=Ui_LoginWindow()
        self.LoginWindow.setupUi(self.tab0)
        self.library_tab.addTab(self.tab0,"")


        #TAB 2
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.RegisterWindow=Ui_RegisterWindow()
        self.RegisterWindow.setupUi(self.tab1)
        self.library_tab.addTab(self.tab1,"")
        
        #TAB 3 
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.HelpWindow=Ui_HelpWindow()
        self.HelpWindow.setupUi(self.tab2)
        self.library_tab.addTab(self.tab2,"")

        #TAB 4
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.BooksWindow= Ui_BooksWindow()
        self.BooksWindow.setupUi(self.tab3)
        self.library_tab.addTab(self.tab3,"")

        #TAB 5
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.AccountWindow= Ui_MyaccWindow()
        self.AccountWindow.setupUi(self.tab4)
        self.library_tab.addTab(self.tab4,"")

        #TAB 6
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.RequestWindow= Ui_RequestWindow()
        self.RequestWindow.setupUi(self.tab5)
        self.library_tab.addTab(self.tab5,"")

        #########################################

        #Actions
        self.RegisterWindow.BACK.clicked.connect(self.toLogin)
        self.HelpWindow.BACK.clicked.connect(self.toLogin)
        #Testing self.RegisterWindow.SIGN_UP.clicked.connect(self.toAcc)
        self.LoginWindow.SIGN_UP.clicked.connect(self.toRegister)
        self.LoginWindow.SIGN_IN.clicked.connect(self.logged)
        self.LoginWindow.HELP.clicked.connect(self.toHelp)
        self.RegisterWindow.HELP.clicked.connect(self.toHelp)
        self.AccountWindow.LOGOUT.clicked.connect(self.toLogin)
        self.RegisterWindow.SIGN_UP.clicked.connect(self.signupaction)
        #####Main Page Actions "After Logging in"#####
        self.BooksWindow.MY_ACCOUNT.clicked.connect(self.toAcc)
        self.BooksWindow.REQUEST.clicked.connect(self.toRequest)

        self.AccountWindow.BOOKS.clicked.connect(self.toBooks)
        self.AccountWindow.REQUEST.clicked.connect(self.toRequest)

        self.RequestWindow.MY_ACCOUNT.clicked.connect(self.toAcc)
        self.RequestWindow.BOOKS.clicked.connect(self.toBooks)

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
    def logged(self):
        if (self.LoginWindow.ID.text()!="" and self.LoginWindow.PASSWORD.text()!=""):
         client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         client.connect(('127.0.0.1', 12397 ))
         id = self.LoginWindow.ID.text()
         password = self.LoginWindow.PASSWORD.text()
         password=hashlib.sha256(str.encode(password)).hexdigest()#password encryption before send it       
         client.send(str.encode(id+' '+password))
         response = client.recv(2048)
         response = response.decode()
         if response =='password or id is incorrect':
            self.LoginWindow.lg_error.setText(response)
         elif response =='YES':
             self.toAcc()

         client.close()
        else:
            self.LoginWindow.lg_error.setText("You can't leave any field empty")

                    
    def toLogin(self):
        self.LoginWindow.lg_error.setText("")
        self.library_tab.setCurrentIndex(0)
        self.clear("login")
        self.clear("myaccount")
    def toRegister(self):
        self.clear("register")
        self.library_tab.setCurrentIndex(1)
    def toHelp(self):
        self.library_tab.setCurrentIndex(2)
    def toBooks(self):
        self.library_tab.setCurrentIndex(3)
    def toAcc(self):
        self.library_tab.setCurrentIndex(4)
    def toRequest(self):
        self.library_tab.setCurrentIndex(5)
    def signupaction(self):
        #GetText From Register Fields
        fn=self.RegisterWindow.FIRST_NAME.text()
        ln=self.RegisterWindow.LAST_NAME.text()
        ml=self.RegisterWindow.EMAIL_ADDRESS.text()
        ph=self.RegisterWindow.PHONE.text()
        ps=self.RegisterWindow.PASSWORD.text()
        psc=self.RegisterWindow.CONFIRME_PASSWORD.text()
        id=self.RegisterWindow.ID.text()
        if(fn!="" and ln!="" and ml!="" and ph!="" and ps!="" and id!=""): 
            if(ps==psc):
                if self.RegisterWindow.checkBox.isChecked():
                    # Ui_Gui.cur.execute("INSERT INTO members (id,firstname,lastname,email,phone,password) VALUES('"+str(id)+"','"+fn+"','"+ln+"','"+ml+"','"+ph+"','"+ps+"')")
                    # Ui_Gui.conn.commit()
                    # other info
                    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
                    #response = client1.recv(2048)
                    password=hashlib.sha256(str.encode(ps)).hexdigest()#password encryption before send it
                    confirm_password=hashlib.sha256(str.encode(psc)).hexdigest()
                    client1.connect(('127.0.0.1', 12397 ))
                    client1.send(str.encode(id+' '+fn+' '+ln+' '+ml+' '+ph+' '+password))
                    self.clear("register")
                    client1.close()
                    self.RegisterWindow.re_error.setStyleSheet("color:green;")
                    self.RegisterWindow.re_error.setText("Registered Succefully")
                    self.toAcc()
                else:
                    self.RegisterWindow.re_error.setStyleSheet("color:red;")
                    self.RegisterWindow.re_error.setText("Please confirm your action by checking the check box")         
            else:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("Password and Confirmed Password should be the same")
        else:
            self.RegisterWindow.re_error.setStyleSheet("color:red;")
            self.RegisterWindow.re_error.setText("You can't leave any field empty")
    def getbooks(self):
        with Ui_Gui.conn:
            Ui_Gui.cur.execute("SELECT * FROM book")
            #Fetch Books Data's from data base
            data = Ui_Gui.cur.fetchall()
            #Adding Books data to table down here
    def clear(self,page):
        if(page=="register"):
            self.RegisterWindow.FIRST_NAME.setText("")
            self.RegisterWindow.LAST_NAME.setText("")
            self.RegisterWindow.EMAIL_ADDRESS.setText("")
            self.RegisterWindow.PHONE.setText("")
            self.RegisterWindow.PASSWORD.setText("")
            self.RegisterWindow.CONFIRME_PASSWORD.setText("")
            self.RegisterWindow.ID.setText("")
        if(page=="login"):
            self.LoginWindow.ID.setText("")
            self.LoginWindow.PASSWORD.setText("")
        if(page=="myaccount"):
            self.AccountWindow.FIRST_NAME.setText("")
            self.AccountWindow.LAST_NAME.setText("")
            self.AccountWindow.ID.setText("")
            self.AccountWindow.PHONE.setText("")
            self.AccountWindow.EMAIL_ADDRESS.setText("")
    
  
        

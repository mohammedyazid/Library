import socket
import hashlib
import re
from PyQt5 import QtCore, QtWidgets
import sys
sys.path.append('Windows_Ui/')
from register import Ui_RegisterWindow
from login import Ui_LoginWindow
from help import Ui_HelpWindow
from books import Ui_BooksWindow
from request import Ui_RequestWindow
from myacc import Ui_MyaccWindow
from about import About

class student(object): 
    def setupUi(self, Gui):
        ###############################################
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
        
        #TAB 3########unused#####
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

        #TAB 6#########unused#####
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.RequestWindow= Ui_RequestWindow()
        self.RequestWindow.setupUi(self.tab5)
        self.library_tab.addTab(self.tab5,"")
        
        #TAB 7
        self.tab6 = QtWidgets.QWidget()
        self.tab6.setObjectName("tab6")
        self.AboutWindow= About()
        self.AboutWindow.setupUi(self.tab6)
        self.library_tab.addTab(self.tab6,"")

        #########################################

        ############Link buttons with an action#########
        
                ########Before logging in######
        self.LoginWindow.SIGN_UP.clicked.connect(self.toRegister)
        self.LoginWindow.SIGN_IN.clicked.connect(self.logged)
        self.LoginWindow.ABOUT.clicked.connect(self.toabout)
        self.RegisterWindow.BACK.clicked.connect(self.toLogin)
        self.RegisterWindow.ABOUT.clicked.connect(self.toabout)
        self.RegisterWindow.SIGN_UP.clicked.connect(self.signupaction)
        
        #self.HelpWindow.BACK.clicked.connect(self.toLogin)
        
                #####After Logging in#######
        self.BooksWindow.MY_ACCOUNT.clicked.connect(self.toAcc)

        self.AccountWindow.BOOKS.clicked.connect(self.toBooks)
        self.AccountWindow.ABOUT_US.clicked.connect(self.toabout)
        self.AccountWindow.LOGOUT.clicked.connect(self.toLogin)
        self.AccountWindow.SUBMIT.clicked.connect(self.changepass)

        self.AboutWindow.BACK.clicked.connect(self.back)
        
        ####################################################################
        '''Setting initial index to Zero which means 
        when you run the code the first page u will see is the login page'''
        
        self.retranslateUi(Gui)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gui)
        ####################################################################
        
        
        ##This variable is used in about page when u press back button in the about page you will be redirected to
        ##1-Account window if you were already logged into your account
        ##2-The most recent page opened "if you're not logged in/registered" for exemple if you press about in the login page and then u press back in about you'll be redirected to the login page
        self.indice=0

    #########Define Tabs index's and Title#############
    def retranslateUi(self, Gui):
        _translate = QtCore.QCoreApplication.translate
        Gui.setWindowTitle(_translate("Gui", "Gui"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab0), _translate("Gui", "Login"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab1), _translate("Gui", "Register"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab2), _translate("Gui", "Help"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab3), _translate("Gui", "Books"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab4), _translate("Gui", "My Account"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab5), _translate("Gui", "Request"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab6), _translate("Gui", "About"))
        
    #########Fonctions############
    def logged(self):
        
        ####Check if the password and id fields are not empty########
        if (self.LoginWindow.ID.text()!="" and self.LoginWindow.PASSWORD.text()!=""):
            
            #######Define client variable as a client to be able to connect to server#####
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            #######Connect client to server###
            client.connect(('127.0.0.1', 12397 ))
            
            #####get the entered id and password values###
            id = self.LoginWindow.ID.text()
            password = self.LoginWindow.PASSWORD.text()
            
            #password encryption 
            password=hashlib.sha256(str.encode(password)).hexdigest()       
            
            #Sending the encrypted password to the server
            client.send(str.encode(id+' '+password))
            
            #recieve the encrypted server response
            response = client.recv(2048)
            
            #Decoding the encrypted response
            response = response.decode()
            
            #This means if response is not an error message then turn it into a list
            if(len(response)>27):
                #replace any of the below characters in the response with '' then save them   
                response = re.sub('[\' ()]', '', response)
                response = re.sub('[,]', ' ', response)
                response = response.split(' ')
                
            #if the recieved response equals to 'password or id is incorrect then display the message
            if response =='password or id is incorrect':
                self.LoginWindow.lg_error.setText(response)
            
            #else if the response is a list with a length eqauls to 5 display user info in the account page and redirect him to it 
            elif len(response)==5:
                self.AccountWindow.ID.setText(response[0])
                self.AccountWindow.FIRST_NAME.setText(response[1])
                self.AccountWindow.LAST_NAME.setText(response[2])
                self.AccountWindow.PHONE.setText(response[3])
                self.AccountWindow.EMAIL_ADDRESS.setText(response[4])
                self.toAcc()
                
            #Disconnect the client
            client.close()
        
        ##if either the id or password field was empty display an error message 
        else:
            self.LoginWindow.lg_error.setText("You can't leave any field empty")
    
    ##redirect to about page
    def toabout(self):
        self.library_tab.setCurrentIndex(6)
    
    ##redirect to the last opened page
    def back(self):
        self.library_tab.setCurrentIndex(self.indice)
    
    ##redirect to login page                
    def toLogin(self):
        
        ####Clear the login error label if it exists and redirect to login page
        self.LoginWindow.lg_error.setText("")
        self.library_tab.setCurrentIndex(0)
        
        ####when logging out clear the id and password left in the login page 
        self.clear("login")
        self.clear("myaccount")
        
        ##this means that the recent page accessed is the login page in case if the user press the about page
        self.indice=0
        
    ##redirect to register page
    def toRegister(self):
        
        #clear text fields if there is any data from the ast operation left
        self.clear("register")
        self.library_tab.setCurrentIndex(1)
        
        ##this means that the recent page accessed is the register page in case if the user press the about page
        self.indice=1
    
    ##redirect to books page
    def toBooks(self):
        
        #clear the error label
        self.AccountWindow.DISPLAY.setText('')
        self.library_tab.setCurrentIndex(3)
    
    
    def toAcc(self):
        
        self.AccountWindow.DISPLAY.setText('')
        
        ##This means the recent accessed page is the account page
        self.indice=4
        self.library_tab.setCurrentIndex(4)
        
    def toRequest(self):
        self.AccountWindow.DISPLAY.setText('')
        self.library_tab.setCurrentIndex(5)
        
    def signupaction(self):
        ######GetText From Register Text Fields#######
        fn=self.RegisterWindow.FIRST_NAME.text()
        ln=self.RegisterWindow.LAST_NAME.text()
        ml=self.RegisterWindow.EMAIL_ADDRESS.text()
        ph=self.RegisterWindow.PHONE.text()
        ps=self.RegisterWindow.PASSWORD.text()
        psc=self.RegisterWindow.CONFIRME_PASSWORD.text()
        id=self.RegisterWindow.ID.text()
        ########Match########
        mailformat = re.match("^[A-Za-z0-9_.]{4,}@[A-Za-z]{3,}\.[A-Za-z]{2,}$",ml)
        passformat = re.match("^.{8,}",ps)
        idformat = re.match("^[0-9]{8,10}$",id)
        phoneformat = re.match("^[0]?[6|7|5]{1}[0-9]{8}$",ph)
        fnameformat = re.match("^[A-Za-z ]{3,}$",fn)
        lnameformat = re.match("^[A-Za-z ]{3,}$",ln)
        ###################
        
        ##check if the field are not empty and their formats are valid
        if(fn!="" and ln!="" and ml!="" and ph!="" and ps!="" and id!="" and mailformat!=None and passformat!=None and idformat!=None and phoneformat!=None) and fn !=None and ln!=None: 
            ###Check if the password and the confirmed password are the same
            if(ps==psc):
                if self.RegisterWindow.checkBox.isChecked():
                    
                    #Define client 
                    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
                    #password encryption before send it
                    password=hashlib.sha256(str.encode(ps)).hexdigest()
                    
                    client1.connect(('127.0.0.1', 12397 ))
                    client1.send(str.encode(id+' '+fn+' '+ln+' '+ml+' '+ph+' '+password))
                    self.clear("register")
                    
                    #Disconnect client
                    client1.close()
                    
                    self.AccountWindow.ID.setText(id)
                    self.AccountWindow.FIRST_NAME.setText(fn)
                    self.AccountWindow.LAST_NAME.setText(ln)
                    self.AccountWindow.PHONE.setText(ph)
                    self.AccountWindow.EMAIL_ADDRESS.setText(ml)
                    self.toAcc()
                    
                else:
                    self.RegisterWindow.re_error.setStyleSheet("color:red;")
                    self.RegisterWindow.re_error.setText("Please confirm your action by checking the check box")         
            else:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("Password and Confirmed Password should be the same")
        else:
            if fnameformat == None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("invalid first name")
            elif lnameformat == None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("invalid last name")
            elif mailformat==None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("Invalid Mail format")
            elif idformat ==None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("invalid id")
            elif phoneformat ==None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("invalid phone number")
            elif passformat==None:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("Short Password Please type a long one")
            else:
                self.RegisterWindow.re_error.setStyleSheet("color:red;")
                self.RegisterWindow.re_error.setText("You can't leave any field empty")
            
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
        if(page=="changepass"):
            self.AccountWindow.CURRENT_PASSWORD.setText("")
            self.AccountWindow.NEW_PASSWORD.setText("")
            self.AccountWindow.CONFIRME_PASSWORD.setText("")
        
    def changepass(self):
        
        password = self.AccountWindow.CURRENT_PASSWORD.text()
        npassword= self.AccountWindow.NEW_PASSWORD.text()
        cpassword = self.AccountWindow.CONFIRME_PASSWORD.text()
        
        if(npassword == cpassword):
            client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client2.connect(('127.0.0.1', 12397 ))
        
            password=hashlib.sha256(str.encode(password)).hexdigest()
            npassword=hashlib.sha256(str.encode(npassword)).hexdigest()
            id = self.AccountWindow.ID.text()
            
            ##send the old and the new password to the server
            client2.send(str.encode(id+' '+password+' '+npassword))
            
            response = client2.recv(2048)
            response = response.decode()
            
            #if server response = done display success message else display and error
            if(response == 'Done'):
                self.AccountWindow.DISPLAY.setStyleSheet("color:green;")
                self.AccountWindow.DISPLAY.setText('Password Changed succefully')
                self.clear("changepass")
            else:
                self.AccountWindow.DISPLAY.setStyleSheet("color:red;")
                self.AccountWindow.DISPLAY.setText(response)
        else:
            self.AccountWindow.DISPLAY.setStyleSheet("color:red;")
            self.AccountWindow.DISPLAY.setText('New Pass != Confirmed Pass')
        client2.close()
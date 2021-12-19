from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Ui.books import Ui_BooksWindow
from Ui.members import Ui_MembersWidnow
import psycopg2
from psycopg2 import extras
import time
import socket


DB_HOST=""
DB_NAME=""
DB_USER=""
DB_PASS=""

ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)


port = 12397 # Reserve a port for your service

try:
        ServerSocket.bind(('', port))# bind the ServerSocket with (host+port) tuple
except socket.error as e:
        print(str(e))

ServerSocket.listen(5)
class Ui_Gui(object):
    ThreadCount=0
    def setupUi(self, Gui):
        
       # '''Tab Widget Size & Postition intialisation'''
        Gui.setObjectName("Library")
        Gui.resize(1179, 723)
        self.library_tab = QtWidgets.QTabWidget(Gui)
        self.library_tab.setGeometry(QtCore.QRect(-2, -32,1179, 723))
        self.library_tab.setStyleSheet("")
        self.library_tab.setObjectName("library_tab")
        
        ################Tabs#####################
        #TAB 1
        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")
        self.BooksWindow=Ui_BooksWindow()
        self.BooksWindow.setupUi(self.tab0)
        self.library_tab.addTab(self.tab0,"")


        #TAB 2
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.MembersWindow=Ui_MembersWidnow()
        self.MembersWindow.setupUi(self.tab1)
        self.library_tab.addTab(self.tab1,"")
        
        

        #########################################

        #Actions
        self.BooksWindow.MANAGE_MEMBERS.clicked.connect(self.tomembers)
        self.MembersWindow.MANAGE_BOOKS.clicked.connect(self.tobooks)

        '''Setting initial index to Zero which means 
        when you run the code the first page u will see is the login page'''
        ################################################
        self.retranslateUi(Gui)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gui)
        ################################################
        
    def retranslateUi(self, Gui):
        _translate = QtCore.QCoreApplication.translate
        Gui.setWindowTitle(_translate("Agent Space", "Agent Space"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab0), _translate("Agent Space", "Books"))
        self.library_tab.setTabText(self.library_tab.indexOf(self.tab1), _translate("Agent Space", "Members"))
        
    #Fonctions
    def tomembers(self):
        self.library_tab.setCurrentIndex(1)
    def tobooks(self):
        self.library_tab.setCurrentIndex(0)
    
    def client_connection(self,Client):
        

        

        data = Client.recv(2048)
        data = data.decode()
        infos=data.split()
        
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur2 = conn.cursor()
        if len(infos) == 6:
           cur2.execute("INSERT INTO members (id,firstname,lastname,email,phone,password) VALUES(%s,%s,%s,%s,%s,%s)",(infos[0],infos[1],infos[2],infos[3],infos[4],infos[5]))
        else:
            idd1= infos[0]
            passwordd1=infos[1]
            sql_id_pssowrd = """SELECT id,password FROM members WHERE id = '%s' AND password = '%s'""" % (idd1,passwordd1)
            cur2.execute(sql_id_pssowrd)
            resault_id_password=cur2.fetchall()
            
            print(len(resault_id_password))

            if len(resault_id_password) == 1:
                Client.send(str.encode('YES'))
            elif len(resault_id_password) == 0:
                Client.send(str.encode('password or id is incorrect'))  
           
      
        conn.commit()
        cur2.close()
        conn.close()
     
        
        
    def with_clients(self):
        import threading
        while True:
            connec, address = ServerSocket.accept()
            client_handler = threading.Thread(target=self.client_connection,args=(connec,))
            client_handler.start()
            Ui_Gui.ThreadCount += 1
            print('Connection Request: ' + str(Ui_Gui.ThreadCount))
            #ServerSocket.close()

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('Ui/')
from books import Ui_BooksWindow
from members import Ui_MembersWidnow
import psycopg2
from psycopg2 import extras
import time

DB_HOST="localhost"
DB_NAME="library"
DB_USER="postgres"
DB_PASS="admin"


class Ui_Gui(object):
    conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
    cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur2 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    '''Select from books table'''
    cur1.execute("SELECT * FROM books")
    '''select from members table'''
    cur2.execute("SELECT * FROM books")
    def setupUi(self, Gui):
        '''Tab Widget Size & Postition intialisation'''
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
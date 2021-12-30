from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from books import Ui_BooksWindow
from members import Ui_MembersWidnow
import psycopg2
from psycopg2 import extras
import time
import socket

DB_HOST="localhost"
DB_NAME="libraryagent"
DB_USER="yassine"
DB_PASS="adpost2008"

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
        self.BooksWindow.ADD_BOOK.clicked.connect(self.add_book)
        self.BooksWindow.DELETE.clicked.connect(self.delete_book)
        self.MembersWindow.DELETE.clicked.connect(self.delete_member)

        '''Setting initial index to Zero which means 
        when you run the code the first page u will see is the login page'''
        ################################################
        self.retranslateUi(Gui)
        self.library_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Gui)
        ################################################
        self.display_books()
        self.display_members()
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
        elif len(infos) == 2:
            idd1= infos[0]
            passwordd1=infos[1]
            sql_id_pssowrd = """SELECT id,password FROM members WHERE id = '%s' AND password = '%s'""" % (idd1,passwordd1)
            cur2.execute(sql_id_pssowrd)
            resault_id_password=cur2.fetchall()

            if len(resault_id_password) == 1:
                sql_data = """SELECT id,firstname,lastname,phone,email FROM members WHERE id = '%s' AND password = '%s'""" % (idd1,passwordd1)
                cur2.execute(sql_data)
                result_data=cur2.fetchall()
                result_data = ' '.join(map(str,result_data))
                #print(result_data)
                Client.send(str.encode(result_data))
            elif len(resault_id_password) == 0:
                Client.send(str.encode('password or id is incorrect'))  
        
        elif len(infos)==3:
                idc=infos[0]
                passc= infos[1]
                newpass=infos[2]
                sql_pass = """SELECT id,password FROM members WHERE id = '%s' AND password = '%s'""" % (idc,passc)
                cur2.execute(sql_pass)
                result_pass=cur2.fetchall()
                if len(result_pass)==1:
                    sql_update = """UPDATE members SET password='%s' WHERE id = '%s'""" % (newpass,idc)
                    cur2.execute(sql_update)
                    Client.send(str.encode('Done'))
                else :
                    Client.send(str.encode('Current Password Not found !'))
        
        else:
            titlee=infos[0]
            titlee=titlee.split("|")
            sql_book= """select * from books where title like '%s';""" %('%'+titlee[0]+'%')
            cur2.execute(sql_book)
            result_book = cur2.fetchall()
            
            if len(result_book)>0:
                result_book = ','.join(map(str,result_book))
                Client.send(str.encode(result_book))
            
                
            else:
                Client.send(str.encode("book not found")) 

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

    def add_book(self):
        
        #GetText From books Fields  
        bt_d=self.BooksWindow.BOOK_TITLE_ADD.text().lower()
        au_d=self.BooksWindow.AUTHOR_ADD.text().lower()
        ry_d=self.BooksWindow.RELEASE_YEAR_ADD.text().lower()
        
        
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur3 = conn.cursor()
        cur4=conn.cursor()
        cur4.execute('select count(*) from books;')######################################
        number_in_db=cur4.fetchall()[0][0]
        code=str(number_in_db+1)+bt_d[0]+au_d[len(au_d)-1]+str(len(bt_d))+au_d[0]+bt_d[len(bt_d)-1]
        code=code.lower()

        if(bt_d!="" and au_d!="" and ry_d!=""):

            cur3.execute("INSERT INTO books (code,title,author,released,status) VALUES(%s,%s,%s,%s,%s)",(code,bt_d,au_d,ry_d,"avalible"))
            conn.commit()
            cur3.close()
            
            self.BooksWindow.BOOK_TITLE_ADD.setText("")
            self.BooksWindow.AUTHOR_ADD.setText("")
            self.BooksWindow.RELEASE_YEAR_ADD.setText("")
            self.BooksWindow.RELEASE_YEAR.setText("")
            
        
        cur4.execute("SELECT * FROM books")
        data = cur4.fetchall()
        conn.commit()
        a = len(data) 
        b =  len(data[0])

        self.BooksWindow.Books_table.setSortingEnabled(False)
        self.BooksWindow.Books_table.setRowCount(a)
        self.BooksWindow.Books_table.setColumnCount(b)
        i=1
        j=0
        for j in range(a):
            for i in range(b):
             item = QtWidgets.QTableWidgetItem(data[j][i])
             self.BooksWindow.Books_table.setItem(j, i, item)
        self.BooksWindow.Books_table.sortByColumn(0,QtCore.Qt.SortOrder.DescendingOrder)
        
    
    def delete_book(self):
        
        bt=self.BooksWindow.BOOK_TITLE.text()
        au=self.BooksWindow.AUTHOR.text()
        ry=self.BooksWindow.RELEASE_YEAR.text()
        
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur3 = conn.cursor()
        cur4=conn.cursor()

        cur3.execute("DELETE FROM books WHERE title=%s AND author=%s AND released=%s AND status='avalible'",(bt,au,ry) )
        conn.commit()
        cur3.close()
        
        cur4.execute("SELECT * FROM books")
        data = cur4.fetchall()
        conn.commit()
        a = len(data) 
        b =  len(data[0])

        self.BooksWindow.Books_table.setSortingEnabled(False)
        self.BooksWindow.Books_table.setRowCount(a)
        self.BooksWindow.Books_table.setColumnCount(b)
        i=1
        j=0
        for j in range(a):
            for i in range(b):
             item = QtWidgets.QTableWidgetItem(data[j][i])
             self.BooksWindow.Books_table.setItem(j, i, item)
        self.BooksWindow.Books_table.sortByColumn(0,QtCore.Qt.SortOrder.DescendingOrder)
    
    
    def display_members(self):

        
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur5=conn.cursor()

        cur5.execute("SELECT * FROM members")
        data = cur5.fetchall()
        conn.commit()
        a = len(data) 
        b =  len(data[0])

        self.MembersWindow.Members_table.setSortingEnabled(False)
        self.MembersWindow.Members_table.setRowCount(a)
        self.MembersWindow.Members_table.setColumnCount(b)
        i=1
        j=0
        for j in range(a):
            for i in range(b):
             item = QtWidgets.QTableWidgetItem(data[j][i])
             self.MembersWindow.Members_table.setItem(j, i, item)
        self.MembersWindow.Members_table.sortByColumn(0,QtCore.Qt.SortOrder.DescendingOrder)
        
        
    def delete_member(self):
        
        id=self.MembersWindow.ID.text()
        fn=self.MembersWindow.FIRST_NAME.text()
        ln=self.MembersWindow.LAST_NAME.text()
        ph=self.MembersWindow.PHONE.text()
        em=self.MembersWindow.EMAIL_ADDRESS.text()
        
        
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur5=conn.cursor()
        cur6=conn.cursor()
        
        cur6.execute("DELETE FROM members WHERE id=%s AND firstname=%s AND lastname=%s AND phone=%s AND email=%s",(id,fn,ln,ph,em) )
        cur5.execute("SELECT * FROM members")
        data = cur5.fetchall()
        conn.commit()
        a = len(data) 
        b =  len(data[0])

        self.MembersWindow.Members_table.setSortingEnabled(False)
        self.MembersWindow.Members_table.setRowCount(a)
        self.MembersWindow.Members_table.setColumnCount(b)
        i=1
        j=0
        for j in range(a):
            for i in range(b):
             item = QtWidgets.QTableWidgetItem(data[j][i])
             self.MembersWindow.Members_table.setItem(j, i, item)
        self.MembersWindow.Members_table.sortByColumn(0,QtCore.Qt.SortOrder.DescendingOrder)
     
    def display_books(self):
        conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST)
        cur7=conn.cursor() 
        cur7.execute("SELECT * FROM books")
        data = cur7.fetchall()
        conn.commit()
        cur7.execute("select count(*) from books")
        number_of_books=cur7.fetchall()
        conn.commit()
        cur7.execute("select count(*) from members")
        number_of_members=cur7.fetchall()
        conn.commit()
        number_of_books=number_of_books[0][0]
        number_of_members=number_of_members[0][0]

        self.BooksWindow.NUMBER_OF_BOOKS.setText(str(number_of_books))
        self.BooksWindow.NUMBER_OF_MEMBERS.setText(str(number_of_members)) 


        a = len(data) 
        b =  len(data[0])

        self.BooksWindow.Books_table.setSortingEnabled(False)
        self.BooksWindow.Books_table.setRowCount(a)
        self.BooksWindow.Books_table.setColumnCount(b)
        i=1
        j=0
        for j in range(a):
            data[j]=list(data[j])
            data[j][0]=data[j][0].upper()
            for i in range(b):   
             item = QtWidgets.QTableWidgetItem(data[j][i])
             self.BooksWindow.Books_table.setItem(j, i, item)
        self.BooksWindow.Books_table.sortByColumn(0,QtCore.Qt.SortOrder.DescendingOrder)
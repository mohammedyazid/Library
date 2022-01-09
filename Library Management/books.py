# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'books.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import re
from Path import * 
class Ui_BooksWindow(object):
    def setupUi(self, BooksWindow):
        self.path = path()
        BooksWindow.setObjectName("BooksWindow")
        BooksWindow.resize(1128, 629)
        BooksWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.BookWindow = QtWidgets.QWidget(BooksWindow)
        self.BookWindow.setObjectName("BookWindow")
        self.frame_16 = QtWidgets.QFrame(self.BookWindow)
        self.frame_16.setGeometry(QtCore.QRect(0, 0, 171, 621))
        self.frame_16.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color:rgb(28, 113, 216)")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label19 = QtWidgets.QLabel(self.frame_16)
        self.label19.setGeometry(QtCore.QRect(10, 0, 141, 71))
        self.label19.setStyleSheet("font: 63 italic 30pt \"URW Bookman\";\n"
"color:white;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label19.setObjectName("label19")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_14.setGeometry(QtCore.QRect(90, 10, 101, 41))
        self.pushButton_14.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.pushButton_14.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path+"graduate-cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon)
        self.pushButton_14.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.log_credits_24 = QtWidgets.QPushButton(self.frame_16)
        self.log_credits_24.setGeometry(QtCore.QRect(920, 20, 181, 41))
        self.log_credits_24.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.path+"programmer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_credits_24.setIcon(icon1)
        self.log_credits_24.setIconSize(QtCore.QSize(25, 25))
        self.log_credits_24.setObjectName("log_credits_24")
        self.log_credits_25 = QtWidgets.QPushButton(self.frame_16)
        self.log_credits_25.setGeometry(QtCore.QRect(920, 70, 181, 41))
        self.log_credits_25.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.path+"book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_credits_25.setIcon(icon2)
        self.log_credits_25.setIconSize(QtCore.QSize(25, 25))
        self.log_credits_25.setObjectName("log_credits_25")
        self.MY_ACCOUNT = QtWidgets.QPushButton(self.frame_16)
        self.MY_ACCOUNT.setGeometry(QtCore.QRect(10, 180, 151, 51))
        self.MY_ACCOUNT.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        self.MY_ACCOUNT.setIcon(icon1)
        self.MY_ACCOUNT.setIconSize(QtCore.QSize(25, 25))
        self.MY_ACCOUNT.setObjectName("MY_ACCOUNT")
        self.BOOKS = QtWidgets.QPushButton(self.frame_16)
        self.BOOKS.setGeometry(QtCore.QRect(10, 240, 151, 51))
        self.BOOKS.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        self.BOOKS.setIcon(icon2)
        self.BOOKS.setIconSize(QtCore.QSize(25, 25))
        self.BOOKS.setObjectName("BOOKS")
        self.REQUEST = QtWidgets.QPushButton(self.frame_16)
        self.REQUEST.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.REQUEST.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(self.path+"interview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.REQUEST.setIcon(icon3)
        self.REQUEST.setIconSize(QtCore.QSize(25, 25))
        self.REQUEST.setObjectName("REQUEST")
        self.icon11 = QtWidgets.QPushButton(self.frame_16)
        self.icon11.setGeometry(QtCore.QRect(-20, 50, 191, 111))
        self.icon11.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(self.path+"digital-library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon11.setIcon(icon4)
        self.icon11.setIconSize(QtCore.QSize(100, 100))
        self.icon11.setObjectName("icon11")
        self.TABLE = QtWidgets.QTableWidget(self.BookWindow)
        self.TABLE.setGeometry(QtCore.QRect(180, 140, 941, 461))
        self.TABLE.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.TABLE.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TABLE.setObjectName("TABLE")
        self.TABLE.setColumnCount(5)
        self.TABLE.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TABLE.setHorizontalHeaderItem(4, item)
        self.TABLE.horizontalHeader().setDefaultSectionSize(188)
        self.frame_5 = QtWidgets.QFrame(self.BookWindow)
        self.frame_5.setGeometry(QtCore.QRect(180, 0, 941, 131))
        self.frame_5.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color:rgb(28, 113, 216)")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label20 = QtWidgets.QLabel(self.frame_5)
        self.label20.setGeometry(QtCore.QRect(10, 0, 211, 71))
        self.label20.setStyleSheet("font: 63 italic 30pt \"URW Bookman\";\n"
"color:white;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label20.setObjectName("label20")
        self.icon12 = QtWidgets.QPushButton(self.frame_5)
        self.icon12.setGeometry(QtCore.QRect(140, 0, 111, 51))
        self.icon12.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon12.setText("")
        self.icon12.setIcon(icon)
        self.icon12.setIconSize(QtCore.QSize(25, 25))
        self.icon12.setObjectName("icon12")
        self.SUBMIT = QtWidgets.QPushButton(self.frame_5)
        self.SUBMIT.setGeometry(QtCore.QRect(310, 80, 91, 31))
        self.SUBMIT.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: rgb(46, 194, 126);\n"
"    border: 2px solid white;\n"
"    border-radius: 15px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 10px;\n"
"    padding: 0px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color:rgb(0, 137, 236);;\n"
"    background-color: white;;\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(self.path+"magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SUBMIT.setIcon(icon5)
        self.SUBMIT.setIconSize(QtCore.QSize(17, 17))
        self.SUBMIT.setObjectName("SUBMIT")
        self.SUBMIT.clicked.connect(self.search_book)
        self.TITLE = QtWidgets.QLineEdit(self.frame_5)
        self.TITLE.setGeometry(QtCore.QRect(10, 80, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.TITLE.setFont(font)
        self.TITLE.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.TITLE.setMaxLength(100)
        self.TITLE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.TITLE.setDragEnabled(True)
        self.TITLE.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.TITLE.setClearButtonEnabled(True)
        self.TITLE.setObjectName("TITLE")
        #BooksWindow.setCentralWidget(self.BookWindow)
        self.menubar = QtWidgets.QMenuBar(BooksWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 22))
        self.menubar.setObjectName("menubar")
        #BooksWindow.setMenuBar(self.menubar)

        self.retranslateUi(BooksWindow)
        QtCore.QMetaObject.connectSlotsByName(BooksWindow)

    def retranslateUi(self, BooksWindow):
        _translate = QtCore.QCoreApplication.translate
        BooksWindow.setWindowTitle(_translate("BooksWindow", "Catalogue"))
        self.label19.setText(_translate("BooksWindow", "Library"))
        self.log_credits_24.setText(_translate("BooksWindow", "My account"))
        self.log_credits_25.setText(_translate("BooksWindow", "Books"))
        self.MY_ACCOUNT.setText(_translate("BooksWindow", "My account"))
        self.BOOKS.setText(_translate("BooksWindow", "Books"))
        self.REQUEST.setText(_translate("BooksWindow", "Request"))
        item = self.TABLE.horizontalHeaderItem(0)
        item.setText(_translate("BooksWindow", "code"))
        item = self.TABLE.horizontalHeaderItem(1)
        item.setText(_translate("BooksWindow", "Title"))
        item = self.TABLE.horizontalHeaderItem(2)
        item.setText(_translate("BooksWindow", "Author"))
        item = self.TABLE.horizontalHeaderItem(3)
        item.setText(_translate("BooksWindow", "Release Year"))
        item = self.TABLE.horizontalHeaderItem(4)
        item.setText(_translate("BooksWindow", "Status"))
        self.label20.setText(_translate("BooksWindow", "Catalogue"))
        self.SUBMIT.setText(_translate("BooksWindow", "Submit"))
        self.TITLE.setPlaceholderText(_translate("BooksWindow", "Title"))
    def search_book(self):
        while (self.TABLE.rowCount() > 0):
                self.TABLE.removeRow(0)
                    
        if self.TITLE.text() !="":    
                
                client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client2.connect(('127.0.0.1', 12397 ))
                request =self.TITLE.text().lower().split()
                request = "|".join(request)
                
                client2.send(str.encode(request))
                response = client2.recv(2048)
                response = response.decode()
                response = re.sub('[\'()]', '', response)
                response = response.split(",")
                client2.close()
                self.TABLE.insertRow(0)
                
                for i in range(len(response)):
                       
                        if i%5==0: 
                            self.TABLE.setItem(0 , i%5,QtWidgets.QTableWidgetItem(response[i].upper()))       
                        else:
                                self.TABLE.setItem(0 , i%5,QtWidgets.QTableWidgetItem(response[i]))
                                if i%5 == 4 and i!=len(response)-1:
                                   self.TABLE.insertRow(0)

                                              
        else:
                print("")        
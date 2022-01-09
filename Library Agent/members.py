# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Agent_members.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MembersWidnow(object):
    def setupUi(self, MembersWidnow):
        MembersWidnow.setObjectName("MembersWidnow")
        MembersWidnow.resize(1179, 723)
        MembersWidnow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.MembersWindow = QtWidgets.QWidget(MembersWidnow)
        self.MembersWindow.setObjectName("MembersWindow")
        self.frame_5 = QtWidgets.QFrame(self.MembersWindow)
        self.frame_5.setGeometry(QtCore.QRect(0, -10, 1181, 91))
        self.frame_5.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: rgb(28, 33, 40);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label20 = QtWidgets.QLabel(self.frame_5)
        self.label20.setGeometry(QtCore.QRect(10, 0, 411, 71))
        self.label20.setStyleSheet("font: 63 italic 30pt \"URW Bookman\";\n"
"color:white;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label20.setObjectName("label20")
        self.icon = QtWidgets.QPushButton(self.frame_5)
        self.icon.setGeometry(QtCore.QRect(380, 10, 91, 61))
        self.icon.setStyleSheet("background-color: rgba(42, 41, 41, 0);")
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/yassine/Library/Library/Library Agent/Assets/milky-way.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(50, 50))
        self.icon.setObjectName("icon")
        self.MANAGE_BOOKS = QtWidgets.QPushButton(self.frame_5)
        self.MANAGE_BOOKS.setGeometry(QtCore.QRect(1010, 20, 151, 61))
        self.MANAGE_BOOKS.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    \n"
"    background-color: rgb(26, 95, 180);\n"
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
        icon1.addPixmap(QtGui.QPixmap("/home/yassine/Library/Library/Library Agent/Assets/programmer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MANAGE_BOOKS.setIcon(icon1)
        self.MANAGE_BOOKS.setIconSize(QtCore.QSize(25, 25))
        self.MANAGE_BOOKS.setObjectName("MANAGE_BOOKS")
        self.Members_table = QtWidgets.QTableWidget(self.MembersWindow)
        self.Members_table.setGeometry(QtCore.QRect(570, 130, 591, 561))
        self.Members_table.setStyleSheet("color:white;\n"
"border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: rgb(34, 39, 46);")
        self.Members_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Members_table.setObjectName("Members_table")
        self.Members_table.setColumnCount(6)
        self.Members_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Members_table.setHorizontalHeaderItem(5, item)
        self.label22 = QtWidgets.QLabel(self.MembersWindow)
        self.label22.setGeometry(QtCore.QRect(50, 260, 101, 31))
        self.label22.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label22.setObjectName("label22")
        self.label23 = QtWidgets.QLabel(self.MembersWindow)
        self.label23.setGeometry(QtCore.QRect(50, 440, 61, 31))
        self.label23.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23.setObjectName("label23")
        self.label21 = QtWidgets.QLabel(self.MembersWindow)
        self.label21.setGeometry(QtCore.QRect(50, 180, 101, 31))
        self.label21.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21.setObjectName("label21")
        self.FIRST_NAME = QtWidgets.QLineEdit(self.MembersWindow)
        self.FIRST_NAME.setGeometry(QtCore.QRect(50, 210, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.FIRST_NAME.setFont(font)
        self.FIRST_NAME.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.FIRST_NAME.setMaxLength(100)
        self.FIRST_NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.FIRST_NAME.setDragEnabled(True)
        self.FIRST_NAME.setPlaceholderText("")
        self.FIRST_NAME.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FIRST_NAME.setClearButtonEnabled(True)
        self.FIRST_NAME.setObjectName("FIRST_NAME")
        self.LAST_NAME = QtWidgets.QLineEdit(self.MembersWindow)
        self.LAST_NAME.setGeometry(QtCore.QRect(50, 290, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.LAST_NAME.setFont(font)
        self.LAST_NAME.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.LAST_NAME.setMaxLength(100)
        self.LAST_NAME.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.LAST_NAME.setDragEnabled(True)
        self.LAST_NAME.setPlaceholderText("")
        self.LAST_NAME.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.LAST_NAME.setClearButtonEnabled(True)
        self.LAST_NAME.setObjectName("LAST_NAME")
        self.PHONE = QtWidgets.QLineEdit(self.MembersWindow)
        self.PHONE.setGeometry(QtCore.QRect(110, 470, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.PHONE.setFont(font)
        self.PHONE.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.PHONE.setMaxLength(10)
        self.PHONE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PHONE.setDragEnabled(True)
        self.PHONE.setPlaceholderText("")
        self.PHONE.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PHONE.setClearButtonEnabled(True)
        self.PHONE.setObjectName("PHONE")
        self.frame_15 = QtWidgets.QFrame(self.MembersWindow)
        self.frame_15.setGeometry(QtCore.QRect(10, 90, 551, 601))
        self.frame_15.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label20_2 = QtWidgets.QLabel(self.frame_15)
        self.label20_2.setGeometry(QtCore.QRect(160, 0, 211, 71))
        self.label20_2.setStyleSheet("font: 63 italic 22pt \"URW Bookman\";\n"
"color:black;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label20_2.setObjectName("label20_2")
        self.DELETE = QtWidgets.QPushButton(self.frame_15)
        self.DELETE.setGeometry(QtCore.QRect(100, 470, 341, 41))
        self.DELETE.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(26, 95, 180);\n"
"    border: 1px solid white;\n"
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
        icon2.addPixmap(QtGui.QPixmap("/home/yassine/Library/Library/Library Agent/Assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DELETE.setIcon(icon2)
        self.DELETE.setIconSize(QtCore.QSize(20, 20))
        self.DELETE.setObjectName("DELETE")
        self.EMAIL_ADDRESS = QtWidgets.QLineEdit(self.frame_15)
        self.EMAIL_ADDRESS.setGeometry(QtCore.QRect(40, 290, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.EMAIL_ADDRESS.setFont(font)
        self.EMAIL_ADDRESS.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.EMAIL_ADDRESS.setMaxLength(100)
        self.EMAIL_ADDRESS.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EMAIL_ADDRESS.setDragEnabled(True)
        self.EMAIL_ADDRESS.setPlaceholderText("")
        self.EMAIL_ADDRESS.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.EMAIL_ADDRESS.setClearButtonEnabled(True)
        self.EMAIL_ADDRESS.setObjectName("EMAIL_ADDRESS")
        self.label23_2 = QtWidgets.QLabel(self.frame_15)
        self.label23_2.setGeometry(QtCore.QRect(40, 260, 131, 31))
        self.label23_2.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23_2 = QtWidgets.QLabel(self.frame_15)
        self.label23_2.setGeometry(QtCore.QRect(40, 260, 131, 31))
        self.label23_2.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23_2.setObjectName("label23_2")
        self.label23_4 = QtWidgets.QLabel(self.frame_15)
        self.label23_4.setGeometry(QtCore.QRect(330, 170, 121, 31))
        self.label23_4.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23_4.setObjectName("label23_4")
        self.ID = QtWidgets.QLineEdit(self.frame_15)
        self.ID.setGeometry(QtCore.QRect(330, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ID.setFont(font)
        self.ID.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.ID.setMaxLength(10)
        self.ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ID.setDragEnabled(True)
        self.ID.setPlaceholderText("")
        self.ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")
        self.delete_book_5 = QtWidgets.QPushButton(self.frame_15)
        self.delete_book_5.setGeometry(QtCore.QRect(40, 370, 61, 51))
        self.delete_book_5.setStyleSheet("font: 75 13pt \"Ubuntu\";")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/yassine/Library/Library/Library Agent/Assets/algeria.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_book_5.setIcon(icon5)
        self.delete_book_5.setIconSize(QtCore.QSize(20, 20))
        self.delete_book_5.setObjectName("delete_book_5")
        self.SEARCH_FIELD = QtWidgets.QLineEdit(self.MembersWindow)
        self.SEARCH_FIELD.setGeometry(QtCore.QRect(590, 90, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.SEARCH_FIELD.setFont(font)
        self.SEARCH_FIELD.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.SEARCH_FIELD.setMaxLength(100)
        self.SEARCH_FIELD.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.SEARCH_FIELD.setDragEnabled(True)
        self.SEARCH_FIELD.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.SEARCH_FIELD.setClearButtonEnabled(True)
        self.SEARCH_FIELD.setObjectName("SEARCH_FIELD")
        self.SUBMIT = QtWidgets.QPushButton(self.MembersWindow)
        self.SUBMIT.setGeometry(QtCore.QRect(990, 90, 91, 31))
        self.DISPLAY_ALL = QtWidgets.QPushButton(self.MembersWindow)
        self.DISPLAY_ALL.setGeometry(QtCore.QRect(1080, 90, 91, 31))
        self.SUBMIT.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(36, 31, 49);\n"
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
        self.DISPLAY_ALL.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(36, 31, 49);\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/yassine/Library/Library/Library Agent/Assets/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SUBMIT.setIcon(icon6)
        self.SUBMIT.setIconSize(QtCore.QSize(17, 17))
        self.SUBMIT.setObjectName("SUBMIT")
        self.frame_17 = QtWidgets.QFrame(self.MembersWindow)
        self.frame_17.setGeometry(QtCore.QRect(460, 0, 321, 81))
        self.frame_17.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color:white;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label21_3 = QtWidgets.QLabel(self.frame_17)
        self.label21_3.setGeometry(QtCore.QRect(20, 0, 281, 31))
        self.label21_3.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21_3.setObjectName("label21_3")
        self.NUMBER_OF_BOOKS = QtWidgets.QLineEdit(self.frame_17)
        self.NUMBER_OF_BOOKS.setGeometry(QtCore.QRect(40, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.NUMBER_OF_BOOKS.setFont(font)
        self.NUMBER_OF_BOOKS.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"color:black;"
"")
        self.NUMBER_OF_BOOKS.setMaxLength(100)
        self.NUMBER_OF_BOOKS.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NUMBER_OF_BOOKS.setDragEnabled(True)
        self.NUMBER_OF_BOOKS.setReadOnly(True)
        self.NUMBER_OF_BOOKS.setPlaceholderText("")
        self.NUMBER_OF_BOOKS.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NUMBER_OF_BOOKS.setClearButtonEnabled(False)
        self.NUMBER_OF_BOOKS.setObjectName("NUMBER_OF_BOOKS")
        self.frame_18 = QtWidgets.QFrame(self.MembersWindow)
        self.frame_18.setGeometry(QtCore.QRect(790, 0, 221, 81))
        self.frame_18.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: transparent;\n"
"color:white;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label21_4 = QtWidgets.QLabel(self.frame_18)
        self.label21_4.setGeometry(QtCore.QRect(10, 0, 191, 31))
        self.label21_4.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21_4.setObjectName("label21_4")
        self.NUMBER_OF_MEMBERS = QtWidgets.QLineEdit(self.frame_18)
        self.NUMBER_OF_MEMBERS.setGeometry(QtCore.QRect(40, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.NUMBER_OF_MEMBERS.setFont(font)
        self.NUMBER_OF_MEMBERS.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"color:black;"
"")
        self.NUMBER_OF_MEMBERS.setMaxLength(100)
        self.NUMBER_OF_MEMBERS.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NUMBER_OF_MEMBERS.setDragEnabled(True)
        self.NUMBER_OF_MEMBERS.setReadOnly(True)
        self.NUMBER_OF_MEMBERS.setPlaceholderText("")
        self.NUMBER_OF_MEMBERS.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NUMBER_OF_MEMBERS.setClearButtonEnabled(False)
        self.NUMBER_OF_MEMBERS.setObjectName("NUMBER_OF_MEMBERS")
        
        self.frame_15.raise_()
        self.frame_5.raise_()
        self.Members_table.raise_()
        self.label22.raise_()
        self.label23.raise_()
        self.label21.raise_()
        self.FIRST_NAME.raise_()
        self.LAST_NAME.raise_()
        self.PHONE.raise_()
        self.SEARCH_FIELD.raise_()
        self.SUBMIT.raise_()
        self.frame_17.raise_()
        self.frame_18.raise_()
        
        #MembersWidnow.setCentralWidget(self.MembersWindow)
        self.menubar = QtWidgets.QMenuBar(MembersWidnow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 22))
        self.menubar.setObjectName("menubar")
        #MembersWidnow.setMenuBar(self.menubar)

        self.retranslateUi(MembersWidnow)
        QtCore.QMetaObject.connectSlotsByName(MembersWidnow)

    def retranslateUi(self, MembersWidnow):
        _translate = QtCore.QCoreApplication.translate
        MembersWidnow.setWindowTitle(_translate("MembersWidnow", "Manage Members"))
        self.label20.setText(_translate("MembersWidnow", "Library Agent Space"))
        self.MANAGE_BOOKS.setText(_translate("MembersWidnow", "Manage Books"))
        item = self.Members_table.horizontalHeaderItem(0)
        item.setText(_translate("MembersWidnow", "ID"))
        item = self.Members_table.horizontalHeaderItem(1)
        item.setText(_translate("MembersWidnow", "First Name"))
        item = self.Members_table.horizontalHeaderItem(2)
        item.setText(_translate("MembersWidnow", "Last Name"))
        item = self.Members_table.horizontalHeaderItem(3)
        item.setText(_translate("MembersWidnow", "Email"))
        item = self.Members_table.horizontalHeaderItem(4)
        item.setText(_translate("MembersWidnow", "Phone"))
        item = self.Members_table.horizontalHeaderItem(5)
        item.setText(_translate("MembersWidnow", "Password"))
        self.label22.setText(_translate("MembersWidnow", "Last Name"))
        self.label23.setText(_translate("MembersWidnow", "Phone"))
        self.label21.setText(_translate("MembersWidnow", "First Name"))
        self.label20_2.setText(_translate("MembersWidnow", "Delete Member"))
        self.DELETE.setText(_translate("MembersWidnow", "DELETE"))
        self.label23_2.setText(_translate("MembersWidnow", "Email Address"))
        self.label23_4.setText(_translate("MembersWidnow", "ID"))
        self.delete_book_5.setText(_translate("MembersWidnow", "+213"))
        self.SEARCH_FIELD.setPlaceholderText(_translate("MembersWidnow", "Enter any Member First or Last Name Or ID"))
        self.SUBMIT.setText(_translate("MembersWidnow", "Submit"))
        self.DISPLAY_ALL.setText(_translate("MembersWidnow", "display all"))
        self.label21_3.setText(_translate("BooksWindow", "Number of Books in the library"))
        self.label21_4.setText(_translate("BooksWindow", "Number of Members"))
        
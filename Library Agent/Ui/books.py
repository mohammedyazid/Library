

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BooksWindow(object):
    def setupUi(self, BooksWindow):
        BooksWindow.setObjectName("BooksWindow")
        BooksWindow.resize(1179, 723)
        BooksWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.BookWindow = QtWidgets.QWidget(BooksWindow)
        self.BookWindow.setObjectName("BookWindow")
        self.frame_5 = QtWidgets.QFrame(self.BookWindow)
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
        icon.addPixmap(QtGui.QPixmap("Library Agent/Ui/Assets/milky-way.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(50, 50))
        self.icon.setObjectName("icon")
        self.MANAGE_MEMBERS = QtWidgets.QPushButton(self.frame_5)
        self.MANAGE_MEMBERS.setGeometry(QtCore.QRect(1010, 20, 151, 61))
        self.MANAGE_MEMBERS.setStyleSheet("\n"
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
        icon1.addPixmap(QtGui.QPixmap("Icons/programmer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MANAGE_MEMBERS.setIcon(icon1)
        self.MANAGE_MEMBERS.setIconSize(QtCore.QSize(25, 25))
        self.MANAGE_MEMBERS.setObjectName("MANAGE_MEMBERS")
        self.Books_table = QtWidgets.QTableWidget(self.BookWindow)
        self.Books_table.setGeometry(QtCore.QRect(590, 130, 571, 561))
        self.Books_table.setStyleSheet("color:white;\n"
"border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: rgb(34, 39, 46);")
        self.Books_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Books_table.setObjectName("Books_table")
        self.Books_table.setColumnCount(5)
        self.Books_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Books_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Books_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Books_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Books_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Books_table.setHorizontalHeaderItem(4, item)
        self.label22 = QtWidgets.QLabel(self.BookWindow)
        self.label22.setGeometry(QtCore.QRect(260, 130, 91, 31))
        self.label22.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label22.setObjectName("label22")
        self.label23 = QtWidgets.QLabel(self.BookWindow)
        self.label23.setGeometry(QtCore.QRect(50, 200, 121, 31))
        self.label23.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23.setObjectName("label23")
        self.ADD_BOOK = QtWidgets.QPushButton(self.BookWindow)
        self.ADD_BOOK.setGeometry(QtCore.QRect(260, 230, 191, 31))
        self.ADD_BOOK.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    background-color: rgb(36, 31, 49);\n"
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
        icon2.addPixmap(QtGui.QPixmap("Icons/borrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ADD_BOOK.setIcon(icon2)
        self.ADD_BOOK.setIconSize(QtCore.QSize(30, 30))
        self.ADD_BOOK.setObjectName("ADD_BOOK")
        self.label21 = QtWidgets.QLabel(self.BookWindow)
        self.label21.setGeometry(QtCore.QRect(50, 130, 91, 31))
        self.label21.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21.setObjectName("label21")
        self.BOOK_TITLE_ADD = QtWidgets.QLineEdit(self.BookWindow)
        self.BOOK_TITLE_ADD.setGeometry(QtCore.QRect(50, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BOOK_TITLE_ADD.setFont(font)
        self.BOOK_TITLE_ADD.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.BOOK_TITLE_ADD.setMaxLength(100)
        self.BOOK_TITLE_ADD.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.BOOK_TITLE_ADD.setDragEnabled(True)
        self.BOOK_TITLE_ADD.setPlaceholderText("")
        self.BOOK_TITLE_ADD.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.BOOK_TITLE_ADD.setClearButtonEnabled(True)
        self.BOOK_TITLE_ADD.setObjectName("BOOK_TITLE_ADD")
        self.AUTHOR_ADD = QtWidgets.QLineEdit(self.BookWindow)
        self.AUTHOR_ADD.setGeometry(QtCore.QRect(260, 160, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.AUTHOR_ADD.setFont(font)
        self.AUTHOR_ADD.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.AUTHOR_ADD.setMaxLength(100)
        self.AUTHOR_ADD.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.AUTHOR_ADD.setDragEnabled(True)
        self.AUTHOR_ADD.setPlaceholderText("")
        self.AUTHOR_ADD.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.AUTHOR_ADD.setClearButtonEnabled(True)
        self.AUTHOR_ADD.setObjectName("AUTHOR_ADD")
        self.RELEASE_YEAR_ADD = QtWidgets.QLineEdit(self.BookWindow)
        self.RELEASE_YEAR_ADD.setGeometry(QtCore.QRect(50, 230, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.RELEASE_YEAR_ADD.setFont(font)
        self.RELEASE_YEAR_ADD.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.RELEASE_YEAR_ADD.setMaxLength(4)
        self.RELEASE_YEAR_ADD.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.RELEASE_YEAR_ADD.setDragEnabled(True)
        self.RELEASE_YEAR_ADD.setPlaceholderText("")
        self.RELEASE_YEAR_ADD.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.RELEASE_YEAR_ADD.setClearButtonEnabled(True)
        self.RELEASE_YEAR_ADD.setObjectName("RELEASE_YEAR_ADD")
        self.frame_15 = QtWidgets.QFrame(self.BookWindow)
        self.frame_15.setGeometry(QtCore.QRect(10, 90, 551, 211))
        self.frame_15.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label20_2 = QtWidgets.QLabel(self.frame_15)
        self.label20_2.setGeometry(QtCore.QRect(170, -10, 171, 71))
        self.label20_2.setStyleSheet("font: 63 italic 22pt \"URW Bookman\";\n"
"color:black;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label20_2.setObjectName("label20_2")
        self.frame_16 = QtWidgets.QFrame(self.BookWindow)
        self.frame_16.setGeometry(QtCore.QRect(10, 310, 551, 241))
        self.frame_16.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.SUBMIT_MODIFICATION = QtWidgets.QPushButton(self.frame_16)
        self.SUBMIT_MODIFICATION.setGeometry(QtCore.QRect(290, 110, 181, 41))
        self.SUBMIT_MODIFICATION.setStyleSheet("\n"
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Assets/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SUBMIT_MODIFICATION.setIcon(icon3)
        self.SUBMIT_MODIFICATION.setIconSize(QtCore.QSize(20, 20))
        self.SUBMIT_MODIFICATION.setObjectName("SUBMIT_MODIFICATION")
        self.DELETE = QtWidgets.QPushButton(self.frame_16)
        self.DELETE.setGeometry(QtCore.QRect(290, 170, 181, 41))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Assets/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DELETE.setIcon(icon4)
        self.DELETE.setIconSize(QtCore.QSize(20, 20))
        self.DELETE.setObjectName("DELETE")
        self.label21_2 = QtWidgets.QLabel(self.frame_16)
        self.label21_2.setGeometry(QtCore.QRect(40, 10, 91, 31))
        self.label21_2.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21_2.setObjectName("label21_2")
        self.label22_2 = QtWidgets.QLabel(self.frame_16)
        self.label22_2.setGeometry(QtCore.QRect(40, 150, 91, 31))
        self.label22_2.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label22_2.setObjectName("label22_2")
        self.BOOK_TITLE = QtWidgets.QLineEdit(self.frame_16)
        self.BOOK_TITLE.setGeometry(QtCore.QRect(40, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.BOOK_TITLE.setFont(font)
        self.BOOK_TITLE.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.BOOK_TITLE.setMaxLength(100)
        self.BOOK_TITLE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.BOOK_TITLE.setDragEnabled(True)
        self.BOOK_TITLE.setPlaceholderText("")
        self.BOOK_TITLE.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.BOOK_TITLE.setClearButtonEnabled(True)
        self.BOOK_TITLE.setObjectName("BOOK_TITLE")
        self.AUTHOR = QtWidgets.QLineEdit(self.frame_16)
        self.AUTHOR.setGeometry(QtCore.QRect(40, 180, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.AUTHOR.setFont(font)
        self.AUTHOR.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.AUTHOR.setMaxLength(100)
        self.AUTHOR.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.AUTHOR.setDragEnabled(True)
        self.AUTHOR.setPlaceholderText("")
        self.AUTHOR.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.AUTHOR.setClearButtonEnabled(True)
        self.AUTHOR.setObjectName("AUTHOR")
        self.RELEASE_YEAR = QtWidgets.QLineEdit(self.frame_16)
        self.RELEASE_YEAR.setGeometry(QtCore.QRect(40, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.RELEASE_YEAR.setFont(font)
        self.RELEASE_YEAR.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.RELEASE_YEAR.setMaxLength(4)
        self.RELEASE_YEAR.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.RELEASE_YEAR.setDragEnabled(True)
        self.RELEASE_YEAR.setPlaceholderText("")
        self.RELEASE_YEAR.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.RELEASE_YEAR.setClearButtonEnabled(True)
        self.RELEASE_YEAR.setObjectName("RELEASE_YEAR")
        self.label23_2 = QtWidgets.QLabel(self.frame_16)
        self.label23_2.setGeometry(QtCore.QRect(40, 80, 121, 31))
        self.label23_2.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(65, 191, 64, 0);")
        self.label23_2.setObjectName("label23_2")
        self.SEARCH_FIELD = QtWidgets.QLineEdit(self.BookWindow)
        self.SEARCH_FIELD.setGeometry(QtCore.QRect(590, 90, 471, 31))
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
        self.SUBMIT = QtWidgets.QPushButton(self.BookWindow)
        self.SUBMIT.setGeometry(QtCore.QRect(1070, 90, 91, 31))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Library Management/Windows_Library Agent/Ui/Assets/Ui/Icons/magnifying-glass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SUBMIT.setIcon(icon5)
        self.SUBMIT.setIconSize(QtCore.QSize(17, 17))
        self.SUBMIT.setObjectName("SUBMIT")
        self.frame_17 = QtWidgets.QFrame(self.BookWindow)
        self.frame_17.setGeometry(QtCore.QRect(10, 560, 321, 131))
        self.frame_17.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label21_3 = QtWidgets.QLabel(self.frame_17)
        self.label21_3.setGeometry(QtCore.QRect(20, 10, 281, 31))
        self.label21_3.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21_3.setObjectName("label21_3")
        self.NUMBER_OF_BOOKS = QtWidgets.QLineEdit(self.frame_17)
        self.NUMBER_OF_BOOKS.setGeometry(QtCore.QRect(40, 50, 221, 31))
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
"\n"
"\n"
"")
        self.NUMBER_OF_BOOKS.setMaxLength(100)
        self.NUMBER_OF_BOOKS.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NUMBER_OF_BOOKS.setDragEnabled(True)
        self.NUMBER_OF_BOOKS.setReadOnly(True)
        self.NUMBER_OF_BOOKS.setPlaceholderText("")
        self.NUMBER_OF_BOOKS.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NUMBER_OF_BOOKS.setClearButtonEnabled(True)
        self.NUMBER_OF_BOOKS.setObjectName("NUMBER_OF_BOOKS")
        self.frame_18 = QtWidgets.QFrame(self.BookWindow)
        self.frame_18.setGeometry(QtCore.QRect(340, 560, 221, 131))
        self.frame_18.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label21_4 = QtWidgets.QLabel(self.frame_18)
        self.label21_4.setGeometry(QtCore.QRect(10, 10, 191, 31))
        self.label21_4.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(42, 41, 41, 0);")
        self.label21_4.setObjectName("label21_4")
        self.NUMBER_OF_MEMBERS = QtWidgets.QLineEdit(self.frame_18)
        self.NUMBER_OF_MEMBERS.setGeometry(QtCore.QRect(40, 50, 141, 31))
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
"\n"
"\n"
"")
        self.NUMBER_OF_MEMBERS.setMaxLength(100)
        self.NUMBER_OF_MEMBERS.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.NUMBER_OF_MEMBERS.setDragEnabled(True)
        self.NUMBER_OF_MEMBERS.setReadOnly(True)
        self.NUMBER_OF_MEMBERS.setPlaceholderText("")
        self.NUMBER_OF_MEMBERS.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.NUMBER_OF_MEMBERS.setClearButtonEnabled(True)
        self.NUMBER_OF_MEMBERS.setObjectName("NUMBER_OF_MEMBERS")
        self.frame_15.raise_()
        self.frame_5.raise_()
        self.Books_table.raise_()
        self.label22.raise_()
        self.label23.raise_()
        self.ADD_BOOK.raise_()
        self.label21.raise_()
        self.BOOK_TITLE_ADD.raise_()
        self.AUTHOR_ADD.raise_()
        self.RELEASE_YEAR_ADD.raise_()
        self.frame_16.raise_()
        self.SEARCH_FIELD.raise_()
        self.SUBMIT.raise_()
        self.frame_17.raise_()
        self.frame_18.raise_()
        #BooksWindow.setCentralWidget(self.BookWindow)
        self.menubar = QtWidgets.QMenuBar(BooksWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 22))
        self.menubar.setObjectName("menubar")
        #BooksWindow.setMenuBar(self.menubar)

        self.retranslateUi(BooksWindow)
        QtCore.QMetaObject.connectSlotsByName(BooksWindow)

    def retranslateUi(self, BooksWindow):
        _translate = QtCore.QCoreApplication.translate
        BooksWindow.setWindowTitle(_translate("BooksWindow", "Manage Books"))
        self.label20.setText(_translate("BooksWindow", "Library Agent Space"))
        self.MANAGE_MEMBERS.setText(_translate("BooksWindow", "Manage Members "))
        item = self.Books_table.horizontalHeaderItem(0)
        item.setText(_translate("BooksWindow", "code"))
        item = self.Books_table.horizontalHeaderItem(1)
        item.setText(_translate("BooksWindow", "Title"))
        item = self.Books_table.horizontalHeaderItem(2)
        item.setText(_translate("BooksWindow", "Author"))
        item = self.Books_table.horizontalHeaderItem(3)
        item.setText(_translate("BooksWindow", "Release Year"))
        item = self.Books_table.horizontalHeaderItem(4)
        item.setText(_translate("BooksWindow", "Status"))
        self.label22.setText(_translate("BooksWindow", "Author"))
        self.label23.setText(_translate("BooksWindow", "Release Year"))
        self.ADD_BOOK.setText(_translate("BooksWindow", "Add Book"))
        self.label21.setText(_translate("BooksWindow", "Book Title"))
        self.label20_2.setText(_translate("BooksWindow", "Add a Book"))
        self.SUBMIT_MODIFICATION.setText(_translate("BooksWindow", "Submit Modification"))
        self.DELETE.setText(_translate("BooksWindow", "dELETE"))
        self.label21_2.setText(_translate("BooksWindow", "Book Title"))
        self.label22_2.setText(_translate("BooksWindow", "Author"))
        self.label23_2.setText(_translate("BooksWindow", "Release Year"))
        self.SEARCH_FIELD.setPlaceholderText(_translate("BooksWindow", "Title..."))
        self.SUBMIT.setText(_translate("BooksWindow", "Submit"))
        self.label21_3.setText(_translate("BooksWindow", "Number of Books in the library"))
        self.label21_4.setText(_translate("BooksWindow", "Number of Members"))

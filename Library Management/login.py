# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Path import path

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        self.path = path()
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1128, 629)
        LoginWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, -10, 1131, 321))
        self.frame_2.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: rgb(28, 113, 216);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label1 = QtWidgets.QLabel(self.frame_2)
        self.label1.setGeometry(QtCore.QRect(160, 60, 221, 71))
        self.label1.setStyleSheet("font: 63 italic 40pt \"URW Bookman\";\n"
"color:white;")
        self.label1.setObjectName("label1")
        self.ABOUT = QtWidgets.QPushButton(self.frame_2)
        self.ABOUT.setGeometry(QtCore.QRect(170, 270, 171, 41))
        self.ABOUT.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    border:3px solid white;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 17px;\n"
"    background-color : transparent;\n"
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
        self.ABOUT.setObjectName("ABOUT")
        self.icon2 = QtWidgets.QPushButton(self.frame_2)
        self.icon2.setGeometry(QtCore.QRect(290, 60, 89, 41))
        self.icon2.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.path+"graduate-cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon2.setIcon(icon)
        self.icon2.setIconSize(QtCore.QSize(50, 50))
        self.icon2.setObjectName("icon2")
        self.icon1 = QtWidgets.QPushButton(self.frame_2)
        self.icon1.setGeometry(QtCore.QRect(160, 130, 191, 111))
        self.icon1.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(self.path+"online-library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon1.setIcon(icon1)
        self.icon1.setIconSize(QtCore.QSize(100, 100))
        self.icon1.setObjectName("icon1")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(540, 20, 521, 561))
        self.frame.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SIGN_UP = QtWidgets.QPushButton(self.frame)
        self.SIGN_UP.setGeometry(QtCore.QRect(250, 400, 81, 41))
        self.SIGN_UP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SIGN_UP.setStyleSheet("QPushButton{background-color:transparent;\n"
"color: rgb(46, 194, 126);\n"
"font: 75 12pt \"Ubuntu\";\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"font:serif;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(46, 194, 126);\n"
"font: 75 15pt \"Ubuntu\";\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"font:serif;\n"
"}")
        self.SIGN_UP.setObjectName("SIGN_UP")
        self.label5 = QtWidgets.QLabel(self.frame)
        self.label5.setGeometry(QtCore.QRect(110, 190, 111, 17))
        self.label5.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label5.setObjectName("label5")
        self.label6 = QtWidgets.QLabel(self.frame)
        self.label6.setGeometry(QtCore.QRect(110, 270, 111, 20))
        self.label6.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label6.setObjectName("label6")
        self.SIGN_IN = QtWidgets.QPushButton(self.frame)
        self.SIGN_IN.setGeometry(QtCore.QRect(110, 360, 261, 41))
        self.SIGN_IN.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: rgb(0, 137, 236);;\n"
"    border-radius: 5px;\n"
"    border:3px solid rgb(0, 137, 236);;\n"
"    font-family:\'Montserrat\', sans-serif;\n"
"    text-transform: uppercase;\n"
"    text-align: center;\n"
"    line-height: 1;\n"
"    font-size: 17px;\n"
"    background-color : transparent;\n"
"    padding: 10px;\n"
"    outline: none;\n"
"    \n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    color: white;\n"
"    background-color: rgb(0, 137, 236);;\n"
"}\n"
"")
        self.SIGN_IN.setObjectName("SIGN_IN")
        self.label7 = QtWidgets.QLabel(self.frame)
        self.label7.setGeometry(QtCore.QRect(120, 410, 131, 21))
        self.label7.setStyleSheet("font: 75 12pt \"Ubuntu\";")
        self.label7.setObjectName("label7")
        self.label4 = QtWidgets.QLabel(self.frame)
        self.label4.setGeometry(QtCore.QRect(330, 20, 91, 41))
        self.label4.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label4.setObjectName("label4")
        self.label3 = QtWidgets.QLabel(self.frame)
        self.label3.setGeometry(QtCore.QRect(240, 20, 91, 41))
        self.label3.setStyleSheet("font: 75 20pt \"Ubuntu\";\n"
"color:rgb(28, 113, 216);")
        self.label3.setObjectName("label3")
        self.label2 = QtWidgets.QLabel(self.frame)
        self.label2.setGeometry(QtCore.QRect(80, 20, 161, 41))
        self.label2.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label2.setObjectName("label2")
        self.icon3 = QtWidgets.QPushButton(self.frame)
        self.icon3.setGeometry(QtCore.QRect(130, 60, 191, 111))
        self.icon3.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(self.path+"login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon3.setIcon(icon2)
        self.icon3.setIconSize(QtCore.QSize(100, 100))
        self.icon3.setObjectName("icon3")
        self.ID = QtWidgets.QLineEdit(self.frame)
        self.ID.setGeometry(QtCore.QRect(100, 210, 281, 31))
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
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.ID.setMaxLength(10)
        self.ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.ID.setDragEnabled(True)
        self.ID.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ID.setClearButtonEnabled(True)
        self.ID.setObjectName("ID")
        self.PASSWORD = QtWidgets.QLineEdit(self.frame)
        self.PASSWORD.setGeometry(QtCore.QRect(100, 290, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.PASSWORD.setFont(font)
        self.PASSWORD.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 13pt \"Ubuntu Mono\";\n"
"\n"
"\n"
"")
        self.PASSWORD.setMaxLength(2000)
        self.PASSWORD.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PASSWORD.setDragEnabled(True)
        self.PASSWORD.setPlaceholderText("")
        self.PASSWORD.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PASSWORD.setClearButtonEnabled(True)
        self.PASSWORD.setObjectName("PASSWORD")
        self.lg_error = QtWidgets.QLabel(self.centralwidget)
        self.lg_error.setGeometry(QtCore.QRect(620, 350, 321, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.lg_error.setFont(font)
        self.lg_error.setStyleSheet("color: rgb(224, 27, 36);\n"
"background-color: rgba(42, 41, 41, 0);")
        self.lg_error.setText("")
        self.lg_error.setTextFormat(QtCore.Qt.AutoText)
        self.lg_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lg_error.setWordWrap(False)
        self.lg_error.setObjectName("lg_error")
        #LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 22))
        self.menubar.setObjectName("menubar")
        #LoginWindow.setMenuBar(self.menubar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label1.setText(_translate("LoginWindow", "Library"))
        self.ABOUT.setText(_translate("LoginWindow", "ABOUT"))
        self.SIGN_UP.setText(_translate("LoginWindow", "Sign Up"))
        self.label5.setText(_translate("LoginWindow", "ID"))
        self.label6.setText(_translate("LoginWindow", "Password"))
        self.SIGN_IN.setText(_translate("LoginWindow", "Sign In"))
        self.label7.setText(_translate("LoginWindow", "Not a member yet?"))
        self.label4.setText(_translate("LoginWindow", "account"))
        self.label3.setText(_translate("LoginWindow", "Library"))
        self.label2.setText(_translate("LoginWindow", "Log into Your"))
        self.ID.setPlaceholderText(_translate("LoginWindow", "193800...."))

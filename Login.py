

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(970, 612)
        LoginWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(490, 30, 441, 541))
        self.frame.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.log_SignIn = QtWidgets.QPushButton(self.frame)
        self.log_SignIn.setGeometry(QtCore.QRect(90, 360, 261, 41))
        self.log_SignIn.setStyleSheet("\n"
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
        self.log_SignIn.setObjectName("log_SignIn")
        self.log_idTF = QtWidgets.QTextEdit(self.frame)
        self.log_idTF.setGeometry(QtCore.QRect(60, 200, 321, 31))
        self.log_idTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.log_idTF.setObjectName("log_idTF")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 180, 111, 17))
        self.label.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 247, 111, 20))
        self.label_2.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.log_passTF = QtWidgets.QTextEdit(self.frame)
        self.log_passTF.setGeometry(QtCore.QRect(60, 270, 321, 31))
        self.log_passTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.log_passTF.setObjectName("log_passTF")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 50, 161, 41))
        self.label_4.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(220, 50, 181, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Ubuntu\";\n"
"color:rgb(0, 137, 236)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(310, 50, 91, 41))
        self.label_6.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 100, 89, 71))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/yassine/repo/Icons/id.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(100, 410, 161, 41))
        self.label_7.setStyleSheet("font: 75 12pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.log_SignUp = QtWidgets.QPushButton(self.frame)
        self.log_SignUp.setGeometry(QtCore.QRect(240, 410, 81, 41))
        self.log_SignUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_SignUp.setStyleSheet("QPushButton{background-color:transparent;\n"
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
        self.log_SignUp.setObjectName("log_SignUp")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 951, 331))
        self.frame_2.setStyleSheet("background-color: rgb(0, 137, 236);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(150, 60, 171, 61))
        self.label_3.setStyleSheet("font: 63 italic 34pt \"URW Bookman\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.log_credits = QtWidgets.QPushButton(self.frame_2)
        self.log_credits.setGeometry(QtCore.QRect(150, 280, 171, 41))
        self.log_credits.setStyleSheet("\n"
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
        self.log_credits.setObjectName("log_credits")
        self.lib_icon = QtWidgets.QPushButton(self.frame_2)
        self.lib_icon.setEnabled(True)
        self.lib_icon.setGeometry(QtCore.QRect(100, 130, 261, 111))
        self.lib_icon.setStyleSheet("background-color: rgb(0, 137, 236);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.lib_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/yassine/repo/Icons/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lib_icon.setIcon(icon1)
        self.lib_icon.setIconSize(QtCore.QSize(100, 100))
        self.lib_icon.setObjectName("lib_icon")
        self.log_help = QtWidgets.QPushButton(self.centralwidget)
        self.log_help.setGeometry(QtCore.QRect(160, 350, 171, 41))
        self.log_help.setStyleSheet("\n"
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
        self.log_help.setObjectName("log_help")
        self.frame_2.raise_()
        self.frame.raise_()
        self.log_help.raise_()
        
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 22))
        self.menubar.setObjectName("menubar")
        
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.log_SignIn.setText(_translate("LoginWindow", "Sign In"))
        self.log_idTF.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.log_idTF.setPlaceholderText(_translate("LoginWindow", "3800...."))
        self.label.setText(_translate("LoginWindow", "STUDENT ID"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.log_passTF.setHtml(_translate("LoginWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("LoginWindow", "Log into Your"))
        self.label_5.setText(_translate("LoginWindow", "Library"))
        self.label_6.setText(_translate("LoginWindow", "account"))
        self.label_7.setText(_translate("LoginWindow", "Not a member yet?"))
        self.log_SignUp.setText(_translate("LoginWindow", "Sign Up"))
        self.label_3.setText(_translate("LoginWindow", "Library"))
        self.log_credits.setText(_translate("LoginWindow", "Credits"))
        self.log_help.setText(_translate("LoginWindow", "Help"))


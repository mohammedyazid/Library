
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(970, 612)
        RegisterWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
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
        
        self.reg_SignUp = QtWidgets.QPushButton(self.frame)
        self.reg_SignUp.setGeometry(QtCore.QRect(90, 470, 261, 41))
        self.reg_SignUp.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: rgb(0, 137, 236);;\n"
"    border-radius: 10px;\n"
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
        self.reg_SignUp.setObjectName("reg_SignUp")
        self.reg_idTF = QtWidgets.QTextEdit(self.frame)
        self.reg_idTF.setGeometry(QtCore.QRect(50, 250, 201, 31))
        self.reg_idTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_idTF.setObjectName("reg_idTF")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 220, 111, 17))
        self.label.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 290, 111, 20))
        self.label_2.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.reg_passTF = QtWidgets.QTextEdit(self.frame)
        self.reg_passTF.setGeometry(QtCore.QRect(50, 320, 201, 31))
        self.reg_passTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_passTF.setObjectName("reg_passTF")
        self.reg_phoneTF = QtWidgets.QTextEdit(self.frame)
        self.reg_phoneTF.setGeometry(QtCore.QRect(270, 250, 121, 31))
        self.reg_phoneTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_phoneTF.setObjectName("reg_phoneTF")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(270, 220, 141, 17))
        self.label_7.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.reg_fnameTF = QtWidgets.QTextEdit(self.frame)
        self.reg_fnameTF.setGeometry(QtCore.QRect(50, 100, 151, 31))
        self.reg_fnameTF.setToolTip("")
        self.reg_fnameTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_fnameTF.setPlaceholderText("")
        self.reg_fnameTF.setObjectName("reg_fnameTF")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 60, 121, 31))
        self.label_8.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_8.setObjectName("label_8")
        self.reg_confpassTF = QtWidgets.QTextEdit(self.frame)
        self.reg_confpassTF.setGeometry(QtCore.QRect(50, 390, 201, 31))
        self.reg_confpassTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_confpassTF.setObjectName("reg_confpassTF")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 360, 181, 20))
        self.label_9.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_9.setObjectName("label_9")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 101, 41))
        self.label_4.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 81, 41))
        self.label_5.setStyleSheet("font: 75 20pt \"Ubuntu\";\n"
"color:rgb(0, 137, 236)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(250, 10, 151, 41))
        self.label_6.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(50, 430, 241, 23))
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.reg_mailTF = QtWidgets.QTextEdit(self.frame)
        self.reg_mailTF.setGeometry(QtCore.QRect(50, 170, 341, 31))
        self.reg_mailTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_mailTF.setObjectName("reg_mailTF")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(50, 140, 141, 17))
        self.label_10.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_10.setObjectName("label_10")
        self.reg_nameTF = QtWidgets.QTextEdit(self.frame)
        self.reg_nameTF.setGeometry(QtCore.QRect(220, 100, 171, 31))
        self.reg_nameTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.reg_nameTF.setPlaceholderText("")
        self.reg_nameTF.setObjectName("reg_nameTF")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(220, 60, 121, 31))
        self.label_11.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label_11.setObjectName("label_11")
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
        self.label_3.setGeometry(QtCore.QRect(140, 40, 171, 61))
        self.label_3.setStyleSheet("font: 63 italic 34pt \"URW Bookman\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(90, 110, 261, 111))
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 137, 236);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.btn_of_return=QtWidgets.QPushButton(self.frame_2)
        self.btn_of_return.setGeometry(QtCore.QRect(5, 5, 41, 41))
        self.btn_of_return.setIcon(QtGui.QIcon('/home/yassine/Desktop/return2.png'))#######################################
        self.reg_credits = QtWidgets.QPushButton(self.frame_2)
        self.reg_credits.setGeometry(QtCore.QRect(130, 280, 171, 41))
        self.reg_credits.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
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
        self.btn_of_return.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    border:3px solid rgb(100, 137, 236);;\n"
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
"    padding-right:20px"
"}\n"
"")        
        self.reg_credits.setObjectName("reg_credits")
        self.reg_help = QtWidgets.QPushButton(self.centralwidget)
        self.reg_help.setGeometry(QtCore.QRect(140, 350, 171, 41))
        self.reg_help.setStyleSheet("\n"
"QPushButton {\n"
"    transition: all .5s ease;\n"
"    color: rgb(0, 137, 236);;\n"
"    border-radius: 10px;\n"
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
        self.reg_help.setObjectName("reg_help")
        self.frame_2.raise_()
        self.frame.raise_()
        self.reg_help.raise_()
        
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 970, 22))
        self.menubar.setObjectName("menubar")
        
        self.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        self.statusbar.setObjectName("statusbar")
        

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        self.reg_SignUp.setText(_translate("RegisterWindow", "Sign Up"))
        self.reg_idTF.setToolTip(_translate("RegisterWindow", "You can find it in your student id card"))
        self.reg_idTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.reg_idTF.setPlaceholderText(_translate("RegisterWindow", "3800...."))
        self.label.setText(_translate("RegisterWindow", "STUDENT ID"))
        self.label_2.setText(_translate("RegisterWindow", "Password"))
        self.reg_passTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.reg_phoneTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.reg_phoneTF.setPlaceholderText(_translate("RegisterWindow", "0655555555"))
        self.label_7.setText(_translate("RegisterWindow", "Phone "))
        self.reg_fnameTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("RegisterWindow", "Family Name"))
        self.reg_confpassTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_9.setText(_translate("RegisterWindow", "Confirme Password"))
        self.label_4.setText(_translate("RegisterWindow", "Create a"))
        self.label_5.setText(_translate("RegisterWindow", "Library"))
        self.label_6.setText(_translate("RegisterWindow", "membership"))
        self.checkBox.setText(_translate("RegisterWindow", "I\'m sure "))
        self.reg_mailTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.reg_mailTF.setPlaceholderText(_translate("RegisterWindow", "...@gmail.com"))
        self.label_10.setText(_translate("RegisterWindow", "Email"))
        self.reg_nameTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("RegisterWindow", "Name"))
        self.label_3.setText(_translate("RegisterWindow", "Library"))
        self.reg_credits.setText(_translate("RegisterWindow", "Credits"))
        self.reg_help.setText(_translate("RegisterWindow", "Help"))
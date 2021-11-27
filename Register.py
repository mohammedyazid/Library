# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(Ui_RegisterWindow, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(970, 612)
        RegisterWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        Ui_RegisterWindow.centralwidget = QtWidgets.QWidget(RegisterWindow)
        Ui_RegisterWindow.centralwidget.setObjectName("centralwidget")
        Ui_RegisterWindow.frame = QtWidgets.QFrame(Ui_RegisterWindow.centralwidget)
        Ui_RegisterWindow.frame.setGeometry(QtCore.QRect(490, 30, 441, 541))
        Ui_RegisterWindow.frame.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        Ui_RegisterWindow.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Ui_RegisterWindow.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        Ui_RegisterWindow.frame.setObjectName("frame")
        Ui_RegisterWindow.reg_SignUp = QtWidgets.QPushButton(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_SignUp.setGeometry(QtCore.QRect(90, 470, 261, 41))
        Ui_RegisterWindow.reg_SignUp.setStyleSheet("\n"
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
        Ui_RegisterWindow.reg_SignUp.setObjectName("reg_SignUp")
        Ui_RegisterWindow.reg_idTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_idTF.setGeometry(QtCore.QRect(50, 250, 201, 31))
        Ui_RegisterWindow.reg_idTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_idTF.setObjectName("reg_idTF")
        Ui_RegisterWindow.label = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label.setGeometry(QtCore.QRect(50, 220, 111, 17))
        Ui_RegisterWindow.label.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label.setObjectName("label")
        Ui_RegisterWindow.label_2 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_2.setGeometry(QtCore.QRect(50, 290, 111, 20))
        Ui_RegisterWindow.label_2.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_2.setObjectName("label_2")
        Ui_RegisterWindow.reg_passTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_passTF.setGeometry(QtCore.QRect(50, 320, 201, 31))
        Ui_RegisterWindow.reg_passTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_passTF.setObjectName("reg_passTF")
        Ui_RegisterWindow.reg_phoneTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_phoneTF.setGeometry(QtCore.QRect(270, 250, 121, 31))
        Ui_RegisterWindow.reg_phoneTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_phoneTF.setObjectName("reg_phoneTF")
        Ui_RegisterWindow.label_7 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_7.setGeometry(QtCore.QRect(270, 220, 141, 17))
        Ui_RegisterWindow.label_7.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_7.setObjectName("label_7")
        Ui_RegisterWindow.reg_fnameTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_fnameTF.setGeometry(QtCore.QRect(50, 100, 151, 31))
        Ui_RegisterWindow.reg_fnameTF.setToolTip("")
        Ui_RegisterWindow.reg_fnameTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_fnameTF.setPlaceholderText("")
        Ui_RegisterWindow.reg_fnameTF.setObjectName("reg_fnameTF")
        Ui_RegisterWindow.label_8 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_8.setGeometry(QtCore.QRect(50, 60, 121, 31))
        Ui_RegisterWindow.label_8.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_8.setObjectName("label_8")
        Ui_RegisterWindow.reg_confpassTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_confpassTF.setGeometry(QtCore.QRect(50, 390, 201, 31))
        Ui_RegisterWindow.reg_confpassTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_confpassTF.setObjectName("reg_confpassTF")
        Ui_RegisterWindow.label_9 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_9.setGeometry(QtCore.QRect(50, 360, 181, 20))
        Ui_RegisterWindow.label_9.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_9.setObjectName("label_9")
        Ui_RegisterWindow.label_4 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_4.setGeometry(QtCore.QRect(50, 10, 101, 41))
        Ui_RegisterWindow.label_4.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        Ui_RegisterWindow.label_4.setObjectName("label_4")
        Ui_RegisterWindow.label_5 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_5.setGeometry(QtCore.QRect(160, 10, 81, 41))
        Ui_RegisterWindow.label_5.setStyleSheet("font: 75 20pt \"Ubuntu\";\n"
"color:rgb(0, 137, 236)")
        Ui_RegisterWindow.label_5.setObjectName("label_5")
        Ui_RegisterWindow.label_6 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_6.setGeometry(QtCore.QRect(250, 10, 151, 41))
        Ui_RegisterWindow.label_6.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        Ui_RegisterWindow.label_6.setObjectName("label_6")
        Ui_RegisterWindow.checkBox = QtWidgets.QCheckBox(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.checkBox.setGeometry(QtCore.QRect(50, 430, 241, 23))
        Ui_RegisterWindow.checkBox.setTristate(False)
        Ui_RegisterWindow.checkBox.setObjectName("checkBox")
        Ui_RegisterWindow.reg_mailTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_mailTF.setGeometry(QtCore.QRect(50, 170, 341, 31))
        Ui_RegisterWindow.reg_mailTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_mailTF.setObjectName("reg_mailTF")
        Ui_RegisterWindow.label_10 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_10.setGeometry(QtCore.QRect(50, 140, 141, 17))
        Ui_RegisterWindow.label_10.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_10.setObjectName("label_10")
        Ui_RegisterWindow.reg_nameTF = QtWidgets.QTextEdit(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.reg_nameTF.setGeometry(QtCore.QRect(220, 100, 171, 31))
        Ui_RegisterWindow.reg_nameTF.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        Ui_RegisterWindow.reg_nameTF.setPlaceholderText("")
        Ui_RegisterWindow.reg_nameTF.setObjectName("reg_nameTF")
        Ui_RegisterWindow.label_11 = QtWidgets.QLabel(Ui_RegisterWindow.frame)
        Ui_RegisterWindow.label_11.setGeometry(QtCore.QRect(220, 60, 121, 31))
        Ui_RegisterWindow.label_11.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        Ui_RegisterWindow.label_11.setObjectName("label_11")
        Ui_RegisterWindow.frame_2 = QtWidgets.QFrame(Ui_RegisterWindow.centralwidget)
        Ui_RegisterWindow.frame_2.setGeometry(QtCore.QRect(10, 10, 951, 331))
        Ui_RegisterWindow.frame_2.setStyleSheet("background-color: rgb(0, 137, 236);\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        Ui_RegisterWindow.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Ui_RegisterWindow.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        Ui_RegisterWindow.frame_2.setObjectName("frame_2")
        Ui_RegisterWindow.label_3 = QtWidgets.QLabel(Ui_RegisterWindow.frame_2)
        Ui_RegisterWindow.label_3.setGeometry(QtCore.QRect(140, 40, 171, 61))
        Ui_RegisterWindow.label_3.setStyleSheet("font: 63 italic 34pt \"URW Bookman\";\n"
"color:white;")
        Ui_RegisterWindow.label_3.setObjectName("label_3")
        Ui_RegisterWindow.pushButton_8 = QtWidgets.QPushButton(Ui_RegisterWindow.frame_2)
        Ui_RegisterWindow.pushButton_8.setGeometry(QtCore.QRect(90, 110, 261, 111))
        Ui_RegisterWindow.pushButton_8.setStyleSheet("background-color: rgb(0, 137, 236);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 20pt \"Ubuntu\";\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border-radius: 10px;\n"
"\n"
"")
        Ui_RegisterWindow.pushButton_8.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Ui_RegisterWindow.pushButton_8.setIcon(icon)
        Ui_RegisterWindow.pushButton_8.setIconSize(QtCore.QSize(100, 100))
        Ui_RegisterWindow.pushButton_8.setObjectName("pushButton_8")
        Ui_RegisterWindow.reg_credits = QtWidgets.QPushButton(Ui_RegisterWindow.frame_2)
        Ui_RegisterWindow.reg_credits.setGeometry(QtCore.QRect(130, 280, 171, 41))
        Ui_RegisterWindow.reg_credits.setStyleSheet("\n"
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
        Ui_RegisterWindow.reg_credits.setObjectName("reg_credits")
        Ui_RegisterWindow.reg_help = QtWidgets.QPushButton(Ui_RegisterWindow.centralwidget)
        Ui_RegisterWindow.reg_help.setGeometry(QtCore.QRect(140, 350, 171, 41))
        Ui_RegisterWindow.reg_help.setStyleSheet("\n"
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
        Ui_RegisterWindow.reg_help.setObjectName("reg_help")
        Ui_RegisterWindow.frame_2.raise_()
        Ui_RegisterWindow.frame.raise_()
        Ui_RegisterWindow.reg_help.raise_()
        RegisterWindow.setCentralWidget(Ui_RegisterWindow.centralwidget)
        Ui_RegisterWindow.menubar = QtWidgets.QMenuBar(RegisterWindow)
        Ui_RegisterWindow.menubar.setGeometry(QtCore.QRect(0, 0, 970, 22))
        Ui_RegisterWindow.menubar.setObjectName("menubar")
        RegisterWindow.setMenuBar(Ui_RegisterWindow.menubar)
        Ui_RegisterWindow.statusbar = QtWidgets.QStatusBar(RegisterWindow)
        Ui_RegisterWindow.statusbar.setObjectName("statusbar")
        RegisterWindow.setStatusBar(Ui_RegisterWindow.statusbar)

        Ui_RegisterWindow.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(Ui_RegisterWindow, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "MainWindow"))
        Ui_RegisterWindow.reg_SignUp.setText(_translate("RegisterWindow", "Sign Up"))
        Ui_RegisterWindow.reg_idTF.setToolTip(_translate("RegisterWindow", "You can find it in your student id card"))
        Ui_RegisterWindow.reg_idTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.reg_idTF.setPlaceholderText(_translate("RegisterWindow", "3800...."))
        Ui_RegisterWindow.label.setText(_translate("RegisterWindow", "STUDENT ID"))
        Ui_RegisterWindow.label_2.setText(_translate("RegisterWindow", "Password"))
        Ui_RegisterWindow.reg_passTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.reg_phoneTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.reg_phoneTF.setPlaceholderText(_translate("RegisterWindow", "0655555555"))
        Ui_RegisterWindow.label_7.setText(_translate("RegisterWindow", "Phone "))
        Ui_RegisterWindow.reg_fnameTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.label_8.setText(_translate("RegisterWindow", "Family Name"))
        Ui_RegisterWindow.reg_confpassTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.label_9.setText(_translate("RegisterWindow", "Confirme Password"))
        Ui_RegisterWindow.label_4.setText(_translate("RegisterWindow", "Create a"))
        Ui_RegisterWindow.label_5.setText(_translate("RegisterWindow", "Library"))
        Ui_RegisterWindow.label_6.setText(_translate("RegisterWindow", "membership"))
        Ui_RegisterWindow.checkBox.setText(_translate("RegisterWindow", "I\'m sure "))
        Ui_RegisterWindow.reg_mailTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.reg_mailTF.setPlaceholderText(_translate("RegisterWindow", "...@gmail.com"))
        Ui_RegisterWindow.label_10.setText(_translate("RegisterWindow", "Email"))
        Ui_RegisterWindow.reg_nameTF.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        Ui_RegisterWindow.label_11.setText(_translate("RegisterWindow", "Name"))
        Ui_RegisterWindow.label_3.setText(_translate("RegisterWindow", "Library"))
        Ui_RegisterWindow.reg_credits.setText(_translate("RegisterWindow", "Credits"))
        Ui_RegisterWindow.reg_help.setText(_translate("RegisterWindow", "Help"))
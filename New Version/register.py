# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        RegisterWindow.setObjectName("RegisterWindow")
        RegisterWindow.resize(1128, 629)
        RegisterWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(RegisterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1131, 321))
        self.frame_3.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color: rgb(28, 113, 216);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label8 = QtWidgets.QLabel(self.frame_3)
        self.label8.setGeometry(QtCore.QRect(160, 60, 221, 71))
        self.label8.setStyleSheet("font: 63 italic 40pt \"URW Bookman\";\n"
"color:white;")
        self.label8.setObjectName("label8")
        self.re_helpbtn = QtWidgets.QPushButton(self.frame_3)
        self.re_helpbtn.setGeometry(QtCore.QRect(170, 270, 171, 41))
        self.re_helpbtn.setStyleSheet("\n"
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
        self.re_helpbtn.setObjectName("re_helpbtn")
        self.icon4 = QtWidgets.QPushButton(self.frame_3)
        self.icon4.setGeometry(QtCore.QRect(290, 60, 89, 41))
        self.icon4.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Ui/Icons/graduate-cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon4.setIcon(icon)
        self.icon4.setIconSize(QtCore.QSize(50, 50))
        self.icon4.setObjectName("icon4")
        self.icon5 = QtWidgets.QPushButton(self.frame_3)
        self.icon5.setGeometry(QtCore.QRect(160, 130, 191, 111))
        self.icon5.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Assets/Ui/Icons/online-library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon5.setIcon(icon1)
        self.icon5.setIconSize(QtCore.QSize(100, 100))
        self.icon5.setObjectName("icon5")
        self.re_backbtn = QtWidgets.QPushButton(self.frame_3)
        self.re_backbtn.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.re_backbtn.setStyleSheet("")
        self.re_backbtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Assets/Ui/Icons/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.re_backbtn.setIcon(icon2)
        self.re_backbtn.setIconSize(QtCore.QSize(40, 40))
        self.re_backbtn.setObjectName("re_backbtn")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(540, 20, 541, 551))
        self.frame_4.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label12 = QtWidgets.QLabel(self.frame_4)
        self.label12.setGeometry(QtCore.QRect(40, 140, 121, 31))
        self.label12.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label12.setObjectName("label12")
        self.re_idin = QtWidgets.QTextEdit(self.frame_4)
        self.re_idin.setGeometry(QtCore.QRect(40, 290, 201, 31))
        self.re_idin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_idin.setObjectName("re_idin")
        self.label15 = QtWidgets.QLabel(self.frame_4)
        self.label15.setGeometry(QtCore.QRect(40, 270, 111, 20))
        self.label15.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label15.setObjectName("label15")
        self.re_signupbtn = QtWidgets.QPushButton(self.frame_4)
        self.re_signupbtn.setGeometry(QtCore.QRect(140, 480, 261, 41))
        self.re_signupbtn.setStyleSheet("\n"
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
        self.re_signupbtn.setObjectName("re_signupbtn")
        self.label11 = QtWidgets.QLabel(self.frame_4)
        self.label11.setGeometry(QtCore.QRect(280, 0, 151, 41))
        self.label11.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label11.setObjectName("label11")
        self.label10 = QtWidgets.QLabel(self.frame_4)
        self.label10.setGeometry(QtCore.QRect(190, 0, 91, 41))
        self.label10.setStyleSheet("font: 75 20pt \"Ubuntu\";\n"
"color:rgb(28, 113, 216);")
        self.label10.setObjectName("label10")
        self.label9 = QtWidgets.QLabel(self.frame_4)
        self.label9.setGeometry(QtCore.QRect(80, 0, 101, 41))
        self.label9.setStyleSheet("font: 75 20pt \"Ubuntu\";")
        self.label9.setObjectName("label9")
        self.icon6 = QtWidgets.QPushButton(self.frame_4)
        self.icon6.setGeometry(QtCore.QRect(180, 40, 111, 101))
        self.icon6.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon6.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Assets/Ui/Icons/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon6.setIcon(icon3)
        self.icon6.setIconSize(QtCore.QSize(70, 70))
        self.icon6.setObjectName("icon6")
        self.re_namein = QtWidgets.QTextEdit(self.frame_4)
        self.re_namein.setGeometry(QtCore.QRect(250, 170, 231, 31))
        self.re_namein.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_namein.setObjectName("re_namein")
        self.label13 = QtWidgets.QLabel(self.frame_4)
        self.label13.setGeometry(QtCore.QRect(250, 150, 111, 17))
        self.label13.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label13.setObjectName("label13")
        self.re_fnamein = QtWidgets.QTextEdit(self.frame_4)
        self.re_fnamein.setGeometry(QtCore.QRect(40, 170, 201, 31))
        self.re_fnamein.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_fnamein.setPlaceholderText("")
        self.re_fnamein.setObjectName("re_fnamein")
        self.re_mailin = QtWidgets.QTextEdit(self.frame_4)
        self.re_mailin.setGeometry(QtCore.QRect(40, 230, 291, 31))
        self.re_mailin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_mailin.setObjectName("re_mailin")
        self.label14 = QtWidgets.QLabel(self.frame_4)
        self.label14.setGeometry(QtCore.QRect(40, 210, 131, 20))
        self.label14.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label14.setObjectName("label14")
        self.re_cpassin = QtWidgets.QTextEdit(self.frame_4)
        self.re_cpassin.setGeometry(QtCore.QRect(40, 410, 291, 31))
        self.re_cpassin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_cpassin.setPlaceholderText("")
        self.re_cpassin.setObjectName("re_cpassin")
        self.label17 = QtWidgets.QLabel(self.frame_4)
        self.label17.setGeometry(QtCore.QRect(40, 390, 181, 20))
        self.label17.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label17.setObjectName("label17")
        self.re_passin = QtWidgets.QTextEdit(self.frame_4)
        self.re_passin.setGeometry(QtCore.QRect(40, 350, 291, 31))
        self.re_passin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_passin.setPlaceholderText("")
        self.re_passin.setObjectName("re_passin")
        self.label16 = QtWidgets.QLabel(self.frame_4)
        self.label16.setGeometry(QtCore.QRect(40, 330, 101, 20))
        self.label16.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label16.setObjectName("label16")
        self.re_phonein = QtWidgets.QTextEdit(self.frame_4)
        self.re_phonein.setGeometry(QtCore.QRect(330, 290, 151, 31))
        self.re_phonein.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.re_phonein.setObjectName("re_phonein")
        self.icon7 = QtWidgets.QPushButton(self.frame_4)
        self.icon7.setGeometry(QtCore.QRect(250, 290, 81, 31))
        self.icon7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.icon7.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:rgb(0, 137, 236);\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Assets/Ui/Icons/algeria.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon7.setIcon(icon4)
        self.icon7.setObjectName("icon7")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setGeometry(QtCore.QRect(50, 450, 92, 23))
        self.checkBox.setObjectName("checkBox")
        # RegisterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 22))
        self.menubar.setObjectName("menubar")
        # RegisterWindow.setMenuBar(self.menubar)

        self.retranslateUi(RegisterWindow)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindow)

    def retranslateUi(self, RegisterWindow):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindow.setWindowTitle(_translate("RegisterWindow", "Register"))
        self.label8.setText(_translate("RegisterWindow", "Library"))
        self.re_helpbtn.setText(_translate("RegisterWindow", "Help"))
        self.label12.setText(_translate("RegisterWindow", "Family Name"))
        self.re_idin.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.re_idin.setPlaceholderText(_translate("RegisterWindow", "3800...."))
        self.label15.setText(_translate("RegisterWindow", "ID"))
        self.re_signupbtn.setText(_translate("RegisterWindow", "Sign Up"))
        self.label11.setText(_translate("RegisterWindow", "membership"))
        self.label10.setText(_translate("RegisterWindow", "Library"))
        self.label9.setText(_translate("RegisterWindow", "Create a"))
        self.re_namein.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label13.setText(_translate("RegisterWindow", "Name"))
        self.re_fnamein.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.re_mailin.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.re_mailin.setPlaceholderText(_translate("RegisterWindow", "Someone@mail.com"))
        self.label14.setText(_translate("RegisterWindow", "Email address"))
        self.re_cpassin.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label17.setText(_translate("RegisterWindow", "Confirme password"))
        self.re_passin.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label16.setText(_translate("RegisterWindow", "Password"))
        self.re_phonein.setHtml(_translate("RegisterWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.re_phonein.setPlaceholderText(_translate("RegisterWindow", "612345678"))
        self.icon7.setText(_translate("RegisterWindow", "+213"))
        self.checkBox.setText(_translate("RegisterWindow", "I am sure"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myacc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyaccWindow(object):
    def setupUi(self, MyaccWindow):
        MyaccWindow.setObjectName("MyaccWindow")
        MyaccWindow.resize(1128, 629)
        MyaccWindow.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.centralwidget = QtWidgets.QWidget(MyaccWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        self.frame_10.setGeometry(QtCore.QRect(180, 130, 401, 471))
        self.frame_10.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label29 = QtWidgets.QLabel(self.frame_10)
        self.label29.setGeometry(QtCore.QRect(40, 200, 181, 31))
        self.label29.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label29.setObjectName("label29")
        self.mm_conpassin = QtWidgets.QTextEdit(self.frame_10)
        self.mm_conpassin.setGeometry(QtCore.QRect(40, 230, 311, 31))
        self.mm_conpassin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_conpassin.setObjectName("mm_conpassin")
        self.label26 = QtWidgets.QLabel(self.frame_10)
        self.label26.setGeometry(QtCore.QRect(60, 10, 271, 71))
        self.label26.setStyleSheet("font: 25pt \"Ubuntu Mono\";\n"
"color:black;\n"
"background-color: rgba(28, 113, 216, 0)")
        self.label26.setObjectName("label26")
        self.mm_newpassin = QtWidgets.QTextEdit(self.frame_10)
        self.mm_newpassin.setGeometry(QtCore.QRect(40, 170, 311, 31))
        self.mm_newpassin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_newpassin.setObjectName("mm_newpassin")
        self.label28 = QtWidgets.QLabel(self.frame_10)
        self.label28.setGeometry(QtCore.QRect(40, 140, 151, 31))
        self.label28.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label28.setObjectName("label28")
        self.mm_submitbtn = QtWidgets.QPushButton(self.frame_10)
        self.mm_submitbtn.setGeometry(QtCore.QRect(80, 270, 191, 41))
        self.mm_submitbtn.setStyleSheet("\n"
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
        self.mm_submitbtn.setIconSize(QtCore.QSize(30, 30))
        self.mm_submitbtn.setObjectName("mm_submitbtn")
        self.mm_curpassin = QtWidgets.QTextEdit(self.frame_10)
        self.mm_curpassin.setGeometry(QtCore.QRect(40, 110, 311, 31))
        self.mm_curpassin.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_curpassin.setObjectName("mm_curpassin")
        self.label27 = QtWidgets.QLabel(self.frame_10)
        self.label27.setGeometry(QtCore.QRect(40, 80, 161, 31))
        self.label27.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label27.setObjectName("label27")
        self.frame_16 = QtWidgets.QFrame(self.centralwidget)
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
        icon.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/graduate-cap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/programmer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.log_credits_25.setIcon(icon2)
        self.log_credits_25.setIconSize(QtCore.QSize(25, 25))
        self.log_credits_25.setObjectName("log_credits_25")
        self.main_accbtn = QtWidgets.QPushButton(self.frame_16)
        self.main_accbtn.setGeometry(QtCore.QRect(10, 180, 151, 51))
        self.main_accbtn.setStyleSheet("\n"
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
        self.main_accbtn.setIcon(icon1)
        self.main_accbtn.setIconSize(QtCore.QSize(25, 25))
        self.main_accbtn.setObjectName("main_accbtn")
        self.main_booksbtn = QtWidgets.QPushButton(self.frame_16)
        self.main_booksbtn.setGeometry(QtCore.QRect(10, 240, 151, 51))
        self.main_booksbtn.setStyleSheet("\n"
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
        self.main_booksbtn.setIcon(icon2)
        self.main_booksbtn.setIconSize(QtCore.QSize(25, 25))
        self.main_booksbtn.setObjectName("main_booksbtn")
        self.main_reqbtn = QtWidgets.QPushButton(self.frame_16)
        self.main_reqbtn.setGeometry(QtCore.QRect(10, 300, 151, 51))
        self.main_reqbtn.setStyleSheet("\n"
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
        icon3.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/interview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_reqbtn.setIcon(icon3)
        self.main_reqbtn.setIconSize(QtCore.QSize(25, 25))
        self.main_reqbtn.setObjectName("main_reqbtn")
        self.icon11 = QtWidgets.QPushButton(self.frame_16)
        self.icon11.setGeometry(QtCore.QRect(-20, 50, 191, 111))
        self.icon11.setStyleSheet("background-color: rgba(28, 113, 216, 0);")
        self.icon11.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/digital-library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon11.setIcon(icon4)
        self.icon11.setIconSize(QtCore.QSize(100, 100))
        self.icon11.setObjectName("icon11")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(590, 130, 531, 471))
        self.frame_9.setStyleSheet("border: 1px;\n"
"border-radius: 20px;\n"
"background-color: white;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label32 = QtWidgets.QLabel(self.frame_9)
        self.label32.setGeometry(QtCore.QRect(240, 80, 91, 31))
        self.label32.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label32.setObjectName("label32")
        self.mm_nameout = QtWidgets.QTextEdit(self.frame_9)
        self.mm_nameout.setGeometry(QtCore.QRect(240, 110, 271, 31))
        self.mm_nameout.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_nameout.setReadOnly(True)
        self.mm_nameout.setObjectName("mm_nameout")
        self.label33 = QtWidgets.QLabel(self.frame_9)
        self.label33.setGeometry(QtCore.QRect(30, 150, 21, 31))
        self.label33.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label33.setObjectName("label33")
        self.label34 = QtWidgets.QLabel(self.frame_9)
        self.label34.setGeometry(QtCore.QRect(240, 150, 121, 31))
        self.label34.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label34.setObjectName("label34")
        self.label35 = QtWidgets.QLabel(self.frame_9)
        self.label35.setGeometry(QtCore.QRect(30, 220, 121, 31))
        self.label35.setStyleSheet("font: 75 16pt \"Ubuntu\";")
        self.label35.setObjectName("label35")
        self.label30 = QtWidgets.QLabel(self.frame_9)
        self.label30.setGeometry(QtCore.QRect(60, 10, 271, 71))
        self.label30.setStyleSheet("font: 25pt \"Ubuntu Mono\";\n"
"color:black;\n"
"background-color: rgba(28, 113, 216, 0)")
        self.label30.setObjectName("label30")
        self.mm_idout = QtWidgets.QTextEdit(self.frame_9)
        self.mm_idout.setGeometry(QtCore.QRect(30, 180, 181, 31))
        self.mm_idout.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_idout.setReadOnly(True)
        self.mm_idout.setObjectName("mm_idout")
        self.mm_phoneout = QtWidgets.QTextEdit(self.frame_9)
        self.mm_phoneout.setGeometry(QtCore.QRect(300, 180, 141, 31))
        self.mm_phoneout.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_phoneout.setReadOnly(True)
        self.mm_phoneout.setObjectName("mm_phoneout")
        self.mm_fnameout = QtWidgets.QTextEdit(self.frame_9)
        self.mm_fnameout.setGeometry(QtCore.QRect(30, 110, 181, 31))
        self.mm_fnameout.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_fnameout.setReadOnly(True)
        self.mm_fnameout.setObjectName("mm_fnameout")
        self.label31 = QtWidgets.QLabel(self.frame_9)
        self.label31.setGeometry(QtCore.QRect(30, 80, 151, 31))
        self.label31.setStyleSheet("font: 75 16pt \"Ubuntu\";\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label31.setObjectName("label31")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_11.setGeometry(QtCore.QRect(240, 180, 61, 31))
        self.pushButton_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_11.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/algeria.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setObjectName("pushButton_11")
        self.mm_mailout = QtWidgets.QTextEdit(self.frame_9)
        self.mm_mailout.setGeometry(QtCore.QRect(30, 250, 261, 31))
        self.mm_mailout.setStyleSheet("background-color: white;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"border-radius: 10px;\n"
"font: 75 14pt \"Ubuntu Mono\";\n"
"\n"
"")
        self.mm_mailout.setReadOnly(True)
        self.mm_mailout.setObjectName("mm_mailout")
        self.icon13 = QtWidgets.QPushButton(self.frame_9)
        self.icon13.setGeometry(QtCore.QRect(310, 10, 111, 51))
        self.icon13.setStyleSheet("")
        self.icon13.setText("")
        self.icon13.setIcon(icon1)
        self.icon13.setIconSize(QtCore.QSize(50, 50))
        self.icon13.setObjectName("icon13")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(180, 0, 941, 121))
        self.frame_8.setStyleSheet("border: 1px ;\n"
"border-radius: 20px;\n"
"background-color:rgb(28, 113, 216)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label25 = QtWidgets.QLabel(self.frame_8)
        self.label25.setGeometry(QtCore.QRect(310, 20, 231, 71))
        self.label25.setStyleSheet("font: 63 italic 30pt \"URW Bookman\";\n"
"color:white;\n"
"background-color: rgba(28, 113, 216, 0);")
        self.label25.setObjectName("label25")
        self.mm_logoutbtn = QtWidgets.QPushButton(self.frame_8)
        self.mm_logoutbtn.setGeometry(QtCore.QRect(810, 10, 121, 41))
        self.mm_logoutbtn.setStyleSheet("\n"
"QPushButton {\n"
"background-color:rgb(224, 27, 36);\n"
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
"    font-size: 17px;\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Windows_Ui/Assets/Ui/Icons/logout (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mm_logoutbtn.setIcon(icon6)
        self.mm_logoutbtn.setIconSize(QtCore.QSize(20, 20))
        self.mm_logoutbtn.setObjectName("mm_logoutbtn")
        #MyaccWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyaccWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 22))
        self.menubar.setObjectName("menubar")
        #MyaccWindow.setMenuBar(self.menubar)

        self.retranslateUi(MyaccWindow)
        QtCore.QMetaObject.connectSlotsByName(MyaccWindow)

    def retranslateUi(self, MyaccWindow):
        _translate = QtCore.QCoreApplication.translate
        MyaccWindow.setWindowTitle(_translate("MyaccWindow", "My Account"))
        self.label29.setText(_translate("MyaccWindow", "Confirme password"))
        self.mm_conpassin.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label26.setText(_translate("MyaccWindow", "Change password"))
        self.mm_newpassin.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label28.setText(_translate("MyaccWindow", "New password"))
        self.mm_submitbtn.setText(_translate("MyaccWindow", "Submit"))
        self.mm_curpassin.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label27.setText(_translate("MyaccWindow", "Current password"))
        self.label19.setText(_translate("MyaccWindow", "Library"))
        self.log_credits_24.setText(_translate("MyaccWindow", "My account"))
        self.log_credits_25.setText(_translate("MyaccWindow", "Books"))
        self.main_accbtn.setText(_translate("MyaccWindow", "My account"))
        self.main_booksbtn.setText(_translate("MyaccWindow", "Books"))
        self.main_reqbtn.setText(_translate("MyaccWindow", "Request"))
        self.label32.setText(_translate("MyaccWindow", "Name"))
        self.mm_nameout.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label33.setText(_translate("MyaccWindow", "ID"))
        self.label34.setText(_translate("MyaccWindow", "Phone"))
        self.label35.setText(_translate("MyaccWindow", "Mail address"))
        self.label30.setText(_translate("MyaccWindow", "My Informations"))
        self.mm_idout.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.mm_phoneout.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.mm_fnameout.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label31.setText(_translate("MyaccWindow", "Family name"))
        self.pushButton_11.setText(_translate("MyaccWindow", "+213"))
        self.mm_mailout.setHtml(_translate("MyaccWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Mono\'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>"))
        self.label25.setText(_translate("MyaccWindow", "My Account"))
        self.mm_logoutbtn.setText(_translate("MyaccWindow", "Logout"))
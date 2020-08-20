# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pics
import os
from PyQt5.QtWidgets import QMessageBox
import smtplib
import pandas as pd
import numpy as np
from email.message import EmailMessage
import imghdr
import emoji
import pandas as pd
import numpy as np
import pics

import time
import threading
class Ui_MainWindow(object):
    def __init__(self):

        self.email = os.environ.get('EM_NAME')
        self.passw  = os.environ.get('EM_PASS')
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(850, 550))
        MainWindow.setMaximumSize(QtCore.QSize(850, 550))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 20, 431, 71))
        self.label.setStyleSheet("font: 36pt \"Arial Rounded MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(310, 443, 211, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(134, 0, 179);\n"
"\n"
"\n"
"color: rgb(0, 0, 0);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 140, 761, 291))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 111, 71))
        self.label_2.setStyleSheet("background-image: url(:/pics/bg/img_4839 (2).png);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 110, 561, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        from script import Ui_MainWindow as script_window
        ui = script_window()
        a1 = ui.return_value()
        self.flag = a1["flag"]
        self.temp_lineEdit = a1["temp_lineEdit"]
        
        self.pushButton.clicked.connect(self.extracting)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Emaite By Raheel Siddiqui"))
        self.label.setText(_translate("MainWindow", "Sending Email"))
        self.pushButton.setText(_translate("MainWindow", "Send Emails"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Type <name> and <email> if you want to use particular name from excel file"))

    def email_sender(self,reciever_email,name):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                    smtp.login(self.email,self.passw)
                    
                    email_text = self.plainTextEdit.toPlainText()
                    email_text = email_text.replace("<name>",name)
                    email_text = email_text.replace("<email>",reciever_email)
                    print(email_text)


                    
                    msg =EmailMessage()
                    msg['Subject']=f'Thanks {name}'+emoji.emojize(":grinning_face_with_big_eyes:")
                    msg['From'] =self.email
                    msg['To'] = reciever_email
                    content = email_text
                    msg.set_content (content)
                    smtp.send_message(msg)
        except:
            self.message("Internet Problem!")
    '''def create_progress(self,total):
        lst_t=[]
        a1 = int(round(100/total,2))
        for i in range(1,total+1):
            a2=a1*i
            lst_t.append(a2)
        return lst_t'''

    '''def progress_window(self,value):
        
        from progress import  Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        c = self.ui.setupUi(self.window)
        
        c.progressbar.setValue(value)
        self.window.show()'''
                
                
                
                
                
    def extracting(self):
        
        data=pd.read_csv(self.temp_lineEdit)
        
        arr =np.array(data.columns)
        column = [i.lower() for i in arr]
        print(column)
        data.columns = column
        #progress_values = self.create_progress(len(data))
        try:
            threads=[]
            for name,Email in zip(data.loc[:,"names"],data.loc[:,"emails"]):
                print(name,Email)
                #self.progress_window(value)
                t = threading.Thread(target=self.email_sender,args=[Email,name])
                t.start()
                threads.append(t)
            for thread in threads:
                thread.join()
                #self.email_sender(Email,name)
                
        except Exception as e:
            print(e)

            self.message("Internet Problem!")
    def message(self, message):
        a1= QMessageBox()
        a1.setWindowTitle("warning!")
        a1.setText(message)
        a1.setIcon(QMessageBox.Information)
        a1.setStandardButtons(QMessageBox.Ok)
        a1.exec_()

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

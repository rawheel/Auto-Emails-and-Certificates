# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'script.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 624)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bg/IMG_4844.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_6 = QtWidgets.QFrame(self.splitter_2)
        self.frame_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 64pt \"Times New Roman\";\n"
"image: url(:/pics/bg/TITLE.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"color: rgb(0, 0, 0);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 11pt \"Times New Roman\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setStyleSheet("font: 14pt \"Times New Roman\";\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setStyleSheet("font: 14pt \"Times New Roman\";\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame_5 = QtWidgets.QFrame(self.splitter)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet("image: url(:/pics/certificate.jpg);\n"
"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4.addWidget(self.frame_7)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("font: 14pt \"Times New Roman\";\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_7.setAutoFillBackground(False)
        self.pushButton_7.setStyleSheet("font: 14pt \"Times New Roman\";\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuDeveloped_By = QtWidgets.QMenu(self.menuAbout)
        self.menuDeveloped_By.setObjectName("menuDeveloped_By")
        self.menuRaheel_Siddiqui = QtWidgets.QMenu(self.menuDeveloped_By)
        self.menuRaheel_Siddiqui.setObjectName("menuRaheel_Siddiqui")
        MainWindow.setMenuBar(self.menubar)
        self.actionVersion_1_0 = QtWidgets.QAction(MainWindow)
        self.actionVersion_1_0.setObjectName("actionVersion_1_0")
        self.actionFacebook = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pics/fb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFacebook.setIcon(icon1)
        self.actionFacebook.setObjectName("actionFacebook")
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pics/GitHub.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGitHub.setIcon(icon2)
        self.actionGitHub.setObjectName("actionGitHub")
        self.actionLinkedin = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pics/LinkedIn-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLinkedin.setIcon(icon3)
        self.actionLinkedin.setObjectName("actionLinkedin")
        self.menuRaheel_Siddiqui.addSeparator()
        self.menuRaheel_Siddiqui.addAction(self.actionFacebook)
        self.menuRaheel_Siddiqui.addAction(self.actionGitHub)
        self.menuRaheel_Siddiqui.addAction(self.actionLinkedin)
        self.menuDeveloped_By.addAction(self.menuRaheel_Siddiqui.menuAction())
        self.menuAbout.addAction(self.actionVersion_1_0)
        self.menuAbout.addAction(self.menuDeveloped_By.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Emaite By Raheel Siddiqui"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Names"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Emails"))
        self.label.setText(_translate("MainWindow", "File Path:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Excel File Path"))
        self.pushButton_5.setText(_translate("MainWindow", "Load Emails"))
        self.pushButton_4.setText(_translate("MainWindow", "Write Email"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Certificates"))
        self.pushButton_7.setText(_translate("MainWindow", "Send Certificates"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuDeveloped_By.setTitle(_translate("MainWindow", "Developed By"))
        self.menuRaheel_Siddiqui.setTitle(_translate("MainWindow", "Raheel Siddiqui"))
        self.actionVersion_1_0.setText(_translate("MainWindow", "Version 1.0"))
        self.actionFacebook.setText(_translate("MainWindow", "Facebook"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        self.actionLinkedin.setText(_translate("MainWindow", "Linkedin"))
import pics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

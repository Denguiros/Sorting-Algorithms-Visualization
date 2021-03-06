# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sorting.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1454, 872)
        MainWindow.setMinimumSize(QtCore.QSize(1454, 872))
        MainWindow.setMaximumSize(QtCore.QSize(1454, 872))
        MainWindow.setWindowIcon(QIcon("Sort_icon.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(10, 10, 1451, 861))
        self.tabs.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";\n"
"")
        self.tabs.setObjectName("tabs")
        self.sortTab = QtWidgets.QWidget()
        self.sortTab.setEnabled(True)
        self.sortTab.setObjectName("sortTab")
        self.inputField = QtWidgets.QLineEdit(self.sortTab)
        self.inputField.setGeometry(QtCore.QRect(370, 10, 1011, 61))
        self.inputField.setText("")
        self.inputField.setPlaceholderText("Please type in your unsorted list of integers seperated with spaces ...")
        self.sortMethod = QtWidgets.QComboBox(self.sortTab)
        self.sortMethod.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.sortMethod.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.sortMethod.setObjectName("sortMethod")
        self.sortMethod.addItem("")
        self.sortMethod.addItem("")
        self.sortMethod.addItem("")
        self.sortMethod.addItem("")
        self.sortMethod.addItem("")
        self.sortMethod.addItem("")
        self.stateField = QtWidgets.QTextBrowser(self.sortTab)
        self.stateField.setGeometry(QtCore.QRect(370, 90, 1011, 71))
        self.stateField.setObjectName("stateField")
        self.stateField.setStyleSheet("font: 10pt \"MS Reference Sans Serif\";")
        self.stateField.setPlaceholderText("Please type in your unsorted list of integers seperated with spaces ...")
        self.label = QtWidgets.QLabel(self.sortTab)
        self.label.setGeometry(QtCore.QRect(260, 110, 91, 31))
        self.label.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label.setObjectName("label")
        self.mediumSpeedButton = QtWidgets.QRadioButton(self.sortTab)
        self.mediumSpeedButton.setGeometry(QtCore.QRect(300, 690, 111, 20))
        self.mediumSpeedButton.setObjectName("mediumSpeedButton")
        self.slowSpeedButton = QtWidgets.QRadioButton(self.sortTab)
        self.slowSpeedButton.setGeometry(QtCore.QRect(180, 690, 95, 20))
        self.slowSpeedButton.setObjectName("slowSpeedButton")
        self.fastSpeedButton = QtWidgets.QRadioButton(self.sortTab)
        self.fastSpeedButton.setGeometry(QtCore.QRect(430, 690, 95, 20))
        self.fastSpeedButton.setChecked(True)
        self.fastSpeedButton.setObjectName("fastSpeedButton")
        self.animateButton = QtWidgets.QPushButton(self.sortTab)
        self.animateButton.setGeometry(QtCore.QRect(10, 677, 111, 41))
        self.animateButton.setObjectName("animateButton")
        self.line = QtWidgets.QFrame(self.sortTab)
        self.line.setGeometry(QtCore.QRect(-280, 170, 1911, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.resultField = QtWidgets.QTextBrowser(self.sortTab)
        self.resultField.setGeometry(QtCore.QRect(10, 260, 491, 391))
        self.resultField.setObjectName("resultField")
        self.resultField.setPlaceholderText("Please type in your unsorted list of integers seperated with spaces ...")
        self.randomizeButton = QtWidgets.QPushButton(self.sortTab)
        self.randomizeButton.setGeometry(QtCore.QRect(10, 90, 171, 51))
        self.randomizeButton.setObjectName("randomizeButton")
        self.label_3 = QtWidgets.QLabel(self.sortTab)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 271, 31))
        self.label_3.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label_3.setObjectName("label_3")
        self.linkButton = QtWidgets.QPushButton(self.sortTab)
        self.linkButton.setGeometry(QtCore.QRect(310, 760, 111, 41))
        self.linkButton.setObjectName("linkButton")
        self.label_4 = QtWidgets.QLabel(self.sortTab)
        self.label_4.setGeometry(QtCore.QRect(10, 760, 271, 31))
        self.label_4.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.sortTab)
        self.label_5.setGeometry(QtCore.QRect(810, 760, 271, 31))
        self.label_5.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.videoButton = QtWidgets.QPushButton(self.sortTab)
        self.videoButton.setGeometry(QtCore.QRect(1120, 760, 111, 41))
        self.videoButton.setObjectName("videoButton")
        self.exampleImage = QtWidgets.QLabel(self.sortTab)
        self.exampleImage.setGeometry(QtCore.QRect(570, 260, 841, 451))
        self.exampleImage.setText("")
        self.exampleImage.setPixmap(QtGui.QPixmap("bubblesort.png"))
        self.exampleImage.setScaledContents(True)
        self.exampleImage.setWordWrap(False)
        self.exampleImage.setObjectName("exampleImage")
        self.label_6 = QtWidgets.QLabel(self.sortTab)
        self.label_6.setGeometry(QtCore.QRect(570, 200, 111, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.sortTab)
        self.label_7.setGeometry(QtCore.QRect(260, 20, 91, 31))
        self.label_7.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label_7.setObjectName("label_7")
        self.tabs.addTab(self.sortTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.label_8 = QtWidgets.QLabel(self.aboutTab)
        self.label_8.setGeometry(QtCore.QRect(260, 130, 211, 351))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("E:/Profile Picture.jpg"))
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.aboutTab)
        self.label_9.setGeometry(QtCore.QRect(360, 730, 621, 51))
        self.label_9.setStyleSheet("font: 15pt \"MS Reference Sans Serif\";")
        self.label_9.setObjectName("label_9")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.aboutTab)
        self.textBrowser_3.setGeometry(QtCore.QRect(720, 130, 361, 351))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_11 = QtWidgets.QLabel(self.aboutTab)
        self.label_11.setGeometry(QtCore.QRect(720, 570, 91, 41))
        self.label_11.setObjectName("label_11")
        self.facebookButton = QtWidgets.QPushButton(self.aboutTab)
        self.facebookButton.setGeometry(QtCore.QRect(840, 570, 51, 51))
        self.facebookButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("t??l??chargement.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.facebookButton.setIcon(icon)
        self.facebookButton.setIconSize(QtCore.QSize(50, 50))
        self.facebookButton.setObjectName("facebookButton")
        self.instagramButton = QtWidgets.QPushButton(self.aboutTab)
        self.instagramButton.setGeometry(QtCore.QRect(940, 570, 51, 51))
        self.instagramButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ca5b4df7080ab2cb871cae11baa791b1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instagramButton.setIcon(icon1)
        self.instagramButton.setIconSize(QtCore.QSize(50, 50))
        self.instagramButton.setObjectName("instagramButton")
        self.linkedinButton = QtWidgets.QPushButton(self.aboutTab)
        self.linkedinButton.setGeometry(QtCore.QRect(1030, 570, 51, 51))
        self.linkedinButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("t??l??chargement (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.linkedinButton.setIcon(icon2)
        self.linkedinButton.setIconSize(QtCore.QSize(50, 50))
        self.linkedinButton.setObjectName("linkedinButton")
        self.tabs.addTab(self.aboutTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Denguiros Sorting Algorithm"))
        self.sortMethod.setItemText(0, _translate("MainWindow", "Bubble sort"))
        self.sortMethod.setItemText(1, _translate("MainWindow", "Quick sort"))
        self.sortMethod.setItemText(2, _translate("MainWindow", "Selection sort"))
        self.sortMethod.setItemText(3, _translate("MainWindow", "Insertion sort"))
        self.sortMethod.setItemText(4, _translate("MainWindow", "Merge sort"))
        self.sortMethod.setItemText(5, _translate("MainWindow", "Binary search"))
        self.label.setText(_translate("MainWindow", "State :"))
        self.mediumSpeedButton.setText(_translate("MainWindow", "Medium "))
        self.slowSpeedButton.setText(_translate("MainWindow", "Slow"))
        self.fastSpeedButton.setText(_translate("MainWindow", "Fast"))
        self.animateButton.setText(_translate("MainWindow", "Animate"))
        self.randomizeButton.setText(_translate("MainWindow", "Randomize"))
        self.label_3.setText(_translate("MainWindow", "Result :"))
        self.linkButton.setText(_translate("MainWindow", "Link"))
        self.label_4.setText(_translate("MainWindow", "More informations :"))
        self.label_5.setText(_translate("MainWindow", "Explanatory video :"))
        self.videoButton.setText(_translate("MainWindow", "Video"))
        self.label_6.setText(_translate("MainWindow", "Example :"))
        self.label_7.setText(_translate("MainWindow", "Input :"))
        self.tabs.setTabText(self.tabs.indexOf(self.sortTab), _translate("MainWindow", "Sort"))
        self.label_9.setText(_translate("MainWindow", "?? 2020-2022 Fehmi Denguir All Rights Reserved"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Reference Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">This project is made by Fehmi Denguir , an engineering student at National Engineering School of Sfax </span><span style=\" font-size:20pt; font-weight:600; color:#ff0004;\">(ENIS)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600; color:#ff0004;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Contacts :"))
        self.tabs.setTabText(self.tabs.indexOf(self.aboutTab), _translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

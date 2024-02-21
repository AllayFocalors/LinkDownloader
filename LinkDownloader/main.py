# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\LinkDownloader\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import tkinter.filedialog
import tkinter as tk
import pyautogui
import requests
import os

AppName = 'LinkDownloader'

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(AppName)
        Form.resize(700, 400)
        self.Ledt_FileLink = QtWidgets.QLineEdit(Form)
        self.Ledt_FileLink.setGeometry(QtCore.QRect(130, 20, 491, 41))
        self.Ledt_FileLink.setObjectName("Ledt_FileLink")
        self. Butn_StartDownload = QtWidgets.QPushButton(Form)
        self. Butn_StartDownload.setGeometry(QtCore.QRect(130, 140, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self. Butn_StartDownload.setFont(font)
        self. Butn_StartDownload.setObjectName(" Butn_StartDownload")
        self. Butn_StartDownload.clicked.connect(self.StartDownload)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MiSans VF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(130, 200, 491, 31))
        self.progressBar.setProperty("value", 5)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MiSans VF")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Ledt_DnldPath = QtWidgets.QLineEdit(Form)
        self.Ledt_DnldPath.setGeometry(QtCore.QRect(130, 80, 361, 41))
        self.Ledt_DnldPath.setObjectName("Ledt_DnldPath")
        self.Butn_ChooseDirectory = QtWidgets.QPushButton(Form)
        self.Butn_ChooseDirectory.setGeometry(QtCore.QRect(510, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setBold(True)
        font.setWeight(75)
        self.Butn_ChooseDirectory.setFont(font)
        self.Butn_ChooseDirectory.setObjectName("Butn_ChooseDirectory")
        self.Butn_ChooseDirectory.clicked.connect(self.ChooseDirectory)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Butn_StartDownload.setText(_translate("Form", "开始下载"))
        self.label.setText(_translate("Form", "文件地址"))
        self.label_2.setText(_translate("Form", "下载位置"))
        self.Butn_ChooseDirectory.setText(_translate("Form", "浏览路径"))

    def ChooseDirectory(self):
        root = tk.Tk()
        root.withdraw()
        get_save_path = tkinter.filedialog.askdirectory()
        print(get_save_path)
        self.Ledt_DnldPath.setText(get_save_path)	

    def DownloadFile(self):
        buffer_size = 11451
        size_downloaded = 0
        print(f'目标文件: {self.Ledt_DnldPath.text()+self.Ledt_FileLink.text()[-16:]}')
        with open(self.Ledt_DnldPath.text()+'/'+self.Ledt_FileLink.text()[-16:],'wb') as file:
            for data in response.iter_content(buffer_size):
                file.write(data)
                size_downloaded += len(data)
                print('\r已下载{:.1f}MB {:.4f}%'.format(size_downloaded/1024/1024,size_downloaded/content_length*100),end='')
                self.progressBar.setValue(size_downloaded/content_length*100)

    def StartDownload(self, ):
        global response,content_length
        response = requests.get(self.Ledt_FileLink.text(),headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
            },stream=True)
        content_length = int(response.headers["content-length"])
        print(response)
       
        app = QApplication(sys.argv)
        w = QWidget()
        messageBody = f'''资源链接：{self.Ledt_FileLink.text()[:32]} ... {self.Ledt_FileLink.text()[-16:]}
下载地址：{self.Ledt_DnldPath.text()},
文件大小:{content_length/1024:.2f}KB,
即{content_length/1024/1024:.2f}MB
选择Yes开始极速下载'''
        reply = QMessageBox.question(w, 'title', messageBody, QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            print('部署下载...')
            self.DownloadFile()
            sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())

    
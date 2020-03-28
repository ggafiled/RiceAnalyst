# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomeActivity.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json
import apiai

class Ui_HomeActivity(QtWidgets.QFrame):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.root = os.path.dirname(os.path.realpath(__file__))

    def initUI(self):
        self.setObjectName("HomeActivity")
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.resize(900, 500)
        self.setMinimumSize(QtCore.QSize(480, 280))
        self.setMaximumSize(QtCore.QSize(900, 500))
        self.setWindowTitle("")
        self.setAutoFillBackground(False)
        self.setStyleSheet("QWidget{\n"
"    background-color:rgb(241,241,241);\n"
"}")
        self.CLIENT_ACCESS_TOKEN = "85b37081bb9342259ab2e6c2a65f1f0f"
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
        self.btnSelect = QtWidgets.QPushButton(self)
        self.btnSelect.setGeometry(QtCore.QRect(670, 20, 211, 51))
        self.btnSelect.setStyleSheet("QPushButton {\n"
"border-radius:20px;\n"
"background: rgb(254, 255, 255);\n"
"color: rgb(29, 58, 143);\n"
"width: 100%;\n"
"border: 1px solid  rgba(0, 0, 0, 0.1);\n"
"outline: none;\n"
"font-size:16px;\n"
"box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);\n"
"}\n"
"QPushButton:hover{\n"
"background: rgb(29, 58, 143);\n"
"color:#ffffff;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/ggafiled/Downloads/directory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelect.setIcon(icon)
        self.btnSelect.setIconSize(QtCore.QSize(32, 32))
        self.btnSelect.setObjectName("btnSelect")
        self.btnSelect.clicked.connect(self.riceIssueSearch)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 641, 81))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFocus()
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(16)
        font.setBold(False)
        self.plainTextEdit.setFont(font)
        self.labelResult = QtWidgets.QLabel(self)
        self.labelResult.setGeometry(QtCore.QRect(30, 140, 631, 201))
        self.labelResult.setWordWrap(True)
        font = QtGui.QFont()
        font.setFamily("TH Sarabun New")
        font.setPointSize(16)
        self.labelResult.setFont(font)
        self.labelResult.setAutoFillBackground(True)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("TH SarabunPSK")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        QtCore.QMetaObject.connectSlotsByName(self)
        self.btnSelect.setText("ค้นหาอาการ")
        self.label.setText("คำตอบ")

    def riceIssueSearch(self):
        try:
            self.labelResult.setText("")
            request = self.ai.text_request()
            request.lang = "th-TH"
            request.query = self.plainTextEdit.toPlainText()
            response = json.loads(request.getresponse().read().decode('utf-8'))
            message = response['result']['fulfillment']['speech']
            if len(message) <= 0:
                self.labelResult.setText("ไม่สามารถค้นหาวิธีแก้ไข ของอาการดังกล่าวได้ค่ะ")
            self.labelResult.setText(message.strip())
        except:
            self.labelResult.setText("ไม่สามารถค้นหาวิธีแก้ไข เนื่องจากระบบขัดข้องค่ะ กรุณาลองใหม่อีกครั้ง")

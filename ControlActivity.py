# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlActivity.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from HomeActivity import Ui_HomeActivity
from WelcomeActivity import Ui_WelcomeActivity
import os

class Ui_RiceAnalyst(object):
    def setupUi(self, RiceAnalyst):
        RiceAnalyst.setObjectName("RiceAnalyst")
        RiceAnalyst.setWindowModality(QtCore.Qt.ApplicationModal)
        RiceAnalyst.resize(960, 540)
        RiceAnalyst.setMinimumSize(QtCore.QSize(960, 540))
        RiceAnalyst.setMaximumSize(QtCore.QSize(960, 540))
        self.root = os.path.dirname(os.path.realpath(__file__))
        RiceAnalyst.setWindowIcon(QtGui.QIcon(self.root + os.path.sep + "img/icons/32x32.ico"))
        RiceAnalyst.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(RiceAnalyst)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -10, 61, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:rgb(49, 49, 49);\n"
"display:flex;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btnBar = QtWidgets.QPushButton(self.frame)
        self.btnBar.setGeometry(QtCore.QRect(0, 10, 61, 51))
        self.btnBar.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"border:none;\n"
"background-color:rgb(209, 52, 56);")
        self.btnBar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/ggafiled/Downloads/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBar.setIcon(icon1)
        self.btnBar.setIconSize(QtCore.QSize(28, 28))
        self.btnBar.setAutoDefault(False)
        self.btnBar.setDefault(True)
        self.btnBar.setObjectName("btnBar")
        self.btnBar.clicked.connect(self.welcome)
        self.btnHome = QtWidgets.QPushButton(self.frame)
        self.btnHome.setGeometry(QtCore.QRect(0, 60, 61, 51))
        self.btnHome.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnHome.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/ggafiled/Downloads/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon2)
        self.btnHome.setIconSize(QtCore.QSize(28, 28))
        self.btnHome.setAutoDefault(False)
        self.btnHome.setDefault(True)
        self.btnHome.setObjectName("btnHome")
        self.btnHome.clicked.connect(self.home)
        self.btnExit = QtWidgets.QPushButton(self.frame)
        self.btnExit.setGeometry(QtCore.QRect(0, 500, 61, 51))
        self.btnExit.setStyleSheet("/*border:1px solid #ffffff;*/\n"
"QPushButton:hover\n"
"{\n"
"   border:none;\n"
"   background-color:rgb(209, 52, 56);\n"
"}\n"
"QPushButton\n"
"{\n"
"   border:none;\n"
"}")
        self.btnExit.setText("")
        self.btnExit.clicked.connect(self.exit)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/ggafiled/Downloads/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExit.setIcon(icon3)
        self.btnExit.setIconSize(QtCore.QSize(28, 28))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setDefault(True)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.frame)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(60, 0, 901, 541))
        self.mdiArea.setStyleSheet("background-color:#ffffff;")
        brush = QtGui.QBrush(QtGui.QColor(241, 241, 241))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setObjectName("mdiArea")
        RiceAnalyst.setCentralWidget(self.centralwidget)

        self.retranslateUi(RiceAnalyst)
        QtCore.QMetaObject.connectSlotsByName(RiceAnalyst)

        self.welcome()

    def retranslateUi(self, RiceAnalyst):
        _translate = QtCore.QCoreApplication.translate
        RiceAnalyst.setWindowTitle(_translate("RiceAnalyst", "RiceAnalyst-GUI"))
        self.btnHome.setToolTip(_translate("RiceAnalyst", "Home"))
        self.btnExit.setToolTip(_translate("RiceAnalyst", "Exit"))

    def exit(self):
        QtCore.QCoreApplication.exit(0)

    def home(self):
        self.clearbackgroundcolor()
        self.setbackgroundcolor(self.btnHome)
        home_ui = Ui_HomeActivity()
        self.mdiArea.addSubWindow(home_ui)
        home_ui.show()
        home_ui.setWindowState(QtCore.Qt.WindowMaximized)

    def welcome(self):
        self.clearbackgroundcolor()
        self.setbackgroundcolor(self.btnBar)
        welcome_ui = Ui_WelcomeActivity()
        self.mdiArea.addSubWindow(welcome_ui)
        welcome_ui.show()
        welcome_ui.setWindowState(QtCore.Qt.WindowMaximized)

    def clearbackgroundcolor(self):
        self.btnBar.setStyleSheet("QPushButton:hover {"
                "   border:none;\n"
                "   background-color:rgb(209, 52, 56);\n"
                "}\n"
                "QPushButton\n"
                "{\n"
                "   border:none;\n"
                "   background-color: rgb(49, 49, 49);\n"
                "}")
        self.btnHome.setStyleSheet("QPushButton:hover {"
                "   border:none;\n"
                "   background-color:rgb(209, 52, 56);\n"
                "}\n"
                "QPushButton\n"
                "{\n"
                "   border:none;\n"
                "   background-color: rgb(49, 49, 49);\n"
                "}")

    def setbackgroundcolor(self,object):
        object.setStyleSheet("QPushButton:hover {"
                "   border:none;\n"
                "   background-color:rgb(209, 52, 56);\n"
                "}\n"
                "QPushButton\n"
                "{\n"
                "   border:none;\n"
                "   background-color: rgb(209, 52, 56);\n"
                "}")


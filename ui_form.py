# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 370)
        MainWindow.setMinimumSize(QSize(320, 370))
        MainWindow.setMaximumSize(QSize(320, 370))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 281, 357))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Corbel Light"])
        font.setPointSize(25)
        font.setWeight(QFont.Light)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.email = QTextEdit(self.verticalLayoutWidget)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(20, 30))
        self.email.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.email)

        self.password = QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(u"password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setMaxLength(30)

        self.verticalLayout.addWidget(self.password)

        self.show_password = QRadioButton(self.verticalLayoutWidget)
        self.show_password.setObjectName(u"show_password")
        self.show_password.toggled.connect(self.toggle_password_visibility)
        self.verticalLayout.addWidget(self.show_password)

        self.loginButton = QPushButton(self.verticalLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setCheckable(False)

        self.verticalLayout.addWidget(self.loginButton)

        self.verticalSpacer_3 = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.signup = QPushButton(self.verticalLayoutWidget)
        self.signup.setObjectName(u"signup")
        self.signup.setMaximumSize(QSize(70, 150))

        self.verticalLayout.addWidget(self.signup)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def toggle_password_visibility(self, checked):
        if checked:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login into Popcorn hour!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.email.setMarkdown("")
        self.email.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"youremail@email.com", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.show_password.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.signup.setText(QCoreApplication.translate("MainWindow", u"Sign up!", None))
    # retranslateUi


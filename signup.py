# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SignupWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 450)
        MainWindow.setMinimumSize(QSize(320, 450))
        MainWindow.setMaximumSize(QSize(320, 450))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 281, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.email = QTextEdit(self.verticalLayoutWidget)
        self.email.setObjectName(u"email")
        self.email.setMinimumSize(QSize(20, 30))
        self.email.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.email)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.password = QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 30))
        self.password.setMaxLength(30)
        self.password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password)

        self.password_2 = QLineEdit(self.verticalLayoutWidget)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setMinimumSize(QSize(0, 30))
        self.password_2.setMaxLength(30)
        self.password_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_2)

        self.show_password = QRadioButton(self.verticalLayoutWidget)
        self.show_password.setObjectName(u"show_password")
        self.show_password.toggled.connect(self.toggle_password_visibility)

        self.verticalLayout.addWidget(self.show_password)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.first_name = QTextEdit(self.verticalLayoutWidget)
        self.first_name.setObjectName(u"first_name")
        self.first_name.setMinimumSize(QSize(20, 30))
        self.first_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.first_name)

        self.last_name = QTextEdit(self.verticalLayoutWidget)
        self.last_name.setObjectName(u"last_name")
        self.last_name.setMinimumSize(QSize(20, 30))
        self.last_name.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.last_name)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 50))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 20, 190, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.moderator_type = QRadioButton(self.widget)
        self.moderator_type.setObjectName(u"moderator_type")

        self.horizontalLayout.addWidget(self.moderator_type)

        self.user_type = QRadioButton(self.widget)
        self.user_type.setObjectName(u"user_type")

        self.horizontalLayout.addWidget(self.user_type)


        self.verticalLayout.addWidget(self.groupBox)

        self.signup = QPushButton(self.verticalLayoutWidget)
        self.signup.setObjectName(u"signup")
        self.signup.setCheckable(False)

        self.verticalLayout.addWidget(self.signup)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def toggle_password_visibility(self, checked):
        if checked:
            self.password.setEchoMode(QLineEdit.Normal)
            self.password_2.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
            self.password_2.setEchoMode(QLineEdit.Password)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Signup into Popcorn hour!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sign up!", None))
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
        self.password_2.setText("")
        self.password_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repeat password", None))
        self.show_password.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.first_name.setMarkdown("")
        self.first_name.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.first_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your first name", None))
        self.last_name.setMarkdown("")
        self.last_name.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.last_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"User Type", None))
        self.moderator_type.setText(QCoreApplication.translate("MainWindow", u"Moderator", None))
        self.user_type.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.signup.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
    # retranslateUi


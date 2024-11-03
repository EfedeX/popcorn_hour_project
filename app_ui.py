# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        # self.conversation_list = QListWidget(self.centralwidget)
        # self.conversation_list.setObjectName(u"conversation_list")
        # self.conversation_list.setGeometry(QRect(530, 10, 256, 421))
        # self.comment_button = QPushButton(self.centralwidget)
        # self.comment_button.setObjectName(u"comment_button")
        # self.comment_button.setGeometry(QRect(620, 440, 80, 24))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 503, 531))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.image = QLabel(self.layoutWidget)
        self.image.setObjectName(u"image")
        self.image.setMinimumSize(QSize(530, 380))
        self.image.setMaximumSize(QSize(530, 380))
        self.image.setPixmap(QPixmap(""))
        self.image.setScaledContents(True)
        self.movie_info_layout = QVBoxLayout()
        self.movie_title = QLabel(self.layoutWidget)
        self.movie_title.setObjectName(u"movie_title")
        self.movie_title.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.movie_title.setFont(font)
        self.movie_info_layout.addWidget(self.movie_title)

        # Director
        self.movie_director = QLabel(self.layoutWidget)
        self.movie_director.setObjectName(u"movie_director")
        self.movie_director.setAlignment(Qt.AlignCenter)
        self.movie_info_layout.addWidget(self.movie_director)

        # Rating Layout
        self.rating_layout = QHBoxLayout()

        # Estrellas para rating
        self.rating_stars = []
        for i in range(5):
            star_button = QPushButton("★")
            star_button.setObjectName(f"star_{i+1}")
            star_button.setFixedSize(30, 30)
            star_button.setCheckable(False)
            self.rating_stars.append(star_button)
            self.rating_layout.addWidget(star_button)

        # Rating promedio
        self.average_rating = QLabel(self.layoutWidget)
        self.average_rating.setObjectName(u"average_rating")
        self.rating_layout.addWidget(self.average_rating)
        self.movie_info_layout.addLayout(self.rating_layout)

        self.verticalLayout.addLayout(self.movie_info_layout)
        self.verticalLayout.addWidget(self.image)
        self.upload_button = QPushButton(self.layoutWidget)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setMaximumSize(QSize(500, 30))

        self.verticalLayout.addWidget(self.upload_button)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.previous_button = QPushButton(self.layoutWidget)
        self.previous_button.setObjectName(u"previous_button")

        self.horizontalLayout.addWidget(self.previous_button)

        self.next_button = QPushButton(self.layoutWidget)
        self.next_button.setObjectName(u"next_button")

        self.horizontalLayout.addWidget(self.next_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PopcornHour", None))
        # self.comment_button.setText(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.image.setText("")
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"Upload new movie picture", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        # self.comment_button.setText(QCoreApplication.translate("MainWindow", u"Comment", None))
        self.upload_button.setText(QCoreApplication.translate("MainWindow", u"Upload Movie", None))
        self.previous_button.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.movie_title.setText(QCoreApplication.translate("MainWindow", u"Movie Title", None))
        self.movie_director.setText(QCoreApplication.translate("MainWindow", u"Director", None))
        self.average_rating.setText(QCoreApplication.translate("MainWindow", u"Average: 0.0 ★", None))
    # retranslateUi


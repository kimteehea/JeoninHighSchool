# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_Menu_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_User_Menu_window(object):
    def setupUi(self, User_Menu_window):
        if not User_Menu_window.objectName():
            User_Menu_window.setObjectName(u"User_Menu_window")
        User_Menu_window.resize(573, 251)
        self.questions = QPushButton(User_Menu_window)
        self.questions.setObjectName(u"questions")
        self.questions.setGeometry(QRect(120, 10, 331, 71))
        font = QFont()
        font.setPointSize(20)
        self.questions.setFont(font)
        self.Recode = QPushButton(User_Menu_window)
        self.Recode.setObjectName(u"Recode")
        self.Recode.setGeometry(QRect(120, 80, 331, 71))
        self.Recode.setFont(font)
        self.closed = QPushButton(User_Menu_window)
        self.closed.setObjectName(u"closed")
        self.closed.setGeometry(QRect(120, 150, 331, 71))
        self.closed.setFont(font)
        self.info = QLabel(User_Menu_window)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(350, 230, 221, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.info.setFont(font1)
        self.info.setStyleSheet(u"QLabel { \n"
"    border: 1px solid rgba(0, 0, 0, 0); \n"
"}\n"
"")
        self.version = QLabel(User_Menu_window)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(0, 230, 351, 21))
        self.version.setFont(font1)
        self.version.setStyleSheet(u"QLabel { \n"
"    border: 1px solid rgba(0, 0, 0, 0); \n"
"}\n"
"")

        self.retranslateUi(User_Menu_window)

        QMetaObject.connectSlotsByName(User_Menu_window)
    # setupUi

    def retranslateUi(self, User_Menu_window):
        User_Menu_window.setWindowTitle(QCoreApplication.translate("User_Menu_window", u"Form", None))
        self.questions.setText(QCoreApplication.translate("User_Menu_window", u"\uc2dc\ud5d8 \ubcf4\uae30", None))
        self.Recode.setText(QCoreApplication.translate("User_Menu_window", u"\uae30\ub85d", None))
        self.closed.setText(QCoreApplication.translate("User_Menu_window", u"\uc885\ub8cc", None))
        self.info.setText(QCoreApplication.translate("User_Menu_window", u"\uc0ac\uc6a9\uc790 \ub2d8 \ub85c\uadf8\uc778 \ud6c4 \uc0ac\uc6a9\ud574 \uc8fc\uc138\uc694.", None))
        self.version.setText(QCoreApplication.translate("User_Menu_window", u"SW \ubc84\uc804 : 25-01-22.01  |  \ud559\uc2b5\uc9c0 \ubc84\uc804 : 2025-01-10 10:55", None))
    # retranslateUi


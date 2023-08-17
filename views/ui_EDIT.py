# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EDITocvYHG.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_EDIT_USER_DETAILS_2(object):
    def setupUi(self, EditUserWindow):
        if not EditUserWindow.objectName():
            EditUserWindow.setObjectName(u"EDIT_USER_DETAILS_2")
        EditUserWindow.resize(236, 205)
        self.verticalLayout = QVBoxLayout(EditUserWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EDIT_USER_DETAILS = QLabel(EditUserWindow)
        self.EDIT_USER_DETAILS.setObjectName(u"EDIT_USER_DETAILS")

        self.verticalLayout.addWidget(self.EDIT_USER_DETAILS, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.firstName = QLineEdit(EditUserWindow)
        self.firstName.setObjectName(u"firstName")

        self.verticalLayout.addWidget(self.firstName)

        self.lastName = QLineEdit(EditUserWindow)
        self.lastName.setObjectName(u"lastName")

        self.verticalLayout.addWidget(self.lastName, 0, Qt.AlignTop)

        self.Email = QLineEdit(EditUserWindow)
        self.Email.setObjectName(u"Email")

        self.verticalLayout.addWidget(self.Email)

        self.Address = QLineEdit(EditUserWindow)
        self.Address.setObjectName(u"Address")

        self.verticalLayout.addWidget(self.Address)

        self.Done_btn = QPushButton(EditUserWindow)
        self.Done_btn.setObjectName(u"Done_btn")

        self.verticalLayout.addWidget(self.Done_btn)


        self.retranslateUi(EditUserWindow)

        QMetaObject.connectSlotsByName(EditUserWindow)
    # setupUi

    def retranslateUi(self, EditUserWindow):
        EditUserWindow.setWindowTitle(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"Form", None))
        self.EDIT_USER_DETAILS.setText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"EDIT THE USER DETAILS", None))
        self.firstName.setPlaceholderText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"firstname", None))
        self.lastName.setPlaceholderText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"lastname", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"email", None))
        self.Address.setPlaceholderText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"Address", None))
        self.Done_btn.setText(QCoreApplication.translate("EDIT_USER_DETAILS_2", u"DONE", None))
    # retranslateUi


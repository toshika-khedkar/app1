# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdduserlbpRmp.ui'
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

class Ui_AddUser(object):
    def setupUi(self, NewUsersWindow):
        if not NewUsersWindow.objectName():
            NewUsersWindow.setObjectName(u"Add users")
        NewUsersWindow.resize(236, 208)
        self.verticalLayout = QVBoxLayout(NewUsersWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.EDIT_USER_DETAILS = QLabel(NewUsersWindow)
        self.EDIT_USER_DETAILS.setObjectName(u"EDIT_USER_DETAILS")

        self.verticalLayout.addWidget(self.EDIT_USER_DETAILS, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.firstName = QLineEdit(NewUsersWindow)
        self.firstName.setObjectName(u"firstName")

        self.verticalLayout.addWidget(self.firstName)

        self.lastName = QLineEdit(NewUsersWindow)
        self.lastName.setObjectName(u"lastName")

        self.verticalLayout.addWidget(self.lastName, 0, Qt.AlignTop)

        self.Email = QLineEdit(NewUsersWindow)
        self.Email.setObjectName(u"Email")

        self.verticalLayout.addWidget(self.Email)

        self.Address = QLineEdit(NewUsersWindow)
        self.Address.setObjectName(u"Address")

        self.verticalLayout.addWidget(self.Address)

        self.Done_btn = QPushButton(NewUsersWindow)
        self.Done_btn.setObjectName(u"Done_btn")

        self.verticalLayout.addWidget(self.Done_btn)


        self.retranslateUi(NewUsersWindow)

        QMetaObject.connectSlotsByName(NewUsersWindow)
    # setupUi

    def retranslateUi(self, NewUsersWindow):
        NewUsersWindow.setWindowTitle(QCoreApplication.translate("Add User", u"Form", None))
        self.EDIT_USER_DETAILS.setText(QCoreApplication.translate("Add user", u"Add user", None))
        self.firstName.setPlaceholderText(QCoreApplication.translate("Add users", u"firstname", None))
        self.lastName.setPlaceholderText(QCoreApplication.translate("Add users", u"lastname", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("Add users", u"email", None))
        self.Address.setPlaceholderText(QCoreApplication.translate("Add users", u"Address", None))
        self.Done_btn.setText(QCoreApplication.translate("Add users", u"DONE", None))
    # retranslateUi


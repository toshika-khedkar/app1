# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btnhJTXmq.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, Ui_MainWindow):
        if not Ui_MainWindow.objectName():
            Ui_MainWindow.setObjectName(u"Ui_MainWindow")
        Ui_MainWindow.resize(965, 822)
        self.centralwidget = QWidget(Ui_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(67, 33, 100);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 0, 971, 91))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border:2px solid white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.AddUser_btn = QPushButton(NewUserWindow)
        self.AddUser_btn.setObjectName(u"AddUser_btn")
        self.AddUser_btn.setGeometry(QRect(330, 30, 75, 24))
        self.AddUser_btn.setCursor(QCursor(Qt.ArrowCursor))
        self.AddUser_btn.setAutoFillBackground(False)
        self.AddUser_btn.setStyleSheet(u"color:white;")
        self.EDIT_BTN = QPushButton(self.frame)
        self.EDIT_BTN.setObjectName(u"EDIT_BTN")
        self.EDIT_BTN.setGeometry(QRect(420, 30, 75, 24))
        self.EDIT_BTN.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 120, 1481, 391))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 10, 1431, 371))
        self.scrollArea.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border:2px solid white;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1427, 367))
        self.layoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 40, 571, 261))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(False)
        self.frame_3.setMinimumSize(QSize(550, 250))
        self.frame_3.setMaximumSize(QSize(550, 250))
        self.frame_3.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"border:2px solid white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.listUsersTable = QTableWidget(self.frame_3)
        if (self.listUsersTable.columnCount() < 4):
            self.listUsersTable.setColumnCount(4)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.listUsersTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.listUsersTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.listUsersTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.listUsersTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.listUsersTable.rowCount() < 2):
            self.listUsersTable.setRowCount(2)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.listUsersTable.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.listUsersTable.setVerticalHeaderItem(1, __qtablewidgetitem5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense4Pattern)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setForeground(brush);
        self.listUsersTable.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.listUsersTable.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.listUsersTable.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.listUsersTable.setItem(1, 3, __qtablewidgetitem9)
        self.listUsersTable.setObjectName(u"listUsersTable")
        self.listUsersTable.setGeometry(QRect(20, 10, 481, 221))
        self.listUsersTable.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(7, 0, 0);")

        self.horizontalLayout.addWidget(self.frame_3)

        self.booksQtyLabel = QLabel(self.scrollAreaWidgetContents)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(380, 320, 49, 16))
        self.booksQtyLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Ui_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Ui_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 965, 22))
        Ui_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Ui_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        Ui_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_MainWindow)

        QMetaObject.connectSlotsByName(Ui_MainWindow)
    # setupUi

    def retranslateUi(self, Ui_MainWindow):
        Ui_MainWindow.setWindowTitle(QCoreApplication.translate("Ui_MainWindow", u"Ui_MainWindow", None))
        self.AddUser_btn.setText(QCoreApplication.translate("Ui_MainWindow", u"ADDUSER", None))
        self.EDIT_BTN.setText(QCoreApplication.translate("Ui_MainWindow", u"EDIT", None))
        ___qtablewidgetitem = self.listUsersTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ui_MainWindow", u"FirstName", None));
        ___qtablewidgetitem1 = self.listUsersTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ui_MainWindow", u"LastName", None));
        ___qtablewidgetitem2 = self.listUsersTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Ui_MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.listUsersTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Ui_MainWindow", u"Address", None));

        __sortingEnabled = self.listUsersTable.isSortingEnabled()
        self.listUsersTable.setSortingEnabled(False)
        self.listUsersTable.setSortingEnabled(__sortingEnabled)

        self.booksQtyLabel.setText(QCoreApplication.translate("Ui_MainWindow", u"TextLabel", None))
    # retranslateUi


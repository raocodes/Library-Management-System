# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myapp.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 550)
        MainWindow.setMinimumSize(QSize(850, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.issuetab = QWidget()
        self.issuetab.setObjectName(u"issuetab")
        self.horizontalLayout = QHBoxLayout(self.issuetab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftlayoutissue = QVBoxLayout()
        self.leftlayoutissue.setObjectName(u"leftlayoutissue")
        self.booklist = QListWidget(self.issuetab)
        self.booklist.setObjectName(u"booklist")

        self.leftlayoutissue.addWidget(self.booklist)

        self.errorlabel = QLabel(self.issuetab)
        self.errorlabel.setObjectName(u"errorlabel")
        font = QFont()
        font.setBold(True)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet(u"color: orange")

        self.leftlayoutissue.addWidget(self.errorlabel)


        self.horizontalLayout.addLayout(self.leftlayoutissue)

        self.issueline = QFrame(self.issuetab)
        self.issueline.setObjectName(u"issueline")
        self.issueline.setFrameShape(QFrame.VLine)
        self.issueline.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.issueline)

        self.rightlayout = QVBoxLayout()
        self.rightlayout.setSpacing(20)
        self.rightlayout.setObjectName(u"rightlayout")
        self.viewmode = QGroupBox(self.issuetab)
        self.viewmode.setObjectName(u"viewmode")
        font1 = QFont()
        font1.setBold(False)
        self.viewmode.setFont(font1)
        self.viewmode.setFlat(False)
        self.verticalLayout_2 = QVBoxLayout(self.viewmode)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, -1, 6, -1)
        self.avaiablebooksbutton = QRadioButton(self.viewmode)
        self.avaiablebooksbutton.setObjectName(u"avaiablebooksbutton")

        self.verticalLayout_2.addWidget(self.avaiablebooksbutton)

        self.allbooksbutton = QRadioButton(self.viewmode)
        self.allbooksbutton.setObjectName(u"allbooksbutton")

        self.verticalLayout_2.addWidget(self.allbooksbutton)


        self.rightlayout.addWidget(self.viewmode)

        self.sortby = QGroupBox(self.issuetab)
        self.sortby.setObjectName(u"sortby")
        self.sortby.setFlat(False)
        self.verticalLayout_3 = QVBoxLayout(self.sortby)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, -1, 6, -1)
        self.titlebutton = QRadioButton(self.sortby)
        self.titlebutton.setObjectName(u"titlebutton")

        self.verticalLayout_3.addWidget(self.titlebutton)

        self.authorbutton = QRadioButton(self.sortby)
        self.authorbutton.setObjectName(u"authorbutton")

        self.verticalLayout_3.addWidget(self.authorbutton)

        self.ratingbutton = QRadioButton(self.sortby)
        self.ratingbutton.setObjectName(u"ratingbutton")

        self.verticalLayout_3.addWidget(self.ratingbutton)


        self.rightlayout.addWidget(self.sortby)

        self.genre = QGroupBox(self.issuetab)
        self.genre.setObjectName(u"genre")
        self.genre.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.genre)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, 6, -1)
        self.genrebox = QComboBox(self.genre)
        self.genrebox.setObjectName(u"genrebox")

        self.verticalLayout_4.addWidget(self.genrebox)


        self.rightlayout.addWidget(self.genre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.rightlayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.issuetab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.refreshbutton = QPushButton(self.groupBox)
        self.refreshbutton.setObjectName(u"refreshbutton")
        self.refreshbutton.setMinimumSize(QSize(0, 25))
        self.refreshbutton.setStyleSheet(u"QPushButton#refreshbutton{\n"
"	background-color: #3c73a6;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#refreshbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout_5.addWidget(self.refreshbutton)

        self.issuebutton = QPushButton(self.groupBox)
        self.issuebutton.setObjectName(u"issuebutton")
        self.issuebutton.setMinimumSize(QSize(0, 25))
        self.issuebutton.setStyleSheet(u"QPushButton#issuebutton{\n"
"	background-color: MediumSeaGreen;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#issuebutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout_5.addWidget(self.issuebutton)

        self.detailsbutton = QPushButton(self.groupBox)
        self.detailsbutton.setObjectName(u"detailsbutton")
        self.detailsbutton.setMinimumSize(QSize(0, 25))
        self.detailsbutton.setStyleSheet(u"QPushButton#detailsbutton{\n"
"	background-color: #f2a240;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#detailsbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout_5.addWidget(self.detailsbutton)

        self.adminbutton = QPushButton(self.groupBox)
        self.adminbutton.setObjectName(u"adminbutton")
        self.adminbutton.setMinimumSize(QSize(0, 25))
        self.adminbutton.setStyleSheet(u"QPushButton#adminbutton{\n"
"	background-color: #ed7868;\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton#adminbutton:hover{\n"
"	border: 2px solid teal;\n"
"}")

        self.verticalLayout_5.addWidget(self.adminbutton)


        self.rightlayout.addWidget(self.groupBox)

        self.rightlayout.setStretch(0, 4)
        self.rightlayout.setStretch(1, 5)
        self.rightlayout.setStretch(2, 2)
        self.rightlayout.setStretch(3, 10)
        self.rightlayout.setStretch(4, 4)

        self.horizontalLayout.addLayout(self.rightlayout)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(2, 1)
        self.tabWidget.addTab(self.issuetab, "")
        self.deposittab = QWidget()
        self.deposittab.setObjectName(u"deposittab")
        self.horizontalLayout_3 = QHBoxLayout(self.deposittab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.returnbooklist = QListWidget(self.deposittab)
        self.returnbooklist.setObjectName(u"returnbooklist")

        self.horizontalLayout_3.addWidget(self.returnbooklist)

        self.depositline = QFrame(self.deposittab)
        self.depositline.setObjectName(u"depositline")
        self.depositline.setFrameShape(QFrame.VLine)
        self.depositline.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.depositline)

        self.rightlayoutdeposit = QVBoxLayout()
        self.rightlayoutdeposit.setObjectName(u"rightlayoutdeposit")
        self.memberlayout = QVBoxLayout()
        self.memberlayout.setObjectName(u"memberlayout")
        self.enterlayout = QHBoxLayout()
        self.enterlayout.setObjectName(u"enterlayout")
        self.memberlabel = QLabel(self.deposittab)
        self.memberlabel.setObjectName(u"memberlabel")

        self.enterlayout.addWidget(self.memberlabel)

        self.idfield = QLineEdit(self.deposittab)
        self.idfield.setObjectName(u"idfield")

        self.enterlayout.addWidget(self.idfield)


        self.memberlayout.addLayout(self.enterlayout)

        self.errorlabeldeposit = QLabel(self.deposittab)
        self.errorlabeldeposit.setObjectName(u"errorlabeldeposit")
        self.errorlabeldeposit.setStyleSheet(u"")

        self.memberlayout.addWidget(self.errorlabeldeposit)

        self.viewbookbutton = QPushButton(self.deposittab)
        self.viewbookbutton.setObjectName(u"viewbookbutton")

        self.memberlayout.addWidget(self.viewbookbutton)

        self.viewbookhistorybutton = QPushButton(self.deposittab)
        self.viewbookhistorybutton.setObjectName(u"viewbookhistorybutton")

        self.memberlayout.addWidget(self.viewbookhistorybutton)


        self.rightlayoutdeposit.addLayout(self.memberlayout)

        self.ratinglayout = QVBoxLayout()
        self.ratinglayout.setObjectName(u"ratinglayout")
        self.ratinglabel = QLabel(self.deposittab)
        self.ratinglabel.setObjectName(u"ratinglabel")

        self.ratinglayout.addWidget(self.ratinglabel)

        self.onestar = QRadioButton(self.deposittab)
        self.onestar.setObjectName(u"onestar")

        self.ratinglayout.addWidget(self.onestar)

        self.twostar = QRadioButton(self.deposittab)
        self.twostar.setObjectName(u"twostar")

        self.ratinglayout.addWidget(self.twostar)

        self.threestar = QRadioButton(self.deposittab)
        self.threestar.setObjectName(u"threestar")

        self.ratinglayout.addWidget(self.threestar)

        self.fourstar = QRadioButton(self.deposittab)
        self.fourstar.setObjectName(u"fourstar")

        self.ratinglayout.addWidget(self.fourstar)

        self.fivestar = QRadioButton(self.deposittab)
        self.fivestar.setObjectName(u"fivestar")

        self.ratinglayout.addWidget(self.fivestar)


        self.rightlayoutdeposit.addLayout(self.ratinglayout)

        self.returnbutton = QPushButton(self.deposittab)
        self.returnbutton.setObjectName(u"returnbutton")

        self.rightlayoutdeposit.addWidget(self.returnbutton)


        self.horizontalLayout_3.addLayout(self.rightlayoutdeposit)

        self.tabWidget.addTab(self.deposittab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.errorlabel.setText("")
        self.viewmode.setTitle(QCoreApplication.translate("MainWindow", u"View mode:", None))
        self.avaiablebooksbutton.setText(QCoreApplication.translate("MainWindow", u"Books available", None))
        self.allbooksbutton.setText(QCoreApplication.translate("MainWindow", u"All books", None))
        self.sortby.setTitle(QCoreApplication.translate("MainWindow", u"Sort by:", None))
        self.titlebutton.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.authorbutton.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.ratingbutton.setText(QCoreApplication.translate("MainWindow", u"Rating", None))
        self.genre.setTitle(QCoreApplication.translate("MainWindow", u"Genre:", None))
        self.groupBox.setTitle("")
        self.refreshbutton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.issuebutton.setText(QCoreApplication.translate("MainWindow", u"Issue", None))
        self.detailsbutton.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.adminbutton.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.issuetab), QCoreApplication.translate("MainWindow", u"Issue Book", None))
        self.memberlabel.setText(QCoreApplication.translate("MainWindow", u"Enter Member ID:", None))
        self.errorlabeldeposit.setText("")
        self.viewbookbutton.setText(QCoreApplication.translate("MainWindow", u"View books issued", None))
        self.viewbookhistorybutton.setText(QCoreApplication.translate("MainWindow", u"View history of books issued", None))
        self.ratinglabel.setText(QCoreApplication.translate("MainWindow", u"Leave a rating for the book:", None))
        self.onestar.setText("")
        self.twostar.setText(QCoreApplication.translate("MainWindow", u"\u2b50\u2b50", None))
        self.threestar.setText(QCoreApplication.translate("MainWindow", u"\u2b50\u2b50\u2b50", None))
        self.fourstar.setText(QCoreApplication.translate("MainWindow", u"\u2b50\u2b50\u2b50\u2b50", None))
        self.fivestar.setText(QCoreApplication.translate("MainWindow", u"\u2b50\ufe0f\u2b50\ufe0f\u2b50\ufe0f\u2b50\ufe0f\u2b50\ufe0f", None))
        self.returnbutton.setText(QCoreApplication.translate("MainWindow", u"Return Book", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.deposittab), QCoreApplication.translate("MainWindow", u"Deposit Book", None))
    # retranslateUi


# Form implementation generated from reading ui file 'UI/uifiles/admin.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(900, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdminWindow.sizePolicy().hasHeightForWidth())
        AdminWindow.setSizePolicy(sizePolicy)
        AdminWindow.setMinimumSize(QtCore.QSize(900, 500))
        AdminWindow.setMaximumSize(QtCore.QSize(900, 500))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        AdminWindow.setFont(font)
        self.formLayout = QtWidgets.QFormLayout(AdminWindow)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(AdminWindow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.memtab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memtab.sizePolicy().hasHeightForWidth())
        self.memtab.setSizePolicy(sizePolicy)
        self.memtab.setObjectName("memtab")
        self.memtable = QtWidgets.QTableWidget(self.memtab)
        self.memtable.setGeometry(QtCore.QRect(10, 10, 851, 341))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.memtable.setFont(font)
        self.memtable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.memtable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.memtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.memtable.setObjectName("memtable")
        self.memtable.setColumnCount(4)
        self.memtable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.memtable.setHorizontalHeaderItem(3, item)
        self.memtable.horizontalHeader().setVisible(False)
        self.memtable.verticalHeader().setVisible(False)
        self.layoutWidget = QtWidgets.QWidget(self.memtab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 380, 851, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addmem = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.addmem.setFont(font)
        self.addmem.setStyleSheet("background-color : blue;\n"
"color: white;")
        self.addmem.setObjectName("addmem")
        self.horizontalLayout.addWidget(self.addmem)
        self.refreshmem = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.refreshmem.setFont(font)
        self.refreshmem.setStyleSheet("background-color : green;\n"
"color: white;")
        self.refreshmem.setObjectName("refreshmem")
        self.horizontalLayout.addWidget(self.refreshmem)
        self.deletemem = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.deletemem.setFont(font)
        self.deletemem.setStyleSheet("background-color : red;\n"
"color: white;")
        self.deletemem.setObjectName("deletemem")
        self.horizontalLayout.addWidget(self.deletemem)
        self.tabWidget.addTab(self.memtab, "")
        self.booktab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.booktab.sizePolicy().hasHeightForWidth())
        self.booktab.setSizePolicy(sizePolicy)
        self.booktab.setObjectName("booktab")
        self.booktable = QtWidgets.QTableWidget(self.booktab)
        self.booktable.setGeometry(QtCore.QRect(10, 10, 851, 341))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        self.booktable.setFont(font)
        self.booktable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.booktable.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.booktable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.booktable.setObjectName("booktable")
        self.booktable.setColumnCount(6)
        self.booktable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.booktable.setHorizontalHeaderItem(5, item)
        self.booktable.horizontalHeader().setVisible(False)
        self.booktable.verticalHeader().setVisible(False)
        self.layoutWidget_2 = QtWidgets.QWidget(self.booktab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 380, 851, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addbook = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.addbook.setFont(font)
        self.addbook.setStyleSheet("background-color : blue;\n"
"color: white;")
        self.addbook.setObjectName("addbook")
        self.horizontalLayout_2.addWidget(self.addbook)
        self.refreshbook = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.refreshbook.setFont(font)
        self.refreshbook.setStyleSheet("background-color : green;\n"
"color: white;")
        self.refreshbook.setObjectName("refreshbook")
        self.horizontalLayout_2.addWidget(self.refreshbook)
        self.deletebook = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.deletebook.setFont(font)
        self.deletebook.setStyleSheet("background-color : red;\n"
"color: white;")
        self.deletebook.setObjectName("deletebook")
        self.horizontalLayout_2.addWidget(self.deletebook)
        self.tabWidget.addTab(self.booktab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.tabWidget)

        self.retranslateUi(AdminWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Admin"))
        item = self.memtable.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "ID"))
        item = self.memtable.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Name"))
        item = self.memtable.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "DOB"))
        item = self.memtable.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "DOR"))
        self.addmem.setText(_translate("AdminWindow", "Add"))
        self.refreshmem.setText(_translate("AdminWindow", "Refresh"))
        self.deletemem.setText(_translate("AdminWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.memtab), _translate("AdminWindow", "Members"))
        item = self.booktable.horizontalHeaderItem(0)
        item.setText(_translate("AdminWindow", "ID"))
        item = self.booktable.horizontalHeaderItem(1)
        item.setText(_translate("AdminWindow", "Title"))
        item = self.booktable.horizontalHeaderItem(2)
        item.setText(_translate("AdminWindow", "Author"))
        item = self.booktable.horizontalHeaderItem(3)
        item.setText(_translate("AdminWindow", "Genre"))
        item = self.booktable.horizontalHeaderItem(4)
        item.setText(_translate("AdminWindow", "Total"))
        item = self.booktable.horizontalHeaderItem(5)
        item.setText(_translate("AdminWindow", "Issued"))
        self.addbook.setText(_translate("AdminWindow", "Add"))
        self.refreshbook.setText(_translate("AdminWindow", "Refresh"))
        self.deletebook.setText(_translate("AdminWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booktab), _translate("AdminWindow", "Books"))

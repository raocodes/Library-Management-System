# Form implementation generated from reading ui file 'UI/uifiles/deletemembers.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_deletememdialog(object):
    def setupUi(self, deletememdialog):
        deletememdialog.setObjectName("deletememdialog")
        deletememdialog.resize(400, 200)
        deletememdialog.setMinimumSize(QtCore.QSize(400, 200))
        deletememdialog.setMaximumSize(QtCore.QSize(400, 200))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(deletememdialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.memlist = QtWidgets.QListWidget(deletememdialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.memlist.setFont(font)
        self.memlist.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.memlist.setObjectName("memlist")
        self.horizontalLayout.addWidget(self.memlist)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.deletebutton = QtWidgets.QPushButton(deletememdialog)
        self.deletebutton.setMinimumSize(QtCore.QSize(0, 35))
        self.deletebutton.setStyleSheet("QPushButton#deletebutton{\n"
"    background-color: red;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#deletebutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.deletebutton.setObjectName("deletebutton")
        self.verticalLayout.addWidget(self.deletebutton)
        self.closebutton = QtWidgets.QPushButton(deletememdialog)
        self.closebutton.setMinimumSize(QtCore.QSize(0, 35))
        self.closebutton.setStyleSheet("QPushButton#closebutton{\n"
"    background-color: #656565;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#closebutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.closebutton.setObjectName("closebutton")
        self.verticalLayout.addWidget(self.closebutton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.errorlabel = QtWidgets.QLabel(deletememdialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet("color: orange;")
        self.errorlabel.setText("")
        self.errorlabel.setObjectName("errorlabel")
        self.verticalLayout_2.addWidget(self.errorlabel)
        self.verticalLayout_2.setStretch(0, 8)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(deletememdialog)
        QtCore.QMetaObject.connectSlotsByName(deletememdialog)

    def retranslateUi(self, deletememdialog):
        _translate = QtCore.QCoreApplication.translate
        deletememdialog.setWindowTitle(_translate("deletememdialog", "Delete Members"))
        self.deletebutton.setText(_translate("deletememdialog", "Delete"))
        self.closebutton.setText(_translate("deletememdialog", "Close"))

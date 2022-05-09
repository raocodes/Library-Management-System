# Form implementation generated from reading ui file 'UI/uifiles/addmembers.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_addmemdialog(object):
    def setupUi(self, addmemdialog):
        addmemdialog.setObjectName("addmemdialog")
        addmemdialog.resize(400, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(addmemdialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputform = QtWidgets.QFormLayout()
        self.inputform.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.inputform.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputform.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.inputform.setContentsMargins(10, -1, 10, -1)
        self.inputform.setHorizontalSpacing(40)
        self.inputform.setVerticalSpacing(25)
        self.inputform.setObjectName("inputform")
        self.name = QtWidgets.QLabel(addmemdialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.inputform.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.name)
        self.dob = QtWidgets.QLabel(addmemdialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.dob.setFont(font)
        self.dob.setObjectName("dob")
        self.inputform.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.dob)
        self.inputname = QtWidgets.QLineEdit(addmemdialog)
        self.inputname.setMinimumSize(QtCore.QSize(0, 30))
        self.inputname.setObjectName("inputname")
        self.inputform.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputname)
        self.datepicker = QtWidgets.QDateEdit(addmemdialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.datepicker.sizePolicy().hasHeightForWidth())
        self.datepicker.setSizePolicy(sizePolicy)
        self.datepicker.setMinimumSize(QtCore.QSize(0, 30))
        self.datepicker.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.datepicker.setCalendarPopup(False)
        self.datepicker.setObjectName("datepicker")
        self.inputform.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.datepicker)
        self.verticalLayout.addLayout(self.inputform)
        self.error = QtWidgets.QLabel(addmemdialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.error.setFont(font)
        self.error.setStyleSheet("color: orange")
        self.error.setText("")
        self.error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
        self.buttonlayout = QtWidgets.QHBoxLayout()
        self.buttonlayout.setObjectName("buttonlayout")
        self.clearbutton = QtWidgets.QPushButton(addmemdialog)
        self.clearbutton.setMinimumSize(QtCore.QSize(0, 25))
        self.clearbutton.setStyleSheet("QPushButton#clearbutton{\n"
"    background-color: cornflowerblue;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#clearbutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.clearbutton.setObjectName("clearbutton")
        self.buttonlayout.addWidget(self.clearbutton)
        self.submitbutton = QtWidgets.QPushButton(addmemdialog)
        self.submitbutton.setMinimumSize(QtCore.QSize(0, 25))
        self.submitbutton.setStyleSheet("QPushButton#submitbutton{\n"
"    background-color: green;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#submitbutton:hover{\n"
"    border: 2px solid teal;\n"
"}")
        self.submitbutton.setObjectName("submitbutton")
        self.buttonlayout.addWidget(self.submitbutton)
        self.closebutton = QtWidgets.QPushButton(addmemdialog)
        self.closebutton.setMinimumSize(QtCore.QSize(0, 25))
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
        self.buttonlayout.addWidget(self.closebutton)
        self.verticalLayout.addLayout(self.buttonlayout)

        self.retranslateUi(addmemdialog)
        QtCore.QMetaObject.connectSlotsByName(addmemdialog)

    def retranslateUi(self, addmemdialog):
        _translate = QtCore.QCoreApplication.translate
        addmemdialog.setWindowTitle(_translate("addmemdialog", "Add Members"))
        self.name.setText(_translate("addmemdialog", "Name:"))
        self.dob.setText(_translate("addmemdialog", "DOB:"))
        self.datepicker.setDisplayFormat(_translate("addmemdialog", "dd/MM/yyyy"))
        self.clearbutton.setText(_translate("addmemdialog", "Clear"))
        self.submitbutton.setText(_translate("addmemdialog", "Submit"))
        self.closebutton.setText(_translate("addmemdialog", "Close"))

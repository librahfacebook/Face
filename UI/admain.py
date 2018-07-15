# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admainDialog(object):
    def setupUi(self, admainDialog):
        admainDialog.setObjectName("admainDialog")
        admainDialog.resize(541, 354)
        self.label = QtWidgets.QLabel(admainDialog)
        self.label.setGeometry(QtCore.QRect(230, 0, 101, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(admainDialog)
        self.label_3.setGeometry(QtCore.QRect(170, 90, 71, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nameEdit = QtWidgets.QLineEdit(admainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(250, 90, 113, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.label_4 = QtWidgets.QLabel(admainDialog)
        self.label_4.setGeometry(QtCore.QRect(170, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.classEdit = QtWidgets.QLineEdit(admainDialog)
        self.classEdit.setGeometry(QtCore.QRect(250, 140, 113, 20))
        self.classEdit.setObjectName("classEdit")
        self.label_5 = QtWidgets.QLabel(admainDialog)
        self.label_5.setGeometry(QtCore.QRect(140, 190, 101, 20))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.photoButton = QtWidgets.QPushButton(admainDialog)
        self.photoButton.setGeometry(QtCore.QRect(380, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.photoButton.setFont(font)
        self.photoButton.setObjectName("photoButton")
        self.addButton = QtWidgets.QPushButton(admainDialog)
        self.addButton.setGeometry(QtCore.QRect(260, 250, 61, 31))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setAutoFillBackground(False)
        self.addButton.setObjectName("addButton")
        self.imgEdit = QtWidgets.QLineEdit(admainDialog)
        self.imgEdit.setGeometry(QtCore.QRect(250, 190, 113, 20))
        self.imgEdit.setObjectName("imgEdit")

        self.retranslateUi(admainDialog)
        self.photoButton.clicked.connect(admainDialog.takePhoto)
        self.addButton.clicked.connect(admainDialog.addUser)
        QtCore.QMetaObject.connectSlotsByName(admainDialog)

    def retranslateUi(self, admainDialog):
        _translate = QtCore.QCoreApplication.translate
        admainDialog.setWindowTitle(_translate("admainDialog", "管理员"))
        self.label.setText(_translate("admainDialog", "用户管理"))
        self.label_3.setText(_translate("admainDialog", "用户姓名"))
        self.label_4.setText(_translate("admainDialog", "用户班级"))
        self.label_5.setText(_translate("admainDialog", "添加个人照片"))
        self.photoButton.setText(_translate("admainDialog", "拍照"))
        self.addButton.setText(_translate("admainDialog", "添加"))

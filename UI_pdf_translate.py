# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_pdf_translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pdf_translate(object):
    def setupUi(self, pdf_translate):
        pdf_translate.setObjectName("pdf_translate")
        pdf_translate.resize(1280, 900)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(pdf_translate)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(pdf_translate)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_translate = QtWidgets.QPushButton(self.widget)
        self.pushButton_translate.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_translate.setObjectName("pushButton_translate")
        self.horizontalLayout.addWidget(self.pushButton_translate)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_paste_translate = QtWidgets.QPushButton(self.widget)
        self.pushButton_paste_translate.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_paste_translate.setObjectName("pushButton_paste_translate")
        self.horizontalLayout.addWidget(self.pushButton_paste_translate)
        self.pushButton_screenshot = QtWidgets.QPushButton(self.widget)
        self.pushButton_screenshot.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_screenshot.setObjectName("pushButton_screenshot")
        self.horizontalLayout.addWidget(self.pushButton_screenshot)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit_pdf_text = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_pdf_text.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.plainTextEdit_pdf_text.setOverwriteMode(False)
        self.plainTextEdit_pdf_text.setObjectName("plainTextEdit_pdf_text")
        self.verticalLayout.addWidget(self.plainTextEdit_pdf_text)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setEnabled(False)
        self.widget1.setMaximumSize(QtCore.QSize(16777215, 0))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(pdf_translate)
        QtCore.QMetaObject.connectSlotsByName(pdf_translate)

    def retranslateUi(self, pdf_translate):
        _translate = QtCore.QCoreApplication.translate
        pdf_translate.setWindowTitle(_translate("pdf_translate", "PDF translator"))
        self.pushButton_translate.setText(_translate("pdf_translate", "直接翻译"))
        self.pushButton_clear.setText(_translate("pdf_translate", "清空"))
        self.pushButton_paste_translate.setText(_translate("pdf_translate", "先粘贴后翻译"))
        self.pushButton_screenshot.setText(_translate("pdf_translate", "截图"))

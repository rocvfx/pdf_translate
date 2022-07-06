from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyperclip

import sys
from UI_pdf_translate_designed import Ui_Form


class myWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 调用父类的setupUI函数

        self.pushButton_translate.clicked.connect(self.format_pdf_text)  # 将按钮点击事件和helloworld函数绑定

    def format_pdf_text(self):

        temp_text = pyperclip.waitForPaste()
        #temp_text.replace("\r\n", " ")
        clean_text = temp_text.replace('\n', '').replace('\r', '')
        clean_text.strip()
        self.plainTextEdit_pdf_text.setPlainText(clean_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = myWindow()
    ui.show()
    sys.exit(app.exec_())
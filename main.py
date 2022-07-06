from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyperclip
import pyautogui
import sys
import time
from UI_pdf_translate_designed import Ui_pdf_translate


class myWindow(QWidget, Ui_pdf_translate):
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
        self.plainTextEdit_pdf_text.setFocus()
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'a')  # 按键ctrl+c
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'f9')  # 按键ctrl+c



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = myWindow()
    ui.show()
    sys.exit(app.exec_())
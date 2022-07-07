from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pyperclip
import pyautogui
import sys
import time



from UI_pdf_translate import Ui_pdf_translate

#pyautogui.PAUSE = 0.5

class myWindow(QWidget, Ui_pdf_translate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_translate.clicked.connect(self.format_pdf_text)

    def format_pdf_text(self):
        temp_text = pyperclip.paste()
        #temp_text.replace("\r\n", " ")
        clean_text = temp_text.replace('\n', ' ').replace('\r', ' ')
        #clean_text.strip()
        self.plainTextEdit_pdf_text.setPlainText(clean_text)
        self.plainTextEdit_pdf_text.setFocus()
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')  # 按键ctrl+a 全选文本
        time.sleep(0.1)
        #pyautogui.hotkey('ctrl', 'c', 'c')  # 召唤deepl
        pyautogui.keyDown('ctrl')
        pyautogui.press(['c', 'c'])
        pyautogui.keyUp('ctrl')

def main():
    app = QApplication(sys.argv)
    ui = myWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    # app = QApplication(sys.argv)
    # ui = myWindow()
    # ui.show()
    # sys.exit(app.exec_())
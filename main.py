from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
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


        self.webview = QWebEngineView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.webview.sizePolicy().hasHeightForWidth())
        self.webview.setSizePolicy(sizePolicy)
        self.webview.setObjectName("webview")
        self.splitter.addWidget(self.webview)


        url = 'http://webdemo.myscript.com/views/math/index.html'

        self.webview.load(QUrl(url))



        self.pushButton_translate.clicked.connect(self.format_pdf_text)
        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_paste_translate.clicked.connect(self.paste_translate)
        self.pushButton_screenshot.clicked.connect(self.screenshot)

    def clear(self):
        self.plainTextEdit_pdf_text.setPlainText('')

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

    def paste_translate(self):
        temp_text = self.plainTextEdit_pdf_text.toPlainText()
        clean_text = temp_text.replace('\n', ' ').replace('\r', ' ')
        self.plainTextEdit_pdf_text.setPlainText(clean_text)
        self.plainTextEdit_pdf_text.setFocus()
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')  # 按键ctrl+a 全选文本
        time.sleep(0.1)
        # pyautogui.hotkey('ctrl', 'c', 'c')  # 召唤deepl
        pyautogui.keyDown('ctrl')
        pyautogui.press(['c', 'c'])
        pyautogui.keyUp('ctrl')

    def screenshot(self):
        pyautogui.hotkey('shift','win', 's')  # 系统截图
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
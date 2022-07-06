from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from UI_pdf_translate_designed import Ui_Form


class myWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 调用父类的setupUI函数

        self.pushButton.clicked.connect(self.helloworld)  # 将按钮点击事件和helloworld函数绑定




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = myWindow()
    ui.show()
    sys.exit(app.exec_())
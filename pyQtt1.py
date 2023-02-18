import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


form = resource_path('test.ui')
form_class = uic.loadUiType(form)[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # btn_test 클릭 시 testclick 함수 실행
        self.btn_test.clicked.connect(self.testclick)

    # 실행될 함수
    def testclick(self):
        print('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
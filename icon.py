#!/usr/bin/python3
# -*- coding: utf-8 -*-

import ctypes
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

myappid = u'nik.guikablui.test.v0.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


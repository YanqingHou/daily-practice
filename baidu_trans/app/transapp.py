# coding = utf-8
from fanyi_api import transapi
from ui.transui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
"""
    作者： XH
    功能： 运行程序， 开启APP主窗体
    日期： 2019-4-3
"""

class TransApp:

    def __init__(self):
        self.ui = Ui_MainWindow()

    def start(self):
        app = QApplication(sys.argv)
        mainwindow = QMainWindow()
        self.ui.setupUi(mainwindow)
        mainwindow.show()
        sys.exit(app.exec())



# coding = utf-8
import sys

from camera.videowidget import VideoWidget
from PyQt5.QtWidgets import QApplication
"""
作者:xh
功能：弹出界面，启动摄像头功能
日期：2019-3-28
"""


def start():
    app = QApplication(sys.argv)
    widget = VideoWidget()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    start()

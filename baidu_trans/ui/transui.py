# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from fanyi_api.transapi import TransApi
"""
    作者: XH
    功能: 生成界面，监控点击事件，触发时调用槽函数进行翻译
    日期： 2019-4-3
"""

class Ui_MainWindow(object):

    languge_list = ['auto', 'zh', 'en', 'yue', 'wyw', 'jp', 'kor', 'fra',
                    'spa', 'ara', 'ru', 'de']

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 320)
        MainWindow.setMinimumSize(QtCore.QSize(487, 320))
        MainWindow.setBaseSize(QtCore.QSize(487, 320))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 170, 80, 29))
        self.pushButton.setObjectName("pushButton")
        # -------pushbutton绑定槽函数--------
        self.pushButton.pressed.connect(self.pushbutton_slot)
        #------------------------------
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 50, 81, 29))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(12, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(330, 50, 81, 29))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 100, 151, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(300, 100, 151, 181))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自用翻译器 by XH"))
        self.pushButton.setText(_translate("MainWindow", "翻译"))
        self.comboBox.setItemText(0, _translate("MainWindow", "自动检测"))
        self.comboBox.setItemText(1, _translate("MainWindow", "中文"))
        self.comboBox.setItemText(2, _translate("MainWindow", "英语"))
        self.comboBox.setItemText(3, _translate("MainWindow", "粤语"))
        self.comboBox.setItemText(4, _translate("MainWindow", "文言文"))
        self.comboBox.setItemText(5, _translate("MainWindow", "日语"))
        self.comboBox.setItemText(6, _translate("MainWindow", "韩语"))
        self.comboBox.setItemText(7, _translate("MainWindow", "法语"))
        self.comboBox.setItemText(8, _translate("MainWindow", "西班牙语"))
        self.comboBox.setItemText(9, _translate("MainWindow", "阿拉伯语"))
        self.comboBox.setItemText(10, _translate("MainWindow", "俄语"))
        self.comboBox.setItemText(11, _translate("MainWindow", "德语"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "中文"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "英语"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "粤语"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "文言文"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "日语"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "韩语"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "法语"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "西班牙语"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "阿拉伯语"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "俄语"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "德语"))
        self.textEdit_2.setHtml(
            _translate(
                "MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:\'Noto Sans CJK SC\'; font-size:9.7pt; font-weight:400; font-style:normal;\">\n"
                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请输入待翻译文本</p></body></html>"))

    def pushbutton_slot(self):  # 绑定在pushbottun上的槽函数
        """
        触发翻译按钮，传递数据进行翻译，接收返回值显示
        :return:
        """
        print('翻译已经开始')
        # 获取输入的文本内容
        self.text = self.textEdit_2.toPlainText()
        # 获取选中的待翻译语言种类
        from_lag = self.languge_list[self.comboBox.currentIndex()]
        # 获取选中的目标语种
        to = self.languge_list[self.comboBox_2.currentIndex()+1]
        # 将参数传向API，获取返回值
        result = TransApi(keyword=self.text, from_language=from_lag, to=to).baidu_trans()
        # 在屏幕上显示翻译结果
        self.textBrowser.setText(result)
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spider.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 570)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(700, 570))
        MainWindow.setAcceptDrops(True)
        #        MainWindow.setAnimated(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 270, 681, 171))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.urlEdit = QtGui.QLineEdit(self.groupBox)
        self.urlEdit.setGeometry(QtCore.QRect(110, 20, 461, 20))
        self.urlEdit.setObjectName(_fromUtf8("urlEdit"))
        self.chmEdit = QtGui.QLineEdit(self.groupBox)
        self.chmEdit.setGeometry(QtCore.QRect(110, 50, 461, 20))
        self.chmEdit.setObjectName(_fromUtf8("chmEdit"))
        self.browseChm = QtGui.QPushButton(self.groupBox)
        self.browseChm.setGeometry(QtCore.QRect(580, 50, 75, 23))
        self.browseChm.setObjectName(_fromUtf8("browseChm"))
        self.startButton = QtGui.QPushButton(self.groupBox)
        self.startButton.setGeometry(QtCore.QRect(510, 80, 151, 41))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.stopButton = QtGui.QPushButton(self.groupBox)
        self.stopButton.setGeometry(QtCore.QRect(510, 130, 151, 41))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.browseUrl = QtGui.QPushButton(self.groupBox)
        self.browseUrl.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.browseUrl.setObjectName(_fromUtf8("browseUrl"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 81, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.type_combo = QtGui.QComboBox(self.groupBox)
        self.type_combo.setGeometry(QtCore.QRect(110, 80, 161, 31))
        self.type_combo.setObjectName(_fromUtf8("type_combo"))
        self.type_combo.addItem(_fromUtf8(""))
        self.type_combo.addItem(_fromUtf8(""))
        self.type_combo.addItem(_fromUtf8(""))
        self.type_combo.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(290, 90, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.pageNum_combo = QtGui.QComboBox(self.groupBox)
        self.pageNum_combo.setGeometry(QtCore.QRect(380, 80, 111, 31))
        self.pageNum_combo.setObjectName(_fromUtf8("pageNum_combo"))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.pageNum_combo.addItem(_fromUtf8(""))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(190, 140, 81, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(350, 140, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.saveImg_combo = QtGui.QComboBox(self.groupBox)
        self.saveImg_combo.setGeometry(QtCore.QRect(110, 130, 69, 31))
        self.saveImg_combo.setObjectName(_fromUtf8("saveImg_combo"))
        self.saveImg_combo.addItem(_fromUtf8(""))
        self.saveImg_combo.addItem(_fromUtf8(""))
        self.dely_combo = QtGui.QComboBox(self.groupBox)
        self.dely_combo.setGeometry(QtCore.QRect(270, 130, 69, 31))
        self.dely_combo.setObjectName(_fromUtf8("dely_combo"))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.dely_combo.addItem(_fromUtf8(""))
        self.partlyNum_combo = QtGui.QComboBox(self.groupBox)
        self.partlyNum_combo.setGeometry(QtCore.QRect(430, 131, 69, 31))
        self.partlyNum_combo.setObjectName(_fromUtf8("partlyNum_combo"))
        self.partlyNum_combo.addItem(_fromUtf8(""))
        self.partlyNum_combo.addItem(_fromUtf8(""))
        self.partlyNum_combo.addItem(_fromUtf8(""))
        self.partlyNum_combo.addItem(_fromUtf8(""))
        self.partlyNum_combo.addItem(_fromUtf8(""))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 440, 681, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.groupBox_2)
        self.lcdNumber.setGeometry(QtCore.QRect(520, 50, 131, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(530, 10, 121, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.logLabel = QtGui.QLabel(self.groupBox_2)
        self.logLabel.setGeometry(QtCore.QRect(30, 40, 481, 61))
        self.logLabel.setStyleSheet(_fromUtf8("background-color:rgb(216, 255, 221)"))
        self.logLabel.setWordWrap(True)
        self.logLabel.setObjectName(_fromUtf8("logLabel"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 681, 191))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.webView = QtWebKit.QWebView(self.groupBox_4)
        self.webView.setGeometry(QtCore.QRect(10, 20, 661, 161))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("http://check.waitig.com/ads/spider.html")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 200, 681, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.sina_radio = QtGui.QRadioButton(self.groupBox_3)
        self.sina_radio.setGeometry(QtCore.QRect(180, 20, 89, 21))
        self.sina_radio.setChecked(True)
        self.sina_radio.setObjectName(_fromUtf8("sina_radio"))
        self.cnblogs_radio = QtGui.QRadioButton(self.groupBox_3)
        self.cnblogs_radio.setGeometry(QtCore.QRect(270, 20, 89, 21))
        self.cnblogs_radio.setObjectName(_fromUtf8("cnblogs_radio"))
        self.csdn_radio = QtGui.QRadioButton(self.groupBox_3)
        self.csdn_radio.setGeometry(QtCore.QRect(370, 20, 89, 21))
        self.csdn_radio.setObjectName(_fromUtf8("csdn_radio"))
        self.cto_radio = QtGui.QRadioButton(self.groupBox_3)
        self.cto_radio.setGeometry(QtCore.QRect(450, 20, 89, 21))
        self.cto_radio.setObjectName(_fromUtf8("cto_radio"))
        self.seg_radio = QtGui.QRadioButton(self.groupBox_3)
        self.seg_radio.setGeometry(QtCore.QRect(540, 20, 121, 20))
        self.seg_radio.setObjectName(_fromUtf8("seg_radio"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 21))
        self.label.setObjectName(_fromUtf8("label"))
        #       MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "spider博客采集器", None))
        self.groupBox.setTitle(_translate("MainWindow", "控制区", None))
        self.label_2.setText(_translate("MainWindow", "需采集的链接：", None))
        self.label_3.setText(_translate("MainWindow", "chm文件储存地址：", None))
        self.browseChm.setText(_translate("MainWindow", "浏览", None))
        self.startButton.setText(_translate("MainWindow", "开始处理", None))
        self.stopButton.setText(_translate("MainWindow", "停止处理", None))
        self.browseUrl.setText(_translate("MainWindow", "预览", None))
        self.label_4.setText(_translate("MainWindow", "选择采集模式：", None))
        self.type_combo.setItemText(0, _translate("MainWindow", "网站博客主页", None))
        self.type_combo.setItemText(1, _translate("MainWindow", "个人博客主页", None))
        self.type_combo.setItemText(2, _translate("MainWindow", "博文页面", None))
        self.type_combo.setItemText(3, _translate("MainWindow", "其他页面", None))
        self.label_8.setText(_translate("MainWindow", "最大采集页数：", None))
        self.pageNum_combo.setItemText(0, _translate("MainWindow", "1页", None))
        self.pageNum_combo.setItemText(1, _translate("MainWindow", "2页", None))
        self.pageNum_combo.setItemText(2, _translate("MainWindow", "3页", None))
        self.pageNum_combo.setItemText(3, _translate("MainWindow", "4页", None))
        self.pageNum_combo.setItemText(4, _translate("MainWindow", "5页", None))
        self.pageNum_combo.setItemText(5, _translate("MainWindow", "6页", None))
        self.pageNum_combo.setItemText(6, _translate("MainWindow", "无限制", None))
        self.label_10.setText(_translate("MainWindow", "是否保存图片：", None))
        self.label_11.setText(_translate("MainWindow", "采集间隔(秒)：", None))
        self.label_12.setText(_translate("MainWindow", "CHM文章个数：", None))
        self.saveImg_combo.setItemText(0, _translate("MainWindow", "不保存", None))
        self.saveImg_combo.setItemText(1, _translate("MainWindow", "保存", None))
        self.dely_combo.setItemText(0, _translate("MainWindow", "0.5秒", None))
        self.dely_combo.setItemText(1, _translate("MainWindow", "1秒", None))
        self.dely_combo.setItemText(2, _translate("MainWindow", "2秒", None))
        self.dely_combo.setItemText(3, _translate("MainWindow", "3秒", None))
        self.dely_combo.setItemText(4, _translate("MainWindow", "4秒", None))
        self.dely_combo.setItemText(5, _translate("MainWindow", "5秒", None))
        self.dely_combo.setItemText(6, _translate("MainWindow", "无限制", None))
        self.partlyNum_combo.setItemText(0, _translate("MainWindow", "10篇", None))
        self.partlyNum_combo.setItemText(1, _translate("MainWindow", "20篇", None))
        self.partlyNum_combo.setItemText(2, _translate("MainWindow", "30篇", None))
        self.partlyNum_combo.setItemText(3, _translate("MainWindow", "40篇", None))
        self.partlyNum_combo.setItemText(4, _translate("MainWindow", "50篇", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "显示区", None))
        self.label_5.setText(_translate("MainWindow", "采集日志", None))
        self.label_6.setText(_translate("MainWindow", "共发现博文数量", None))
        self.logLabel.setText(_translate("MainWindow", "欢迎使用【Spider】博客采集系统！系统初始化成功！", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "预览区", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "功能区", None))
        self.sina_radio.setText(_translate("MainWindow", "新浪博客", None))
        self.cnblogs_radio.setText(_translate("MainWindow", "cnblogs博客", None))
        self.csdn_radio.setText(_translate("MainWindow", "csdn博客", None))
        self.cto_radio.setText(_translate("MainWindow", "51CTO博客", None))
        self.seg_radio.setText(_translate("MainWindow", "segmentfault博客", None))
        self.label.setText(_translate("MainWindow", "请选择博客类型：", None))


from PyQt4 import QtWebKit

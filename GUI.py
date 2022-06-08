# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap

from custom_widget import myVideoSlider, myVideoWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        palette = QPalette()
        # palette.setBrush(QPalette.Background, QBrush(QPixmap("texture.jpg")))
        color = QColor(230, 255, 255)
        palette.setBrush(QPalette.Background, color)
        MainWindow.setPalette(palette)
        MainWindow.setObjectName("Cinnamoroll")
        MainWindow.resize(1469, 1242)
        self.setWindowIcon(QtGui.QIcon('assets/cinna.jpeg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # record_start button
        self.btn_record_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record_start.setMaximumSize(QtCore.QSize(150, 25))
        self.btn_record_start.setObjectName("btn_record_start")
        self.gridLayout.addWidget(self.btn_record_start, 20, 1, 1, 1)
        # record_end long button
        self.btn_record_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record_end.setMaximumSize(QtCore.QSize(150, 25))
        self.btn_record_end.setObjectName("btn_record_end")
        self.gridLayout.addWidget(self.btn_record_end, 20, 2, 1, 1)
        # record_end short button
        self.btn_record_mid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_record_mid.setMaximumSize(QtCore.QSize(150, 25))
        self.btn_record_mid.setObjectName("btn_record_mid")
        self.gridLayout.addWidget(self.btn_record_mid, 20, 3, 1, 1)
        # save button
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setMaximumSize(QtCore.QSize(150, 25))
        self.gridLayout.addWidget(self.btn_save, 20, 4, 1, 1)
        # clear button
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.setMaximumSize(QtCore.QSize(150, 25))
        self.gridLayout.addWidget(self.btn_clear, 20, 5, 1, 1)

        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.gridLayout.addLayout(self.horizontalLayout_1, 6, 1, 5, 5)

        # 垂直布局1
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.txt_name = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_name.setObjectName("txt_name")
        self.verticalLayout_1.addWidget(self.txt_name)
        self.txt_name.setPlaceholderText("Your name")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        items = ["People&Blogs", "Gaming", "Sports", "Movie", "Travel", "TvShows", "Education", "Animals&Pets",
                 "Science&Technology", "Family", "Food&Drink", "Vehicles&Autos", "Advertisement", "Documentary"]
        self.comboBox.addItems(items)
        self.verticalLayout_1.addWidget(self.comboBox)
        self.txt_start = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_start.setObjectName("txt_start")
        self.verticalLayout_1.addWidget(self.txt_start)
        self.txt_start.setPlaceholderText("start")
        self.txt_end = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_end.setObjectName("txt_end")
        self.verticalLayout_1.addWidget(self.txt_end)
        self.txt_end.setPlaceholderText("end")
        self.txt_mid = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_mid.setObjectName("txt_mid")
        self.verticalLayout_1.addWidget(self.txt_mid)
        self.txt_mid.setPlaceholderText("mid")
        self.txt_caption_en = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_caption_en.setObjectName("txt_caption_en")
        self.verticalLayout_1.addWidget(self.txt_caption_en)
        self.txt_caption_en.setPlaceholderText("caption_en")
        self.txt_caption_ch = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_caption_ch.setObjectName("txt_caption_ch")
        self.verticalLayout_1.addWidget(self.txt_caption_ch)
        self.txt_caption_ch.setPlaceholderText("caption_ch")
        self.txt_prompt_en = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_prompt_en.setObjectName("txt_prompt_en")
        self.verticalLayout_1.addWidget(self.txt_prompt_en)
        self.txt_prompt_en.setPlaceholderText("prompt_en")
        self.txt_prompt_ch = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_prompt_ch.setObjectName("txt_prompt_ch")
        self.verticalLayout_1.addWidget(self.txt_prompt_ch)
        self.txt_prompt_ch.setPlaceholderText("prompt_ch")
        self.txt_gt_en = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_gt_en.setObjectName("txt_gt_en")
        self.verticalLayout_1.addWidget(self.txt_gt_en)
        self.txt_gt_en.setPlaceholderText("gt_en")
        self.txt_gt_ch = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_gt_ch.setObjectName("txt_gt_ch")
        self.verticalLayout_1.addWidget(self.txt_gt_ch)
        self.txt_gt_ch.setPlaceholderText("gt_ch")

        # 垂直布局2
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setMinimumSize(QtCore.QSize(410, 200))
        self.wgt_video.setMaximumSize(QtCore.QSize(10000, 10000))
        palette = QtGui.QPalette()#调色板
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(True)
        self.wgt_video.setObjectName("wgt_video")
        self.verticalLayout_2.addWidget(self.wgt_video)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        #video open button
        self.btn_open = QtWidgets.QPushButton(self.splitter)
        self.btn_open.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_open.setObjectName("btn_open")
        #video play button
        self.btn_play = QtWidgets.QPushButton(self.splitter)
        self.btn_play.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_play.setObjectName("btn_play")
        #audio slider
        self.sld_audio = QtWidgets.QSlider(self.splitter)
        self.sld_audio.setMinimumSize(QtCore.QSize(100, 0))
        self.sld_audio.setMaximumSize(QtCore.QSize(150, 20))
        self.sld_audio.setProperty("value", 100)
        self.sld_audio.setOrientation(QtCore.Qt.Horizontal)
        self.sld_audio.setObjectName("sld_audio")
        #audio label
        self.lab_audio = QtWidgets.QLabel(self.splitter)
        self.lab_audio.setObjectName("lab_audio")
        #cast button
        # self.btn_cast = QtWidgets.QPushButton(self.splitter)
        # self.btn_cast.setObjectName("btn_cast")
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        #video slider
        self.sld_video = myVideoSlider(self.centralwidget)
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.verticalLayout_2.addWidget(self.sld_video)
        #video label
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lab_video.setObjectName("lab_video")
        self.verticalLayout_2.addWidget(self.lab_video)

        self.horizontalLayout_1.addLayout(self.verticalLayout_2)
        self.horizontalLayout_1.addLayout(self.verticalLayout_1)
        self.horizontalLayout_1.setStretch(0, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 1469, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Cinnamoroll", "Cinnamoroll"))
        self.btn_record_start.setText(_translate("Cinnamoroll", "RecordStart"))
        self.btn_record_end.setText(
            _translate("Cinnamoroll", "RecordEnd"))
        self.btn_record_mid.setText(
            _translate("Cinnamoroll", "RecordMid"))
        self.btn_save.setText(_translate("Cinnamoroll", "Save"))
        self.btn_clear.setText(_translate("Cinnamoroll", "Clear"))
        self.lab_video.setText(_translate("Cinnamoroll", "0%"))
        self.btn_open.setText(_translate("Cinnamoroll", "Open"))
        self.btn_play.setText(_translate("Cinnamoroll", "Play/Pause"))
        self.lab_audio.setText(_translate("Cinnamoroll", "volume:100%"))
        # self.btn_cast.setText(_translate("Cinnamoroll", "ScreenShot"))

import datetime
import json
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *

from custom_widget import myVideoWidget
from cut_video import SOURCE_DIR_JSON
from GUI import Ui_MainWindow
from tools import Logger, contains_chinese

SOURCE_DIR_JSON = "data/jsons"
SOURCE_DIR_VID = "data/videos"


class myMainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        # 添加退出按钮
        fileMenu = self.menubar.addMenu("文件")
        exitButton = QAction('Exit', self)
        exitButton.setSeparator(0)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('退出当前应用')
        fileMenu.addAction(exitButton)
        exitButton.triggered.connect(qApp.quit)

        self.sld_video_pressed = False  # 判断当前进度条识别否被鼠标点击
        self.videoFullScreen = False   # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()   # 创建一个全屏的widget
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的
        self.btn_open.clicked.connect(self.openVideoFile)   # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playOrPause)       # play or pause
        # self.btn_cast.clicked.connect(self.castVideo)        # 视频截图
        self.player.positionChanged.connect(
            self.changeSlide)      # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(
            self.videoDoubleClicked)  # 双击全屏
        self.wgt_video.doubleClickedItem.connect(
            self.videoDoubleClicked)  # 双击全屏
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)  # 释放进度条
        self.sld_video.sliderPressed.connect(self.pressSlider)  # 按住进度条
        self.sld_video.sliderMoved.connect(self.moveSlider)   # 进度条拖拽跳转
        self.sld_video.ClickedValue.connect(self.clickedSlider)  # 进度条点击跳转
        self.sld_audio.valueChanged.connect(self.volumeChange)  # 控制声音播放
        self.btn_save.clicked.connect(self.saveJson)  # 保存为json文件
        self.btn_clear.clicked.connect(self.clearAllText)  # 清除所有文本框内容
        self.btn_record_start.clicked.connect(lambda: self.record(0))  # 记录时间点
        self.btn_record_end.clicked.connect(lambda: self.record(1))
        self.btn_record_mid.clicked.connect(lambda: self.record(2))

        self.location = 0
        self.play = True
        self.filename = ""
        self.logger = Logger()

    def castVideo(self):
        '''
        截图
        '''
        screen = QGuiApplication.primaryScreen()
        cast_jpg = './'+QDateTime.currentDateTime().toString("yyyy-MM-dd hh-mm-ss-zzz")+'.jpg'
        screen.grabWindow(self.wgt_video.winId()).save(cast_jpg)

    def volumeChange(self, position):
        '''
        调节声音
        '''
        volume = round(position/self.sld_audio.maximum()*100)
        self.player.setVolume(volume)
        self.lab_audio.setText("volume:"+str(volume)+"%")

    def clickedSlider(self, position):
        '''
        点击slider控制视频进度
        '''
        self.logger.debug("click,location:%d,duration:%d" %
                          (self.location, self.player.duration()))
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.1fs" % (
                (position/1000)))
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        '''
        滑动slider调节视频进度
        '''
        self.logger.warning("move,location:%d,duration:%d" %
                            (self.location, self.player.duration()))
        self.sld_video_pressed = True
        self.location = position
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.1fs" % (
                (position/1000)))

    def pressSlider(self):
        self.sld_video_pressed = True

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        '''
        视频播放
        '''
        self.location = position
        self.logger.info("change,location:%d,duration:%d" %
                         (self.location, self.player.duration()))
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            self.sld_video.setValue(
                round((position/(self.player.duration()+0.1))*100))
            self.lab_video.setText("%.1fs" % (
                (position/1000)))

    def openVideoFile(self):
        '''
        打开目录，选取视频文件
        '''
        url = QFileDialog.getOpenFileUrl()[0]
        filename = url.toString().split("/")[-1]
        self.filename = filename
        self.player.setMedia(QMediaContent(url))  # 选取视频文件
        self.player.play()  # 播放视频

        # print(self.player.availableMetaData())

    def playOrPause(self):
        '''
        播放和暂停
        '''
        if(self.play):
            self.play = False
            self.player.pause()
        else:
            self.play = True
            self.player.play()

    def videoDoubleClicked(self, text):
        '''
        双击全屏播放
        '''
        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.setVideoOutput(self.wgt_video)
                self.videoFullScreenWidget.hide()
                self.videoFullScreen = False
            else:
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.videoFullScreenWidget.setFullScreen(1)
                self.videoFullScreen = True

    def saveJson(self):
        '''
        获取所有文本框内容，并保存为xml文档
        '''
        author_name = self.txt_name.text()
        category = self.comboBox.currentText()
        start = self.txt_start.text()
        end = self.txt_end.text()
        mid = self.txt_mid.text()
        caption_en = self.txt_caption_en.toPlainText()
        caption_ch = self.txt_caption_ch.toPlainText()
        prompt_en = self.txt_prompt_en.toPlainText()
        prompt_ch = self.txt_prompt_ch.toPlainText()
        gt_en = self.txt_gt_en.toPlainText()
        gt_ch = self.txt_gt_ch.toPlainText()

        flag = author_name and category and start and end and mid and caption_ch and caption_en and prompt_ch and prompt_en and gt_en and gt_ch
        if(not flag):
            choice = QMessageBox.warning(
                self, "Warning", "有空字段，请检查文本框内容", QMessageBox.Yes | QMessageBox.No)
            self.logger.warning("有空字段,请检查文本框内容")
            return

        if(not(caption_ch and caption_ch and prompt_ch and prompt_en and gt_en and gt_ch)):
            choice = QMessageBox.warning(
                self, "Warning", "文本不能为空，请检查文本框内容", QMessageBox.Yes | QMessageBox.No)
            self.logger.warning("文本不能为空,请检查文本框内容")
            return

        if(contains_chinese(caption_en) or contains_chinese(prompt_en) or contains_chinese(gt_en)):
            choice = QMessageBox.warning(
                self, "Warning", "caption_en|prompt_en|gt_en不该含有中文字符,请检查文本框内容", QMessageBox.Yes | QMessageBox.No)
            self.logger.warning("caption_en|prompt_en|gt_en不该含有中文字符,请检查文本框内容")
            return

        if(not (contains_chinese(caption_ch) and contains_chinese(prompt_ch) and contains_chinese(gt_ch))):
            choice = QMessageBox.warning(
                self, "Warning", "caption_ch|prompt_ch|gt_ch不含有中文字符,请检查文本框内容", QMessageBox.Yes | QMessageBox.No)
            self.logger.warning("caption_ch|prompt_ch|gt_ch不含有中文字符,请检查文本框内容")
            return

        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d-%H-%M-%S")
        url = "https://www.youtube.com/watch?v="+self.filename
        results = {"author": author_name, "url": url, "filename": self.filename, "time": time, "content": {"category": category, "start": start, "end": end, "mid": mid, "caption_en": caption_en, "caption_ch": caption_ch, "prompt_en": prompt_en,
                                                                                                           "prompt_ch": prompt_ch, "gt_en": gt_en, "gt_ch": gt_ch}}
        self.logger.info(results)

        js = json.dumps(results, ensure_ascii=False)
        with open(os.path.join(SOURCE_DIR_JSON, self.filename+"-"+time+".json"), "w", encoding="utf8") as f:
            f.write(js)

    def clearAllText(self):
        '''
        清除所有文本框内容
        '''
        self.logger.info("clear all textbox content")
        self.txt_start.clear()
        self.txt_end.clear()
        self.txt_mid.clear()
        self.txt_caption_en.clear()
        self.txt_caption_ch.clear()
        self.txt_prompt_en.clear()
        self.txt_prompt_ch.clear()
        self.txt_gt_en.clear()
        self.txt_gt_ch.clear()

    def record(self, type):
        '''
        type=0:记录开始时间点
        type=1:记录整段视频结束时间点
        type=2:记录前半段视频结束时间点
        '''
        if type == 0:
            if(self.play == False):  # 必须是视频暂停状态下才能记录
                self.txt_start.setText("%d" % self.location)
        elif type == 1:
            if(self.play == False):  # 必须是视频暂停状态下才能记录
                self.txt_end.setText("%d" % self.location)
        elif type == 2:
            if(self.play == False):  # 必须是视频暂停状态下才能记录
                self.txt_mid.setText("%d" % self.location)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vieo_gui = myMainWindow()
    vieo_gui.show()
    sys.exit(app.exec_())

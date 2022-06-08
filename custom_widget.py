from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QSlider


class myVideoSlider(QSlider):
    ClickedValue = pyqtSignal(int)

    def __init__(self, father):
        super().__init__(Qt.Horizontal, father)
        self.setMinimum(0)
        self.setMaximum(1000)
        # 步长
        self.setSingleStep(1)
        self.setTickInterval(5)

    def mousePressEvent(self, QMouseEvent):  # 单击事件
        super().mousePressEvent(QMouseEvent)
        value = QMouseEvent.localPos().x()
        # self.setValue(int(value)/9)
        # 根据鼠标点击的位置和slider的长度算出百分比
        value = round(value/self.width()*self.maximum())
        self.ClickedValue.emit(value)


class myVideoWidget(QVideoWidget):
    doubleClickedItem = pyqtSignal(str)  # 创建双击信号

    def __init__(self, parent=None):
        super(QVideoWidget, self).__init__(parent)

    def mouseDoubleClickEvent(self, QMouseEvent):  # 双击事件
        self.doubleClickedItem.emit("double clicked")

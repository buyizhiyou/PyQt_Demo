from PyQt5.QtCore import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QSlider


class myVideoSlider(QSlider):
    ClickedValue = pyqtSignal(int)

    def __init__(self, father):
        super().__init__(Qt.Horizontal, father)
        self.setMinimum(0)
        self.setMaximum(100000)
        # 步长
        self.setSingleStep(1)
        self.setTickInterval(1)
        self.pos = 0

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

class DoubleSlider(QSlider):
    ClickedValue = pyqtSignal(float)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.decimals = 5
        self._max_int = 10 ** self.decimals#100000

        super().setMinimum(0)
        super().setMaximum(self._max_int)

        self._min_value = 0.0
        self._max_value = 100000

    @property
    def _value_range(self):
        return self._max_value - self._min_value

    def value(self):
        return float(super().value()) / self._max_int * self._value_range + self._min_value

    def setValue(self, value):
        super().setValue(int((value - self._min_value) / self._value_range * self._max_int))

    def setMinimum(self, value):
        if value > self._max_value:
            raise ValueError("Minimum limit cannot be higher than maximum")

        self._min_value = value
        self.setValue(self.value())

    def setMaximum(self, value):
        if value < self._min_value:
            raise ValueError("Minimum limit cannot be higher than maximum")

        self._max_value = value
        self.setValue(self.value())

    def minimum(self):
        return self._min_value

    def maximum(self):
        return self._max_value


    def mousePressEvent(self, QMouseEvent):  # 单击事件
        super().mousePressEvent(QMouseEvent)
        value = QMouseEvent.localPos().x()
        # self.setValue(int(value)/9)
        # 根据鼠标点击的位置和slider的长度算出百分比
        value = round(value/self.width()*self.maximum())
        self.ClickedValue.emit(value)
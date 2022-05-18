import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import random
import sys
import subprocess

class datedialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.repaint()
        palette =QPalette()
        pix =QPixmap('images/dialog.jpeg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        _font=QFont()
        _font.setFamily('YouYuan')
        _font.setPixelSize(40)
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.resize(400, 150)
        self.label.setText('大威天龙')
        self.label.setFont(_font)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

    def setPosition(self,x,y):
        self.move(x-400,y+50)




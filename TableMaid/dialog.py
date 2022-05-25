import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import random
import sys
import subprocess

class datedialog(QWidget):
    def __init__(self,x,y):
        super().__init__()
        self.resize(400,150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Widget | Qt.SubWindow)
        self.repaint()
        self.move(x - 400, y + 50)
        palette =QPalette()
        pix =QPixmap('images/dialog.jpeg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background,QBrush(pix))
        _font=QFont()
        _font.setFamily('YouYuan')
        _font.setPixelSize(25)
        self.setPalette(palette)
        self.label = QLabel(self)
        self.label.move(10,10)
        self.label.resize(390, 140)

        self.label.setWordWrap(True)
        #self.label.setStyleSheet("qproperty-alignment: AlignTop;")
        self.label.setAlignment(Qt.AlignTop)
        self.label.setText('阿富汗几点回家咖啡哈哈就开始放寒假')
        self.label.setFont(_font)


    def setPosition(self,x,y):
        self.move(x-400,y+50)




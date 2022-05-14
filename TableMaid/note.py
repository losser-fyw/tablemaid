import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import random
import sys
import subprocess

class Note(QWidget):
    def __init__(self):
        super().__init__()
        self.is_follow_mouse =False
        self.number=0

        self.resize(400,150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.repaint()

        # 鼠标左键按下时, 宠物将和鼠标位置绑定'

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    # 鼠标移动, 则宠物也移动
    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
        event.accept()
    # 鼠标释放时, 取消绑定
    def mouseReleaseEvent(self, event):
        if self.is_follow_mouse == True:
            self.is_follow_mouse = False
            self.setCursor(QCursor(Qt.ArrowCursor))
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Note()
    win.show()
    sys.exit(app.exec_())

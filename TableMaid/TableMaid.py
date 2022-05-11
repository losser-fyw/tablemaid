from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import random
import sys
import subprocess
from dialog import datedialog

class tablemaid(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.setMenu)
        self.repaint()
        # 变量
        self.is_follow_mouse = False
        self.startpos = self.pos()

        self.child = datedialog()
        self.setUI()

        #计时器
        self.timer=QTimer()
        self.timer.timeout.connect(self.child.close)
        self.timer.start(3000)


    def setUI(self):
        self.label = QLabel(self)
        self.label.resize(200, 200)
        self.label.setPixmap(QPixmap('images/2.jpg'))
        self.label.setScaledContents(True)
        #右击菜单

    def setMenu(self,event):
        cmenu = QMenu(self)
        #Quit = QAction('退出')
        note=cmenu.addAction("便签")
        cmenu.addSeparator()
        setting=cmenu.addAction("设置")
        help=cmenu.addAction("反馈求助")
        cmenu.addSeparator()
        Quit=cmenu.addAction("退出")
        Quit.triggered.connect(self.close)
        Quit.triggered.connect(self.child.close)
        mini=cmenu.addAction('最小化')



        cmenu.exec_(QCursor.pos())



    #鼠标左键按下时, 宠物将和鼠标位置绑定'
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            self.is_follow_mouse = True
            self.startpos = self.pos()
            self.timer.stop()
            self.timer.start(3000)
            self.mouse_drag_pos = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))


    #鼠标移动, 则宠物也移动

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            self.child.setPosition(self.x(), self.y())
            self.timer.start(3000)
            event.accept()

    #鼠标释放时, 取消绑定

    def mouseReleaseEvent(self, event):

        if self.is_follow_mouse==True:
            self.is_follow_mouse = False
            if self.pos()==self.startpos:
                self.child.setPosition(self.x(),self.y())
                self.child.show()

            self.setCursor(QCursor(Qt.ArrowCursor))

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=tablemaid()
    win.show()
    sys.exit(app.exec_())
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import random
import sys
import subprocess
import pymongo
from dialog import datedialog
from note import Note
from alarm import clock_alert

class tablemaid(QMainWindow):
    def __init__(self):
        super().__init__()
        #os.system('alarm.py')
        #print(setting.mydb.list_collection_names())
        # 变量区

        self.is_follow_mouse = False
        self.startpos = self.pos()
        self.petList = ['1', '2', '3']
        self.max_length = len(self.petList)
        self.child = datedialog(self.x(),self.y())

        self.alarm=clock_alert()

        self.note=Note()
        # 计时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.child.close)
        self.timer.start(3000)


        self.timer_image = QTimer()
        self.timer_image.timeout.connect(self.presentation)
        self.timer_image.start(1000)
        self.alarm_timer=QTimer()
        self.alarm_timer.timeout.connect(self.alarm_dialog)
        self.alarm_timer.start(100)

        #设置主窗口
        self.resize(200,200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Widget | Qt.SubWindow)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.customContextMenuRequested.connect(self.setMenu)
        self.repaint()
        self.setUI()




    def setUI(self):
        self.label = QLabel(self)
        self.label.resize(200, 200)
        self.label.setPixmap(QPixmap('images/2.jpg'))
        self.label.setScaledContents(True)
        self.petNum = 0
        self.presentation()

    def presentation(self):
        if(self.petNum==self.max_length):
            self.petNum=0
        self.petImage = QPixmap('./images/' + self.petList[1] + '.jpg')
        self.label.setPixmap(self.petImage)
        self.petNum += 1
        self.label.update()

    def setMenu(self,event):
        cmenu = QMenu(self)
        alarm = cmenu.addAction("闹钟")
        alarm.triggered.connect(self.alarm.show)
        note=cmenu.addAction("便签")
        note.triggered.connect(self.note.show)

        cmenu.addSeparator()
        setting=cmenu.addAction("设置")
        help=cmenu.addAction("反馈求助")
        cmenu.addSeparator()
        Quit=cmenu.addAction("退出")
        Quit.triggered.connect(app.quit)
        mini=cmenu.addAction('最小化')
        cmenu.exec_(QCursor.pos())
    def alarm_dialog(self):
        if self.alarm.monitor2():
            str=self.alarm.monitor2()
            self.child.label.setText(str)
            self.child.show()




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
        jud_x1 = self.x()
        if   Qt.LeftButton and self.is_follow_mouse:
            self.move(event.globalPos() - self.mouse_drag_pos)
            self.child.move(event.globalPos() - self.mouse_drag_pos)

            jud_x2 = self.x()
            if (jud_x1 > jud_x2):
                self.label.setPixmap(QPixmap('./images/5.png'))
                self.child.close()
            if (jud_x2 > jud_x1):
                self.label.setPixmap(QPixmap('./images/4.png'))
                self.child.close()
        self.timer_image.stop()
        self.timer_image.start(300)
        event.accept()
    #鼠标释放时, 取消绑定
    def mouseReleaseEvent(self, event):
        if self.is_follow_mouse==True:
            self.is_follow_mouse = False
            if self.pos()==self.startpos:
                self.child.setPosition(self.x(),self.y())
                self.child.show()
                self.timer.start(3000)

            self.setCursor(QCursor(Qt.ArrowCursor))

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=tablemaid()
    win.show()
    sys.exit(app.exec_())
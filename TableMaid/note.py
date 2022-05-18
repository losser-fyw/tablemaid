import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
class Note(QWidget):
    def __init__(self):
        super().__init__()
        #变量区
        self.number=1
        self.is_follow_mouse =False
        self.child=add_Note()
        self.resize(400,600)
        self.setWindowTitle("便签")
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setUI()
        
    def setUI(self):
        self.add = QPushButton("新建便签", self)
        self.add.resize(400, 50)
        self.add.clicked.connect(self.child.show)
        self.child.button1.clicked.connect(self.addNote)
        #self.add.clicked.connect(self.addNote)
    def addNote(self):

        widget1=QFrame(self)
        widget1.setFrameShape(QFrame.Box)

        widget1.move(0,51*self.number)
        widget1.resize(400,50)
        layout1=QGridLayout()

        label_month_num=QLabel(self.child.edit_month.text(),widget1)

        label_month=QLabel("月",widget1)
        layout1.addWidget(label_month_num,0,0,1,1)
        layout1.addWidget(label_month,0,1,1,1)
        widget1.setLayout(layout1)

        widget1.show()
        self.number+=1
        self.update()

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


class add_Note(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("添加便签事项")
        layout=QGridLayout()
        #月
        self.edit_month=QLineEdit(self)
        self.edit_month.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.label_month = QLabel("月", self)
        layout.addWidget(self.edit_month, 0, 0, 1, 1)
        layout.addWidget(self.label_month, 0, 1, 1, 1)
        #日
        self.edit_day = QLineEdit(self)
        self.edit_day.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_day = QLabel("日", self)
        layout.addWidget(self.edit_day, 0, 2, 1, 1)
        layout.addWidget(self.label_day, 0, 3, 1, 1)
        #时
        self.edit_hour = QLineEdit(self)
        self.edit_hour.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_hour = QLabel("时", self)
        layout.addWidget(self.edit_hour, 1, 0, 1, 1)
        layout.addWidget(self.label_hour, 1, 1, 1, 1)
        #分
        self.edit_minute = QLineEdit(self)
        self.edit_minute.setContextMenuPolicy(Qt.PreventContextMenu)
        self.label_minute = QLabel("分", self)
        layout.addWidget(self.edit_minute, 1, 2, 1, 1)
        layout.addWidget(self.label_minute, 1, 3, 1, 1)
        #事项
        self.label_matter=QLabel("事项",self)
        self.edit_matter=QTextEdit(self)
        self.edit_matter.setContextMenuPolicy(Qt.PreventContextMenu)
        layout.addWidget(self.label_matter,2,0,1,1)
        layout.addWidget(self.edit_matter,3,0,1,4)
        self.button1 = QPushButton("确认", self)
        #self.button1.clicked.connect(self.close)

        self.button2=QPushButton("取消",self)
        self.button2.clicked.connect(self.close)
        layout.addWidget(self.button1,4,0,1,1)
        layout.addWidget(self.button2, 4, 2, 1, 1)
        self.setLayout(layout)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Note()
    win.show()
    sys.exit(app.exec_())

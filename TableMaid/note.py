import time

import pymongo
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatebase"]
mycol = mydb["notes"]
class Note(QWidget):
    def __init__(self):
        super().__init__()
        #变量区
        self.number=1
        self.is_follow_mouse =False
        self.child=add_Note()

        self.resize(400,600)
        self.setMaximumHeight(600)

        self.setWindowTitle("便签")
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setUI()
        #self.show_note()
        
    def setUI(self):
        self.add = QPushButton("新建便签", self)
        self.add.resize(400, 50)
        self.add.setMaximumHeight(50)
        self.add.clicked.connect(self.addNote)
        self.widget=QWidget(self)
        #self.child.button1.clicked.connect(self.addNote)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.add)
        self.vlayout.addWidget(self.widget)

        self.vlayout2=QVBoxLayout()
        self.vlayout2.setAlignment(Qt.AlignTop)
        self.setLayout(self.vlayout)


    def addNote(self):
        block = note_block(self.number)
        self.vlayout2.addWidget(block)
        self.widget.setLayout(self.vlayout2)
        self.number = self.number + 1
        '''
        dict = {}
        dict["_id"] = self.number
        dict["month"] = self.child.edit_month.text()
        dict["day"] = self.child.edit_day.text()
        dict["hour"] = self.child.edit_hour.text()
        dict["minute"] = self.child.edit_minute.text()
        m = mycol.find({"_id": self.number})
        if m != 0:
            for i in m:
                x = mycol.delete_one(i)
            x = mycol.insert_one(dict)
        else:
            x = mycol.insert_one(dict)
        for x in mycol.find():
            print(x)
        self.number =self.number+ 1
        #self.show_note()
        '''
    '''
    def show_note(self):
        self.n=1
        m = mycol.find()
        for i in m:
            print(i)
            widget1 = QFrame(self)
            widget1.setFrameShape(QFrame.Box)
            widget1.move(0, 160 * self.n-1)
            widget1.resize(400, 160)
            layout1 = QVBoxLayout()
            edit=QTextEdit(widget1)
            edit.resize(400,150)
            layout1.addWidget(edit)
            button_time=QPushButton("时间",widget1)
            button_time.resize(20,10)
            layout1.addWidget(button_time)
            button_time.clicked.connect(self.child.show)
            widget1.setLayout(layout1)
            widget1.show()
            self.update()
            self.n=self.n+1
    '''
    #鼠标左键按下时, 宠物将和鼠标位置绑定'
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
        #self.id=1
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

        self.button1 = QPushButton("确认", self)
        self.button1.clicked.connect(self.close)

        self.button2=QPushButton("取消",self)
        self.button2.clicked.connect(self.close)
        layout.addWidget(self.button1,2,0,1,1)
        layout.addWidget(self.button2, 2, 2, 1, 1)
        self.setLayout(layout)

class note_block(QFrame):
    def __init__(self,id):
        super(note_block, self).__init__()
        self.id=id
        self.timeBar=add_Note()
        self.setFrameShape(QFrame.Box)
        self.resize(400, 160)
        self.setMaximumHeight(150)
        layout = QVBoxLayout()
        edit = QTextEdit(self)
        edit.resize(400, 150)
        layout.addWidget(edit)
        button_time = QPushButton("时间", self)
        button_time.resize(20, 10)
        layout.addWidget(button_time)
        button_time.clicked.connect(self.timeBar.show)
        self.setLayout(layout)
    def test(self):
        print(self.id)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Note()
    win.show()
    sys.exit(app.exec_())

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
        self.number = 0
        self.is_follow_mouse =False
        self.child=timeBar()

        self.resize(400,600)
        self.setMaximumHeight(600)

        self.setWindowTitle("便签")
        self.setContextMenuPolicy(Qt.PreventContextMenu)
        self.setUI()
        self.show_note()

        
    def setUI(self):
        self.add = QPushButton("新建便签", self)
        self.add.resize(400, 50)
        self.add.setMaximumHeight(50)
        self.add.clicked.connect(self.addNote)
        # self.setCentralWidget(self.widget)
        # self.child.button1.clicked.connect(self.addNote)

        self.topFiller = QWidget(self)
        self.topFiller.setMinimumSize(350, self.number * 150)
        self.scroll = QScrollArea(self)
        self.scroll.setWidget(self.topFiller)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.add)
        self.vlayout.addWidget(self.scroll)
        self.vlayout2 = QVBoxLayout()
        self.vlayout2.setAlignment(Qt.AlignTop)
        self.setLayout(self.vlayout)

    def show_note(self):
        m = mycol.find()
        for i in m:
            self.number=i["_id"]
            block = note_block(self.number)
            self.vlayout2.addWidget(block)
            self.topFiller.setLayout(self.vlayout2)
            self.topFiller.setMinimumSize(350, self.number * 150)

    def addNote(self):
        self.number = self.number + 1
        block = note_block(self.number)
        self.vlayout2.addWidget(block)
        self.topFiller.setLayout(self.vlayout2)
        self.topFiller.setMinimumSize(350, self.number * 150)


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


class timeBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("设置时间")
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
        self.id = id
        self.timeBar=timeBar()
        self.setFrameShape(QFrame.Box)
        self.resize(400, 160)
        self.setMaximumHeight(150)
        layout = QGridLayout()
        self.edit = QTextEdit(self)
        self.edit.resize(400, 150)
        layout.addWidget(self.edit, 0, 0, 1, 3)
        button_time = QPushButton("时间", self)
        button_time.clicked.connect(self.timeBar.show)
        button_time.resize(20, 10)
        layout.addWidget(button_time, 1, 0, 1, 1)
        self.button_delete=QPushButton("删除",self)
        self.button_delete.clicked.connect(self.delete)
        layout.addWidget(self.button_delete,1,1,1,1)
        button_queren = QPushButton("确认", self)
        button_queren.clicked.connect(self.to_datebase)
        button_queren.resize(20, 10)
        layout.addWidget(button_queren, 1, 2, 1, 1)
        self.setLayout(layout)
        m=mycol.find({"_id":self.id})
        for i in m:
            self.edit.setText(i["matter"])
            self.timeBar.edit_month.setText(i["month"])
            self.timeBar.edit_day.setText(i["day"])
            self.timeBar.edit_hour.setText(i["hour"])
            self.timeBar.edit_minute.setText(i["minute"])
    def to_datebase(self):
        dict = {}
        dict["_id"] = self.id
        dict["month"] = self.timeBar.edit_month.text()
        dict["day"] = self.timeBar.edit_day.text()
        dict["hour"] = self.timeBar.edit_hour.text()
        dict["minute"] = self.timeBar.edit_minute.text()
        dict["matter"]=self.edit.toPlainText()
        m = mycol.find({"_id": self.id})
        if m != 0:
            for i in m:
                x = mycol.delete_one(i)
            x = mycol.insert_one(dict)
        else:
            x = mycol.insert_one(dict)
        for x in mycol.find():
            print(x)
        # self.show_note()
    def delete(self):
        self.deleteLater()
        mycol.delete_one({"_id":self.id})




if __name__=="__main__":
    app=QApplication(sys.argv)
    win=Note()
    win.show()
    sys.exit(app.exec_())

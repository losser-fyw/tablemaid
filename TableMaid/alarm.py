import time

import pymongo
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatebase"]
mycol = mydb["notes"]

class clock_alert(QWidget):
    def __init__(self):
        super(clock_alert,self).__init__()
        flag_alert=0
        self.initUI()


    def initUI(self):

        self.setWindowTitle("小闹钟")  # 设置应用标题
        self.setWindowIcon(QIcon('clock.ico'))  # 设置应用图标
        self.resize(400,200)

        self.tray=TrayModel(self)

        form1=QHBoxLayout()
        form2=QHBoxLayout()
        vbox=QVBoxLayout()

        self.exce_flag_clock=0
        self.month=0
        self.day=0
        self.hour=0
        self.minute=0

        self.month_edit=QLineEdit()
        self.day_edit=QLineEdit()
        self.hour_edit=QLineEdit()
        self.minute_edit=QLineEdit()

        self.label_m=QLabel('月')
        self.label_d=QLabel('日')
        self.label_H=QLabel('时')
        self.label_M=QLabel('分')

        self.month_edit.setInputMask('00')
        self.day_edit.setInputMask('00')
        self.hour_edit.setInputMask('00')
        self.minute_edit.setInputMask('00')

        self.btn_ok=QPushButton('确认')

        form1.addWidget(self.month_edit)
        form1.addWidget(self.label_m)
        form1.addWidget(self.day_edit)
        form1.addWidget(self.label_d)
        form1.addWidget(self.hour_edit)
        form1.addWidget(self.label_H)
        form1.addWidget(self.minute_edit)
        form1.addWidget(self.label_M)

        form2.addWidget(self.btn_ok)

        self.monitor_timer=QTimer()

        vbox.addLayout(form1)
        vbox.addLayout(form2)

        self.setLayout(vbox)
        print(self.month_edit.text())

        self.btn_ok.clicked.connect(self.Judge_Exce)
        self.btn_ok.clicked.connect(self.loop)


    def loop(self):
        if (self.exce_flag_clock==0):
            self.monitor_timer.start(100)
            self.monitor_timer.timeout.connect(self.monitor)

        else:
            print('plz check the input value')

        self.exce_flag_clock=0

    def monitor(self):
        self.month=int(time.strftime('%m'))
        self.day=int(time.strftime('%d'))
        self.hour=int(time.strftime('%H'))
        self.minute=int(time.strftime('%M'))
        if ((self.month==int(self.month_edit.text()))&(self.day==int(self.day_edit.text()))&(self.hour==int(self.hour_edit.text()))&(self.minute==int(self.minute_edit.text()))):
            print('付一伟是大帅逼')
        self.update_time()

    def monitor2(self):
        m=mycol.find()
        for i in m:
            self.month=int(time.strftime('%m'))
            self.day=int(time.strftime('%d'))
            self.hour=int(time.strftime('%H'))
            self.minute=int(time.strftime('%M'))
            if ((self.month==int(i["month"]))&(self.day==int(i["day"]))&(self.hour==int(i["hour"]))&(self.minute==int(i["minute"]))):
                print('付一伟是大帅逼')
                return i["matter"]
            else:
                return 0
            self.update_time()

    def update_time(self):
        self.month = int(time.strftime('%m'))
        self.day = int(time.strftime('%d'))
        self.hour = int(time.strftime('%H'))
        self.minute = int(time.strftime('%M'))

    def Judge_Exce(self):
        if int(self.month_edit.text())>12:
            self.exce_flag_clock=1
        if int(self.month_edit.text())==2:
            if int(self.day_edit.text())>29:
                self.exce_flag_clock=1
        if int(self.day_edit.text())>31:
            self.exce_flag_clock=1
        if ((int(self.month_edit.text())==4)|(int(self.month_edit.text())==6)|(int(self.month_edit.text())==9)|(int(self.month_edit.text())==11)):
            if int(self.day_edit.text())>30:
                self.exce_flag_clock=1
        if int(self.hour_edit.text())>23:
            self.exce_flag_clock=1
        if int(self.minute_edit.text())>59:
            self.exce_flag_clock=1

    def closeEvent(self, a0: QCloseEvent) -> None:
        a0.ignore()
        self.hide()
        self.tray.show()

class TrayModel(QSystemTrayIcon):
    def __init__(self, Window):
        super(TrayModel, self).__init__()
        self.window = Window
        self.init_ui()

    def init_ui(self):
        # 初始化菜单
        self.menu = QMenu()

        self.manage_action = QAction('小闹钟设置', self, triggered=self.manage_clock)
        self.quit_action = QAction('退出应用', self, triggered=self.quit_clock)

        self.menu.addAction(self.manage_action)
        self.menu.addAction(self.quit_action)

        self.setContextMenu(self.menu)

        self.setIcon(QIcon('clock.ico'))
        self.icon = self.MessageIcon()

        self.activated.connect(self.app_click)

    def manage_clock(self):
        self.window.showNormal()
        self.window.activateWindow()

    def quit_clock(self):
        qApp.quit()

    def app_click(self, reason):
        pass






if __name__=='__main__':
    app = QApplication(sys.argv)
    main = clock_alert()
    main.show()
    sys.exit(app.exec_())






from winreg import *
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QIcon, QFont, QPixmap
from PyQt6.QtCore import Qt, QCoreApplication
import sys


class MyApp(QMainWindow):
    def addRegistry(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        key = CreateKey(HKEY_LOCAL_MACHINE, sdp_path)
        try:
            SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
            self.statusBar().showMessage("-> Installed WinWD. (Add on Windows Registry.)")
        except EnvironmentError:
            self.envError()

    def check(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, sdp_path, 0, KEY_ALL_ACCESS)
        except OSError:
            return None
        return key

    def de(self):
        key = self.check()
        if key is not None:
            return True
        else:
            return False

    def act(self, i):
        key = self.check()
        if key is not None:
            v = EnumValue(key, 0)
            if v[1] == i:
                return False
            else:
                return True
        if key is None:
            return False

    def writeDisable(self):
        key = self.check()
        if key is None:
            self.statusBar().showMessage("-> You need installed WinWB first. Please select 'Install WexB' and retry.")
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x1)
                self.statusBar().showMessage("-> Write blocking on. (Write is disabled now.)")
            except EnvironmentError:
                self.envError()

    def writeAble(self):
        key = self.check()
        if key is None:
            self.statusBar().showMessage("-> You need installed WinWB first. Please select 'Install WexB' and retry.")
        else:
            try:
                SetValueEx(key, "WriteProtect", 0, REG_DWORD, 0x0)
                self.statusBar().showMessage("-> Write blocking off. (Write is able now.)")
            except EnvironmentError:
                self.envError()

    def deleteRegistry(self):
        sdp_path = r"SYSTEM\CurrentControlSet\Control\StorageDevicePolicies"
        try:
            DeleteKey(HKEY_LOCAL_MACHINE, sdp_path)
            self.statusBar().showMessage("-> Removed WinWB. (Deleted on Windows Registry.)")
        except FileNotFoundError:
            self.statusBar().showMessage("-> You need installed WinWB first. Please select 'Install WexB' and retry.")

    def envError(self):
        self.statusBar().showMessage("-> Encountered Environment Error")

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def dis():
            btn1.setEnabled(self.act(1))
            btn2.setEnabled(self.act(0))
            btn3.setEnabled(not self.de())
            btn4.setEnabled(self.de())

        def on():
            self.writeDisable()
            dis()

        def off():
            self.writeAble()
            dis()

        def re():
            self.addRegistry()
            dis()

        def dele():
            self.deleteRegistry()
            dis()

        # Label
        title = QLabel("WexB", self)
        title.move(40, 50)
        subtitle = QLabel("Windows External-storage Write Blocking Software", self)
        subtitle.move(40, 210)
        subtitle.resize(320, 30)
        # Fonts
        font1 = title.font()
        font1.setPointSize(26)
        title.setFont(font1)
        # Image
        # pixmap = QPixmap("logo.png")
        # lbl_img = QLabel()
        # lbl_img.setPixmap(pixmap)
        # lbl_size = QLabel("Width: 80, Height: 90")
        # lbl_size.setAlignment(Qt.AlignCenter)
        # vbox = QVBoxLayout()
        # vbox.addWidget(lbl_img)
        # vbox.addWidget(lbl_size)
        # self.setLayout(vbox)
        # Button
        btn1 = QPushButton(" Write Blocker On ", self)
        btn1.move(400, 30)
        btn1.resize(btn1.sizeHint())
        btn1.setEnabled(self.act(1))
        btn1.clicked.connect(on)
        btn2 = QPushButton("Write Blocker Off", self)
        btn2.move(400, 70)
        btn2.resize(btn1.sizeHint())
        btn2.setEnabled(self.act(0))
        btn2.clicked.connect(off)
        btn3 = QPushButton("Install WexB", self)
        btn3.move(400, 110)
        btn3.setEnabled(not self.de())
        btn3.resize(btn1.sizeHint())
        btn3.clicked.connect(re)
        btn4 = QPushButton("Remove WexB", self)
        btn4.move(400, 150)
        btn4.resize(btn1.sizeHint())
        btn4.setEnabled(self.de())
        btn4.clicked.connect(dele)
        btn0 = QPushButton("Quit", self)
        btn0.move(470, 210)
        btn0.resize(btn0.sizeHint())
        btn0.clicked.connect(QCoreApplication.instance().quit)
        # Interface
        self.statusBar().showMessage("status bar")
        # status_bar = self.statusBar()
        # self.setStatusBar(status_bar)
        self.setWindowTitle("WexB")
        self.setWindowIcon(QIcon("logo.ico"))
        self.move(320, 320)
        self.setFixedSize(580, 280)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

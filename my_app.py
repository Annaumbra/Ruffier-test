from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
# from second_win import *

class MainWin(QWidget):
       def __init__(self):
              super().__init__()
       def initUI(self):
              pass
       def next_click(self):
              pass
       def connects(self):
              pass
       def set_appear(self):
              pass
app = QApplication([])
mw = MainWin()
app.exec_()
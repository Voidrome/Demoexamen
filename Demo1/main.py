from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, 
    QDialog
)

from PyQt5.uic import loadUi #загрузка интерфейса
import sys

from PyQt5.QtGui import QPixmap, QIcon

class Test(QDialog):
        def __init__(self):
            super(Test, self).__init__()
            loadUi("test.ui",self) #загружаем интерфейс

app = QApplication(sys.argv) #запуcк приложения

welcome = Test()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("breddit.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon)
widget.show()
widget.setFixedWidth(1000)
widget.setFixedHeight(500)

    #запускаем приложение
try:
    sys.exit(app.exec_())
except:

    print("You close application")
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from MainWindow import Ui_MainWindow
import Window


app = QApplication(sys.argv)
window = Window.Window()
window.show()


sys.exit(app.exec_())

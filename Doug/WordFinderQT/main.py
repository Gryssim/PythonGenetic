#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
import Window


app = QApplication(sys.argv)
window = Window.Window(150, 150, 800, 600, "Testing...")


sys.exit(app.exec_())

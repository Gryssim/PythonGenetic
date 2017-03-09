#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QToolTip, QLabel, QLineEdit,QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, QSize

class Window(QWidget):
    def __init__(self, _x, _y, _height, _width, _name):
        super().__init__()
        self.x = _x
        self.y = _y
        self.height = _height
        self.width = _width
        self.name = _name
        self.text = ""
        self.edt_target = QLineEdit(self)
        self.btn_submit = QPushButton("Submit", self)
        self.letterList = []
        self.lbl_new = QLabel("" ,self)

        self.initUI()


    def initUI(self):

        lbl_target = QLabel('Target Word', self)
        #edt_target = QLineEdit(self)
        #btn_submit = QPushButton("Submit", self)

        lbl_target.move(10, 15)
        self.edt_target.move(100, 10)
        self.btn_submit.move(250, 10)
        self.lbl_new.move(100, 100)
        self.btn_submit.clicked.connect(self.saveWord)

        self.setGeometry(self.x, self.y, self.height, self.width)
        self.setWindowTitle(self.name)
        self.show()


    def saveWord(self):
        self.text = self.edt_target.text()

        self.edt_target.setText("Got It " + self.text)
        self.btn_submit.setEnabled(False)

        for letter in self.text:
            self.letterList.append(letter)

        testWord = ""
        for letter in self.letterList:
            testWord += letter + " "

        font = QFont()

        font.setUnderline(True)
        font.setPixelSize(50)
        self.lbl_new.setFont(font)
        self.lbl_new.resize(len(testWord)*50, 60)

        self.lbl_new.setText(testWord.rstrip())

        self.show()

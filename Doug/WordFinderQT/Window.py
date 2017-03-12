#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
    QToolTip, QLabel, QLineEdit,QGridLayout,QMainWindow)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication, QSize
from MainWindow import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.letterList = []
        self.underlines = []
        '''
        self.x = _x
        self.y = _y
        self.height = _height
        self.width = _width
        self.name = _name
        self.text = ""
        self.lbl_new = QLabel("" ,self)
        self.edt_target = QLineEdit(self)
        self.btn_submit = QPushButton("Submit", self)


        #self.layout = QGridLayout()
        #self.setLayout(self.layout)

        self.initUI()


    def initUI(self):

        lbl_target = QLabel('Target Word', self)
        #edt_target = QLineEdit(self)
        #btn_submit = QPushButton("Submit", self)

        #lbl_target.move(10, 15)
        self.centralWidget.addWidget(lbl_target)
        self.centralWidget.addWidget(self.edt_target)
        self.centralWidget.addWidget(self.btn_submit)
        #self.edt_target.move(100, 10)
        #self.btn_submit.move(250, 10)
        #self.lbl_new.move(100, 100)w
        self.btn_submit.clicked.connect(self.saveWord)



        self.setGeometry(self.x, self.y, self.height, self.width)
        self.setWindowTitle(self.name)
        self.show()
'''
        self.btn_submit.clicked.connect(self.saveWord)

    def saveWord(self):
        self.text = self.edt_target.text()

        #self.edt_target.setText("Got It " + self.text)
        self.btn_submit.setEnabled(False)
        self.edt_target.setEnabled(False)

        for letter in self.text:
            self.letterList.append(letter)

        testWord = ""
        for letter in self.letterList:
            testWord += letter + " "

        font = QFont()
        font.setUnderline(True)
        font.setPixelSize(50)

        for i in range(0, len(testWord.rstrip())):
            if i % 2 == 0:
                self.underlines.append(QLabel("_", self))

        for i in range(len(self.underlines)):
            self.underlines[i].move(100 + (i*50), 100)
            self.underlines[i].setFont(font)
            self.WordFinder.addWidget(self.underlines[i])
        #self.lbl_new.setText(testWord.rstrip())

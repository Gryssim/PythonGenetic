#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
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
        self.targetLetters = []
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

        expandedWord = ""
        for letter in self.letterList:
            expandedWord += letter + " "

        font = QFont()
        font.setUnderline(True)
        font.setPixelSize(50)
        font.setFamily("consolas")

        for i in range(0, len(expandedWord.rstrip())):
            if i % 2 == 0:
                self.targetLetters.append(QLabel("", self))

        for i in range(len(self.targetLetters)):
            self.targetLetters[i].move(100 + (i*50), 100)
            self.targetLetters[i].setFont(font)
            self.WordFinder.addWidget(self.targetLetters[i])
        #self.lbl_new.setText(expandedWord.rstrip())
        alphabet = ['a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p']
        #print(self.verticalLayoutWidget.children())
        for labels in self.verticalLayoutWidget.children():
            if type(labels) == type(self.verticalLayout):
                continue
            else:
                labels.setText(self.text)
                #print(labels)
                #print(">>")

        for letter in self.horizontalLayoutWidget_2.children():
            if type(letter) == type(self.WordFinder):
                continue
            else:
                letter.setText(alphabet[random.randint(0, len(alphabet) - 1)])

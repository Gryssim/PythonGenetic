#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random
import Population
import time
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
        self.mutRate = 0.0
        self.sld_popSize.setValue(1000)
        self.sld_popSize.setTickPosition(1000)
        self.sld_mutRate.setValue(1)
        self.sld_mutRate.setTickPosition(1)
        self.lbl_popSize.setText(str(1000))
        self.lbl_mutRate.setText(str(0.01))
        self.lbl_avgFitness.setText(str(0.0))
        self.lbl_currentGen.setText(str(0))

        self.btn_submit.clicked.connect(self.saveWord)
        self.sld_popSize.valueChanged.connect(self.popChange) #Set Text of Population Size label to value of slider
        self.sld_mutRate.valueChanged.connect(self.mutChange) #Set Text of Mutation Rate label to value of slider


    def popChange(self):
        self.lbl_popSize.setText(str(self.sld_popSize.value()))

    def mutChange(self):
        self.lbl_mutRate.setText(str(self.sld_mutRate.value() * 1.0 / 100))

    def saveWord(self):
        #save input word
        self.text = self.edt_target.text()
        population = Population.Population(self.text, self.sld_mutRate.value() * 1.0 / 100, self.sld_popSize.value())
        #print(self.population.mutRate, self.sld_popSize.value())
        #disable edit field and submit button
        self.btn_submit.setEnabled(False)
        self.edt_target.setEnabled(False)


        #Store each letter of text to array
        for letter in self.text:
            self.letterList.append(letter)

        #Expand letterList to a string with spaces in between each letter
        expandedWord = ""
        for letter in self.letterList:
            expandedWord += letter + " "

        #Setup font to be used in added labels
        font = QFont()
        font.setUnderline(True)
        if len(self.text) > 10:
            font.setPixelSize(30)
        else:
            font.setPixelSize(50)

        #Append new QLabels for each letter/symbol including spaces to targetLetters
        for i in range(len(expandedWord.rstrip())):
            if i % 2 == 0:
                self.targetLetters.append(QLabel("", self))

        #set each QLabel in targetLetters font to defined font
        #and add the QLabels to the WordFinder layout
        for i in range(len(self.targetLetters)):
            self.targetLetters[i].setFont(font)
            self.WordFinder.addWidget(self.targetLetters[i])

        while not population.finished:
            population.naturalSelection()
            population.generate()
            population.calcFitness()
            self.updateTopPopulation(population)
            self.updateBest(population)
            population.getBest()
            population.generations += 1
            time.sleep(0.1)
            QApplication.processEvents()

    def updateTopPopulation(self, population):
        population.population.sort(key = lambda x: x.fitness, reverse = True)

        #for pop in population.population:
            #print(pop.fitness)
            #print(">>", pop.getPhrase())
        popIndex = 0
        #print(self.verticalLayoutWidget.children()) To access
        #children of the desired verticallayout, call the widget.children()
        for labels in self.verticalLayoutWidget.children():
            # verticalLayoutWidget.children() returns all instances including
            # itself. so if type of labels matches the type of itself, continue
            if type(labels) == type(self.verticalLayout):
                continue
            else:
                #set each label in the vertical layout containing gen1-10
                #with instance of text. TODO: Fill instances with top 10 Fitness
                #results
                labels.setText(population.population[popIndex].getPhrase())
                popIndex += 1

    def updateBest(self, population):
        #Get the highest fitness in the population and display in main WordFinder

        bestWord = population.getBest()
        bestIndex = 0
        self.lbl_currentGen.setText(str(population.generations))
        self.lbl_avgFitness.setText('{0:.3f}'.format(population.getAverageFitness()))
        for letter in self.horizontalLayoutWidget_2.children():
            if type(letter) == type(self.WordFinder):
                continue
            else:
                letter.setText(bestWord[bestIndex])
                bestIndex += 1

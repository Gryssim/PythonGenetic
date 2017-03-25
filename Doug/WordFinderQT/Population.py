
import DNA
import mapProp
import random


class Population():
    def __init__(self, _targetWord, _mutRate, _popSize):
        self.mutRate = _mutRate
        self.targetWord = _targetWord
        self.popSize = _popSize
        self.population = []
        self.matingPool = []
        self.generations = 0
        self.finished = False
        self.perfect = 1

        for i in range(self.popSize):
            self.population.append(DNA.DNA(len(self.targetWord)))

        self.calcFitness()

    def calcFitness(self):
        for i in range(self.popSize):
            self.population[i].getFitness(self.targetWord)

    def naturalSelection(self):
        self.matingPool = []

        maxFitness = 0.0;
        for i in range(self.popSize):
            if self.population[i].fitness > maxFitness:
                maxFitness = self.population[i].fitness



        for i in range(self.popSize):
            fitness = mapProp.mapProp(self.population[i].fitness, 0, maxFitness, 0, 1)
            n = int(fitness * 10)
            for j in range(n):
                self.matingPool.append(self.population[i])


    def generate(self):
        for i in range(self.popSize):
            partnerA = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
            partnerB = self.matingPool[random.randint(0, len(self.matingPool) - 1)]
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutRate)
            self.population[i] = child

        self.generations += 1

    def getBest(self):
        worldRecord = 0.0;
        index = 0
        for i in range(self.popSize):
            if self.population[i].fitness > worldRecord:
                index = i
                worldRecord = self.population[i].fitness

        if worldRecord >= self.perfect:
            self.finished = True
        return self.population[index].getPhrase()

    def getAverageFitness(self):
        total = 0
        for i in range(self.popSize):
            total += self.population[i].fitness
        return total / self.popSize

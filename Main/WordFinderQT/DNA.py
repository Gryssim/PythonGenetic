import random

class DNA():
    def __init__(self, dnaLength):
        self.genes = []
        self.fitness = 0

        for i in range(dnaLength):
            self.genes.append(chr(random.randint(32, 127)))

    def getPhrase(self):
        word = ""
        for letters in self.genes:
            word += letters
        return word

    def getFitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))

        midpoint = random.randint(0, len(self.genes))

        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]

        return child


    def mutate(self, mutRate):
        for i in range(len(self.genes)):
            if random.random() < mutRate:
                self.genes[i] = chr(random.randint(32, 127))

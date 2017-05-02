import DNA

string = "Hello"

population = []

for i in range(200):
    population.append(DNA.DNA(len(string)))

newDNA = DNA.DNA(len(string))
twiceNewDNA = DNA.DNA(len(string))

print(newDNA.genes)

print(newDNA.getPhrase())

newDNA.getFitness(string)
print(newDNA.fitness)

for dna in population:
    dna.getFitness(string)
    print(dna.fitness)

crossoverDNA = newDNA.crossover(twiceNewDNA)

print(newDNA.getPhrase()," ", twiceNewDNA.getPhrase())
print(crossoverDNA.getPhrase())

crossoverDNA.mutate(0.01)

print(crossoverDNA.getPhrase())

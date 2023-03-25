import math
import random
from math import sqrt
from algoritm.Chromosome import Chromosome
from algoritm.Genome import Genome
from algoritm.Population import Population


class Genetic:
    def calc(self, points: list, precision: int = 3):
        population_size = round(sqrt(len(points)) * precision)
        population = Population(population_size)
        for i in range(population_size):
            population.add(self.generate_chromosome(points))
        population.sort()
        for i in range(precision):
            population = self.combine_population(population)
            population.sort()
        return self.parse(population.get(0))

    def parse(self, chromosome: Chromosome) -> list:
        data = []
        for genome in chromosome.list():
            data.append(genome)
        return data

    def combine_population(self, population: Population, mutation_rate: float = 0.1) -> Population:
        chromosomes = population.list()
        length = len(chromosomes) - 1
        x = math.ceil(length * 0.1)
        best = chromosomes[:x]
        missing = length - x

        for i in range(missing):
            if i % 2 == 0:
                parent1 = random.choice(best)
                parent2 = random.choice(best)
                child = self.crossover(parent1, parent2)
            else:
                parent = random.choice(best)
                child = self.mutate(parent, mutation_rate)
            best.append(child)

        new_population = Population(length)
        for chromosome in best:
            new_chromosome = self.calc_coefficient(chromosome.list())
            new_population.add(new_chromosome)

        return new_population

    def mutate(self, chromosome: Chromosome, mutation_rate: float = 0.1) -> Chromosome:
        genoms = chromosome.list()
        size = len(genoms)
        for i in range(size):
            if random.random() < mutation_rate:
                j = random.randint(0, size - 1)
                genoms[i], genoms[j] = genoms[j], genoms[i]
        new_chromosome = Chromosome(size)
        for genom in genoms:
            new_chromosome.add(genom)
        return new_chromosome

    def crossover(self, parent1: Chromosome, parent2: Chromosome) -> Chromosome:
        size = len(parent1.list())
        child = Chromosome(size)
        point1 = random.randint(0, size - 1)
        point2 = random.randint(0, size - 1)
        if point2 < point1:
            point1, point2 = point2, point1
        for i in range(point1, point2 + 1):
            child.add(parent1.list()[i])
        for genom in parent2.list():
            if genom not in child.list():
                child.add(genom)
        return child

    def generate_chromosome(self, points: list) -> Chromosome:
        random.shuffle(points)
        chromosome = self.calc_coefficient(points)

        return chromosome

    def calc_coefficient(self, points: list) -> Chromosome:
        chromosome = Chromosome(len(points))
        distance = 0

        for i in range(len(points)):
            point = points[i]
            if i != 0:
                distance += math.dist(points[i - 1], point)
            if point is list:
                genome = Genome(*point)
            else:
                genome = point
            chromosome.add(genome)

        chromosome.set_coefficient(distance)
        return chromosome

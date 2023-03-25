from algorithm import Chromosome


class Population:
    def __init__(self, size: int) -> None:
        self.size = size
        self.population = []

    def add(self, chromosome: Chromosome) -> None:
        if len(self.population) >= self.size:
            return
        self.population.append(chromosome)

    def list(self) -> list:
        return self.population

    def sort(self, invert: bool = False):
        self.population = sorted(self.population, reverse=invert, key=lambda chromosome: chromosome.get_coefficient())

    def get(self, position: int) -> Chromosome:
        return self.population[position]

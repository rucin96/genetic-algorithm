from math import inf

from algoritm import Genome


class Chromosome:
    def __init__(self, size: int) -> None:
        self.size = size
        self.genomes = []
        self.coefficient = inf

    def add(self, genome: Genome) -> None:
        if len(self.genomes) >= self.size:
            return
        self.genomes.append(genome)

    def get(self, position: int) -> Genome:
        if self.genomes[position]:
            return self.genomes[position]
        return None

    def list(self) -> list:
        return self.genomes

    def raw_list(self):
        new_list = []
        for genome in self.genomes:
            new_list.append(genome.list())
        return new_list

    def set_coefficient(self, value: float):
        self.coefficient = value

    def get_coefficient(self) -> float:
        return self.coefficient

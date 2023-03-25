from math import inf


class Chromosome:
    def __init__(self, size: int) -> None:
        self.size = size
        self.genomes = []
        self.coefficient = inf

    def add(self, genome: list) -> None:
        if len(self.genomes) >= self.size:
            return
        self.genomes.append(genome)

    def get(self, position: int) -> list:
        if self.genomes[position]:
            return self.genomes[position]
        return None

    def list(self) -> list:
        return self.genomes

    def set_coefficient(self, value: float):
        self.coefficient = value

    def get_coefficient(self) -> float:
        return self.coefficient

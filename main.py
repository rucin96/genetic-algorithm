import random
import sys

import matplotlib.pyplot as plt
from algoritm.Genetic import Genetic

if __name__ == '__main__':
    points_num = int(sys.argv[1])
    precision = int(sys.argv[2])
    points = []

    for i in range(points_num):
        nums = [random.randrange(-1000, 1000), random.randrange(-1000, 1000)]
        if nums not in points:
            points.append(nums)

    algoritm = Genetic()
    solution = algoritm.calc(points, 200)
    print(str(solution))

    xx = [row[0] for row in solution]
    yy = [row[1] for row in solution]
    plt.plot(xx, yy, color='red', zorder=0)
    plt.scatter(xx, yy, marker='o')
    plt.show()

import numpy as np
from config import *
import math

class Simulation:
    def __init__(self):
        self.reset()

    def reset(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        center = GRID_SIZE // 2
        self.grid[center, center] = PARTICLE_COUNT
        self.entropy_history = []
        self.time = 0

    def update(self):
        new_grid = np.zeros_like(self.grid)
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                count = self.grid[x, y]
                if count > 0:
                    for _ in range(count):
                        dx, dy = np.random.choice([-1, 0, 1]), np.random.choice([-1, 0, 1])
                        nx, ny = (x + dx) % GRID_SIZE, (y + dy) % GRID_SIZE
                        new_grid[nx, ny] += 1
        self.grid = new_grid
        self.time += 1
        self.entropy_history.append(self.calculate_entropy())

    def calculate_entropy(self):
        total = self.grid.sum()
        if total == 0:
            return 0
        probs = self.grid.flatten() / total
        probs = probs[probs > 0]
        return -np.sum(probs * np.log2(probs))

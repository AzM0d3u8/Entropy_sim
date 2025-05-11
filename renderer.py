import pygame
from config import *

class Renderer:
    def __init__(self, screen, simulation):
        self.screen = screen
        self.sim = simulation

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        cell_w = WIDTH / GRID_SIZE
        cell_h = HEIGHT / GRID_SIZE

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                count = self.sim.grid[x, y]
                if count > 0:
                    intensity = min(255, count * 5)
                    color = (intensity, intensity, intensity)
                    rect = pygame.Rect(x * cell_w, y * cell_h, cell_w, cell_h)
                    pygame.draw.rect(self.screen, color, rect)

        font = pygame.font.SysFont(None, 24)
        entropy = self.sim.entropy_history[-1] if self.sim.entropy_history else 0
        label = font.render(f"Entropy: {entropy:.2f} (t={self.sim.time}) - Press R to reset", True, (255, 255, 255))
        self.screen.blit(label, (10, 10))

        pygame.display.flip()

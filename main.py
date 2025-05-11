import pygame
import numpy as np
from config import *
from simulation import Simulation
from renderer import Renderer

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Early Universe Entropy Simulation")
clock = pygame.time.Clock()

simulation = Simulation()
renderer = Renderer(screen, simulation)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                simulation.reset()

    simulation.update()
    renderer.draw()

pygame.quit()

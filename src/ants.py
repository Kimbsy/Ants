import pygame
import random
from simulation import Simulation
from event_handler import EventHandler

# Seed random
random.seed()

# Initialize PyGame
pygame.init()
pygame.display.set_caption('Ants')

# Initialize screen
size = (700, 700)
surface = pygame.display.set_mode(size)

# Initialize simulation with the surface and grid size
sim = Simulation(surface, 75)

# Initialize event handler
e_handler = EventHandler()

# Define colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

while sim.is_running:

  # print(frame_count)

  # Main event loop
  for event in pygame.event.get():
    e_handler.process_event(sim, event)

  # Update the simulation
  sim.update()

  # Clear the screen
  surface.fill(BLACK)

  # Get the simulation to render itself
  sim.render(surface)

  # Update the screen with whats been drawn.
  pygame.display.flip()

  # # Limit to 50 FPS
  # clock.tick(50)

pygame.quit()

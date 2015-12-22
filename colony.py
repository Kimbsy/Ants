import pygame
from ant import Ant

class Colony:
  """Colony class creates ants and acts as their nest"""

  # Constructor
  def __init__(self, sim, x, y):
    # Keep reference to Simulation
    self.sim = sim

    # Set position
    self.x = x
    self.y = y

    # Set circle to draw
    self.radius = 10
    self.color = (0, 0, 255)

    self.spawn_rate = 50

    # Instantiate the list of ants for this colony
    self.ants = []

    # Create initil ants
    for i in range(0, self.spawn_rate):
      self.spawn()

  # Update all ants in coloy
  def update(self, dimens):
    for ant in self.ants:
      ant.update(dimens)

  # Render colony
  def render(self, surface):
    # Render colony
    pos = (self.x, self.y)
    pygame.draw.circle(surface, self.color, pos, self.radius, 0)

    # Draw all ants in colony
    for ant in self.ants:
      ant.render(surface)

  # Spawn a new ant
  def spawn(self):
    ant = Ant(self)
    self.ants.append(ant)

  # Kill specified ant
  def kill(self, ant):
    self.ants.remove(ant)

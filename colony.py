import pygame
from ant import Ant

class Colony:

  # Constructor
  def __init__(self, x, y):
    # Set position
    self.x = x
    self.y = y

    # Set circle to draw
    self.radius = 10
    self.color = (0, 0, 255)

    spawn_rate = 1

    # Instantiate the list of ants for this colony
    self.ants = []

    # Create first ant
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

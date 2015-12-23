from __future__ import division
import pygame
from ant import Ant

class Colony:
  """Colony class creates ants and acts as their nest"""

  # Constructor
  def __init__(self, sim):
    # Keep reference to Simulation
    self.sim = sim

    # Set position
    self.x = int(self.sim.dimens[0] / 2)
    self.y = int(self.sim.dimens[1] / 2)

    # Set circle to draw
    self.radius = 10
    self.color = (0, 0, 255)

    # Set the colony spawn rate
    self.spawn_rate = 50

    # Instantiate the list of ants for this colony
    self.ants = []

    # Track the spawn number
    self.spawn_count = 0

    # Spawn first ant
    self.spawn()

  # Increase the spawn count
  def inc_spawn_count(self, i):
    self.spawn_count = (self.spawn_count + i)

  # Update colony
  def update(self, dimens):
    # Increase spawn count
    self.inc_spawn_count(1)

    # Spawn ants
    spawn_limit = (1 / self.spawn_rate) * 1000
    if self.spawn_count > spawn_limit:
      self.spawn()
      self.spawn_count = 0

    # Update all ants in colony
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

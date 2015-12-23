import pygame
from random import randint

class Food:
  """Class for food objects in game"""

  # Constructor
  def __init__(self, sim):
    # Set position and dimensions
    self.set_position(sim.dimens)
    self.w = 30
    self.h = 30

    self.food_level = 1000

    self.color = (0, 255, 0)

  # Position the food in one of the corners of the screen
  def set_position(self, dimens):
    width = dimens[0]
    height = dimens[1]

    offset = [
      randint(15, 75),
      randint(15, 75),
    ]

    directions = [-1, 1]

    direction = [
      directions[randint(0, 1)],
      directions[randint(0, 1)],
    ]

    x = 0
    y = 0

    x = (x + offset[0] * direction[0]) % width 
    y = (y + offset[1] * direction[1]) % height 

    self.x = x
    self.y = y

  # Define the list of points that makes up the shape
  def get_shape(self):
    points = []

    x = self.x
    y = self.y
    w = self.w
    h = self.h

    points.append([x - (w / 2), y - (h / 2)])
    points.append([x + (w / 2), y - (h / 2)])
    points.append([x + (w / 2), y + (h / 2)])
    points.append([x - (w / 2), y + (h / 2)])

    return points

  # Draw the food to the surface
  def render(self, surface):
    pygame.draw.polygon(surface, self.color, self.get_shape(), 0)


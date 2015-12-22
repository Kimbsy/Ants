import pygame
from random import randint

class Cell:
  """Class which represents a position which can hold a pheremone level"""

  # Constructor
  def __init__(self, i, j, dimens, grid_size):
    # Set border color
    self.color = (255, 0, 0)

    # Set initial pheremone level
    self.pheremone_level = randint(0, 255)

    # Set width and height
    self.w = dimens[0] / grid_size
    self.h = dimens[1] / grid_size

    # Set x and y coords
    self.x = self.w * i
    self.y = self.h * j

  # Set the Cell's pheremone level
  def set_pheremone_level(self, pheremone_level):
    self.pheremone_level = pheremone_level

  # Increment the Cell's pheremone level
  def inc_pheremone_level(self, i):
    new = self.pheremone_level + i

    # Make sure the levels aren't going out of bounds
    if new >= 0 and new <= 255:
      self.pheremone_level = new

  # Perform an update on the Cell
  def update(self):
    self.inc_pheremone_level(-1)

  # Get the greyscale intensity of the Cell based on the pheremone level
  def get_intensity(self):
    intensity = (self.pheremone_level, self.pheremone_level, self.pheremone_level)
    return intensity

  # Draw self to surface
  def render(self, surface):
    # Define rectangle to draw
    rect = [self.x, self.y, self.w, self.h]

    # Draw the interior of the rectangle
    pygame.draw.rect(surface, self.get_intensity(), rect, 0)

    # # Draw the border rectangle
    # pygame.draw.rect(surface, self.color, rect, 1)

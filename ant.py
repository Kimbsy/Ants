import pygame

class Ant:

  # Constructor
  def __init__(self, colony):
    # Set position and dimensions
    self.x = colony.x
    self.y = colony.y
    self.w = 5
    self.h = 10

    # Set the color
    self.color = (255, 0, 0)

    # Set starting energy level
    self.energy = 1000

  # Change the energy level of the ant
  def increment_energy(self, i):
    new = self.energy + i

    if new >= 0:
      self.energy = new

  # Perform an update on the ant
  def update(self, dimens):
    self.update_pos(dimens)
    self.update_energy()

  # Update the ant's position
  def update_pos(self, dimens):
    new_x = self.x + 1
    new_y = self.y + 1

    if new_x < 0:
      new_x = dimens[0]
    if new_x > dimens[0]:
      new_x = 0

    if new_y < 0:
      new_y = dimens[1]
    if new_y > dimens[1]:
      new_y = 0

    self.x = new_x
    self.y = new_y

  # Update the ant's energy level
  def update_energy(self):
    self.increment_energy(-1)

  # Get the rectangle to draw
  def get_rect(self):
    return [self.x, self.y, self.w, self.h]

  # Draw the ant to the surface
  def render(self, surface):
    pygame.draw.rect(surface, self.color, self.get_rect(), 0)

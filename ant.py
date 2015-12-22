import pygame

class Ant:
  """Ant class"""

  # Constructor
  def __init__(self, colony):
    # Keep reference to Colony
    self.colony = colony

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
    self.leave_pheremones()

  # Update the ant's position
  def update_pos(self, dimens):
    new_x = self.x + 2
    new_y = self.y + 2

    new_pos = [new_x, new_y]

    new_pos = self.bound_pos(new_pos, dimens)

    self.x = new_pos[0]
    self.y = new_pos[1]

  # Make sure the position doesn't go off screen
  def bound_pos(self, pos, dimens):
    new_pos = []

    for i, d in enumerate(pos):
      d = d % dimens[i]
      new_pos.append(d)

    return new_pos

  # Update the ant's energy level
  def update_energy(self):
    self.increment_energy(-1)

  # Increse pheremone level in current cell
  def leave_pheremones(self):
    cell = self.colony.sim.get_cell_at((self.x, self.y))
    cell.inc_pheremone_level(40)

  # Get the rectangle to draw
  def get_rect(self):
    return [self.x, self.y, self.w, self.h]

  # Draw the ant to the surface
  def render(self, surface):
    pygame.draw.rect(surface, self.color, self.get_rect(), 0)

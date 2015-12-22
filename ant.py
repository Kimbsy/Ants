import pygame
import math
from random import randint

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

    # Set direction variables
    self.direction = 'S'
    self.direction_timer = 0

    # Set the color
    self.color = (255, 0, 0)

    # Set starting energy level
    self.energy = 500

  # Change the energy level of the ant
  def increment_energy(self, i):
    new = self.energy + i

    if new >= 0:
      self.energy = new
    else:
      self.colony.kill(self)

  # Change the direction timer of the ant
  def inc_direction_timer(self, i):
    new = self.direction_timer + i

    if new >= 0:
      self.direction_timer = new

  # Perform an update on the ant
  def update(self, dimens):
    self.update_pos(dimens)
    self.update_energy()
    self.leave_pheremones()
    self.update_direction()

  # Update the ant's position based on its direction
  def update_pos(self, dimens):
    new_pos = self.get_new_pos()
    new_pos = self.bound_pos(new_pos, dimens)

    self.x = new_pos[0]
    self.y = new_pos[1]

  def get_new_pos(self):
    pos_diff = [0, 0]

    if 'N' in self.direction:
      pos_diff[1] = -1
    if 'S' in self.direction:
      pos_diff[1] = 1
    if 'E' in self.direction:
      pos_diff[0] = 1
    if 'W' in self.direction:
      pos_diff[0] = -1

    new_pos = (self.x + pos_diff[0], self.y + pos_diff[1])

    return new_pos

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

  # Choose a random direction and an amount of time to follow it
  def update_direction(self):
    if self.direction_timer == 0:
      # Choose new direction
      directions = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
      choice = randint(0, len(directions) - 1)
      self.direction = directions[choice]
      self.direction_timer = randint(5, 50)
    else:
      # Count down the timer
      self.inc_direction_timer(-1)

  # Get the shape to draw based on direction
  def get_shape(self):
    d = self.direction
    points = []

    x = self.x
    y = self.y
    w = self.w
    h = self.h

    # Cardinal directions
    if len(d) == 1:
      if 'N' in d or 'S' in d:
        points.append([x - (w / 2), y - (h / 2)])
        points.append([x + (w / 2), y - (h / 2)])
        points.append([x + (w / 2), y + (h / 2)])
        points.append([x - (w / 2), y + (h / 2)])
      else:
        points.append([x - (h / 2), y - (w / 2)])
        points.append([x + (h / 2), y - (w / 2)])
        points.append([x + (h / 2), y + (w / 2)])
        points.append([x - (h / 2), y + (w / 2)])
    # Semi-cardinal directions
    else:
      # Start with N/S
      tmp_points = []
      tmp_points.append([x - (w / 2), y - (h / 2)])
      tmp_points.append([x + (w / 2), y - (h / 2)])
      tmp_points.append([x + (w / 2), y + (h / 2)])
      tmp_points.append([x - (w / 2), y + (h / 2)])

      # Calculate angle to rotate
      if d == 'NW' or d == 'SE':
        theta = (math.pi / 8) * 7
      else:
        theta = math.pi / 8

      # Rotate each point
      for point in tmp_points:
        temp_x = point[0] - x
        temp_y = point[1] - y

        rotated_x = (temp_x * math.cos(theta)) - (temp_y * math.sin(theta))
        rotated_y = (temp_x * math.sin(theta)) + (temp_y * math.cos(theta))

        points.append([rotated_x + x, rotated_y + y])

    return points

  # Draw the ant to the surface
  def render(self, surface):
    pygame.draw.polygon(surface, self.color, self.get_shape(), 0)

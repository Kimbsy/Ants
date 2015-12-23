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
    self.x = colony.x + randint(-20, 20)
    self.y = colony.y + randint(-20, 20)
    self.w = 5
    self.h = 10

    # Set direction variables
    self.directions = ['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'SW']
    self.direction = self.directions[randint(0, len(self.directions) - 1)]
    self.direction_timer = 20

    # Food variables
    self.has_food = False
    self.food_energy = 0

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
      pos_diff[1] = -2
    if 'S' in self.direction:
      pos_diff[1] = 2
    if 'E' in self.direction:
      pos_diff[0] = 2
    if 'W' in self.direction:
      pos_diff[0] = -2

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
    increment = (255 - cell.pheremone_level) / 3
    cell.inc_pheremone_level(increment)

  # Choose a random direction and an amount of time to follow it
  def update_direction(self):
    if self.has_food:
      self.get_direction_home()
    else:
      if self.direction_timer == 0:
        # Choose new direction
        self.get_direction_from_pheremones()
      else:
        # Count down the timer
        self.inc_direction_timer(-1)

  def get_direction_home(self):
    home_pos = (self.colony.x, self.colony.y)

    d = ''

    # North/South
    if home_pos[1] > self.y + 5:
      d = d + 'S'
    elif home_pos[1] < self.y - 5:
      d = d + 'N'

    # East/West
    if home_pos[0] > self.x + 5:
      d = d + 'E'
    elif home_pos[0] < self.x - 5:
      d = d + 'W'

    self.direction = d

  # Get random direction to move in
  def get_direction_from_random(self):
    diff = randint(-2, 2)
    choice = (self.directions.index(self.direction) + diff) % len(self.directions)
    self.direction = self.directions[choice]
    self.direction_timer = randint(15, 30)

    # self.colony.sim.direction_counts[choice] = self.colony.sim.direction_counts[choice] + 1

  # Get direction based on strongest pheremones
  def get_direction_from_pheremones(self):
    # Get neighbouring cells
    neighbours = self.colony.sim.get_surrounding_cells((self.x, self.y))

    # Find strongest pheremones
    strongest = 0
    strongest_cell_indices = []
    choice = 0
    chosen = False

    # test = []

    for i, cell in enumerate(neighbours):
      if not self.opposite(i):
        # print(i)
        # test.append((cell.grid_i, cell.grid_j))
        if cell.pheremone_level == strongest:
          # print('==')
          # print(cell.pheremone_level)
          # print(strongest)
          strongest_cell_indices.append(i)
        if cell.pheremone_level > strongest:
          # print('>')
          # print(cell.pheremone_level)
          # print(strongest)
          strongest_cell_indices = []
          strongest_cell_indices.append(i)
          strongest = cell.pheremone_level
          choice = i
          chosen = True

    # print(test)
    # print(chosen)

    # if (len(strongest_cell_indices) > 1):
    #   print(strongest_cell_indices)

    # If there was any winner
    if chosen:
      # print('chosen')
      # Pick one of the top
      index = randint(0, len(strongest_cell_indices) - 1)
      choice = strongest_cell_indices[index]
      self.direction = self.directions[choice]
      # self.direction_timer = randint(0, 10)
      self.direction_timer = 5

      # self.colony.sim.direction_counts[choice] = self.colony.sim.direction_counts[choice] + 1
    else:
      # Pick one at random
      self.get_direction_from_random()


    # print(self.direction)


  # Check whether a chosen direction is opposite the current direction
  def opposite(self, choice):
    current_index = self.directions.index(self.direction)
    # opposite_index = (current_index + 4) % len(self.directions)

    opposite = False
    # print('')
    # print(current_index)
    # print(range(current_index + 3, current_index + 6))
    for i in range(current_index + 3, current_index + 6):
      # print(i % (len(self.directions)))
      if choice == i % (len(self.directions)):
        opposite = True

    return opposite

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

from __future__ import division 
from cell import Cell
from colony import Colony
from food import Food
import math

class Simulation:
  """Main simulation class"""

  # Constuctor
  def __init__(self, surface, grid_size):
    self.is_running = True
    self.grid_size = grid_size
    self.cells = []
    self.food_items = []
    self.dimens = surface.get_size()

    # Initializa the cells
    self.init_cells()

    # Set the number of Food objects availble
    self.food_count = 1

    # Initialise Food objects
    self.init_food()

    # Initialize the colony
    self.colony = Colony(self)

  # Stop the app
  def stop(self):
    self.is_running = False

  # Create 2D list of Cell objects
  def init_cells(self):
    # Create grid_size * grid_size array of Cells
    for i in range(0, self.grid_size):
      cell_row = []
      for j in range(0, self.grid_size):
        # Pass in dimensions of surface and grid_size so Cell can decide its own size
        cell = Cell(i, j, self.dimens, self.grid_size)

        # Add it to the sim's cells list
        cell_row.append(cell)
      self.cells.append(cell_row)

  # Populate food_items list
  def init_food(self):
    for i in range(0, self.food_count):
      self.add_food()

  # Update the simulation
  def update(self):
    # Update the cells
    for cell_row in self.cells:
      for cell in cell_row:
        cell.update()

    # Update the colony
    self.colony.update(self.dimens)

    # Update food items
    for food in self.food_items:
      food.update()

  # Add food to list
  def add_food(self):
    food = Food(self)
    self.food_items.append(food)

  # Remove food from list
  def kill_food(self, food):
    self.food_items.remove(food)

  # Get the cell at the given position
  def get_cell_at(self, pos):
    # Get position ad dimensions
    width = self.dimens[0]
    height = self.dimens[1]
    x = pos[0]
    y = pos[1]

    # Calculate grid coordinates
    grid_x = int(((x / width) * self.grid_size))
    grid_y = int(((y / height) * self.grid_size))

    # Get Cell at coordinates
    cell = self.cells[grid_x][grid_y]
    return cell

  # Get the eight cells surrounding a position
  def get_surrounding_cells(self, pos):
    cells = []

    cell = self.get_cell_at(pos)

    # Calculate the indices of the rows surrounding the cell
    left_index = (cell.grid_i - 1) % self.grid_size
    right_index = (cell.grid_i + 1) % self.grid_size
    top_index = (cell.grid_j - 1) % self.grid_size
    bottom_index = (cell.grid_j + 1) % self.grid_size

    cells.append(self.cells[left_index][top_index])
    cells.append(self.cells[cell.grid_i][top_index])
    cells.append(self.cells[right_index][top_index])
    cells.append(self.cells[right_index][cell.grid_j])
    cells.append(self.cells[right_index][bottom_index])
    cells.append(self.cells[cell.grid_i][bottom_index])
    cells.append(self.cells[left_index][bottom_index])
    cells.append(self.cells[left_index][cell.grid_j])

    return cells

  # Reset the pheremone levels in the cell at a position
  def reset_cell(self, pos):
    # Find the cell to update
    cell = self.get_cell_at(pos)
    cell.set_pheremone_level(255)

  # Draw things to surface
  def render(self, surface):
    # Draw cells
    for cell_row in self.cells:
      for cell in cell_row:
        cell.render(surface)

    # Draw Food
    for food in self.food_items:
      food.render(surface)

    # Draw colony
    self.colony.render(surface)

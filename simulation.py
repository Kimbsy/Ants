from __future__ import division 
from cell import Cell
from colony import Colony
import math

class Simulation:
  """Main simulation class"""

  # Constuctor
  def __init__(self, surface):
    self.is_running = True
    self.grid_size = 0
    self.cells = []
    self.dimens = surface.get_size()

    # Initialize the colony
    self.colony = Colony(50, 50)

  # Stop the app
  def stop(self):
    self.is_running = False

  # Set the grid size in cells
  def set_grid_size(self, size):
    self.grid_size = size

  # Create 2D list of Cell objects
  def init_cells(self, surface):
    # Create grid_size * grid_size array of Cells
    for i in range(0, self.grid_size):
      cell_row = []
      for j in range(0, self.grid_size):
        # Pass in dimensions of surface and grid_size so Cell can decide its own size
        cell = Cell(i, j, self.dimens, self.grid_size)

        # Add it to the sim's cells list
        cell_row.append(cell)
      self.cells.append(cell_row)

  # Update the simulation
  def update(self):
    # Update the cells
    for cell_row in self.cells:
      for cell in cell_row:
        cell.update()

    # Update the colony
    self.colony.update(self.dimens)

  # Get the cell at the given mouse position
  def get_cell_at(self, pos):
    # Get position ad dimensions
    width = self.dimens[0]
    height = self.dimens[1]
    x = pos[0]
    y = pos[1]

    # Calculate grid coordinates
    grid_x = int(math.floor((x / width) * self.grid_size))
    grid_y = int(math.floor((y / height) * self.grid_size))

    # Get Cell at coordinates
    cell = self.cells[grid_x][grid_y]
    return cell


  # Reset the pheremone levels in the cell moved over
  def reset_cell(self, mouse_pos):
    # Find the cell to update
    cell = self.get_cell_at(mouse_pos)
    cell.set_pheremone_level(255)

  # Draw things to surface
  def render(self, surface):
    # Draw cells
    for cell_row in self.cells:
      for cell in cell_row:
        cell.render(surface)

    # Draw colony
    self.colony.render(surface)

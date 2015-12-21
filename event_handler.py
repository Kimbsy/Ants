import pygame

class EventHandler:
  """Class to handle keyboard and mouse events"""

  @staticmethod
  def process_event(sim, e):
    if e.type == pygame.QUIT:
      sim.stop()
    elif e.type == pygame.MOUSEMOTION:
      sim.reset_cell(e.pos)

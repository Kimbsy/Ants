# Ants
---
A small Python app that simulates an ant colony.

You will need to install pygame:
```bash
# Install python-dev (required by pygame)
sudo apt-get install python-dev
# Install pygame
sudo apt-get install python-pygame
```

To run:
```bash
./build.sh
```

Initial behaiviour algorithm goal:
```
Condition:                                 |    Action:
Not carrying food not on pheromone trail   |    walk randomly lay pheromone
Not carrying food on pheromone trail       |    follow pheromone trail lay pheromone
Reach food                                 |    pick up food
Carrying food                              |    go home
Reach home with food                       |    deposit food turn around
```

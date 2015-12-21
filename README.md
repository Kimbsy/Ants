# Ants
---
A small Python app that simulates an ant colony.

To compile and run:
```bash
./build.sh
```


```
Condition:                                 |    Action:
Not carrying food not on pheromone trail   |    walk randomly lay pheromone
Not carrying food on pheromone trail       |    follow pheromone trail lay more pheromone
Reach home without food on pheromone trail |    turn around follow trail in opposite direction
Reach food                                 |    pick up food turn around follow trail in opposite direction
Carrying food                              |    follow trail lay more pheromone
Reach home with food                       |    deposit food turn around follow trail in opposite direction
```
# life
Conway's Game of Life (Cellular Automata)

A python class for John H. Conway's game of life.

## Documentation
The game state is stored in a numpy array with 1 symoblizing an alive cell and 0 symbolizing a dead cell.

game.py only includes one class for creating a game object and then some basic functions to help out the class
```
from life import Game
```
After importing the Game class, an instance of Conway's Game of Life can be created. The 'Game' class needs an initial shape/size to be given as the first parameter. This is expressed as a tuple with a length of 2. The 'Game' class can also take an initial game state as a second parameter. This initial game state must be a 2 dimensional array with a shape/size that matches that of the first parameter. If an initial state is not specified, the game will be initialized with a blank state.
```
game = Game((5,5)) # creates a 5x5 game of life with a blank state
```
```
initial_state = [[0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
game = Game((5,5), initial_state) # creates a 5x5 game of life with an initial starting state
```

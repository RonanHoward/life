# life
Conway's Game of Life (Cellular Automata)

A python class for John H. Conway's game of life.

uses numpy

## Documentation
The game state is stored in a numpy array with 1 symoblizing an alive cell and 0 symbolizing a dead cell. The game is displayed in the python console using a grid of ascii characters.

game.py only includes one class for creating a game object and then some basic functions to help out the class
```
from life import Game
```
After importing the Game class, an instance of Conway's Game of Life can be created. The 'Game' class needs an initial shape/size to be given as the first parameter. This is expressed as a tuple with a length of 2. The 'Game' class can also take an initial game state as a second parameter. This initial game state must be a 2 dimensional array with a shape/size that matches that of the first parameter. If an initial state is not specified, the game will be initialized with a blank state.
```
game = Game((5,5)) # creates a blank 5x5 game of life
```
```
initial_state = [[0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
game = Game((5,5), initial_state) # creates a 5x5 game of life with an initial starting state
```
The current state of the game can be retrieved with the 'state' property.
```
game.state
```

Now time to play a couple of generations...
This can be done with the 'run_n_generations' method. This method only needs an integer which is the amount of generations that you would like to run. The method can also take a number delay so that you can see each generation sequentially as is appears in the console (instead of scrolling through what each generation looks like). Delay is inputted in seconds. The last parameter is a boolean for wether or not you would like for each generation to be labeled with it's generation number.
```
game.run_n_generations(10, s=0.5, label=True) # run 10 labeled generations, waiting 0.5 seconds in between each generation

game.run_n_generations(10) # this is also a valid way to call the method
```

### Other functions & fun stuff
The 'Game' class also has some other functions which are used in 'run_n_generations', but can be referenced for use alone. The 'nextGeneration' method returns the state of the next generation without actually changing the state property of the game instance. This method does not take any parameters.
```
game.nextGeneration()
```
Likewise, 'setNextGeneration' also returns the next generation, but it also sets the state property of the class instance to the next generation. This method does not take any parameters.
```
game.setNextGeneration()
```
The 'display' method will display the current game state or one specified in the parameter.
```
game.display() #displays current game state
game.display(some_other_game_state) # displays the array specified
```
The characters used in display and amount of blank lines between each generation can be edited by changing some class properties.
```
# default values:
game.alive_char = '# '
game.dead_char  = '. '
game.dead_lines = 2
```

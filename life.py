# game driver for python life
import numpy as np
import time

def inBounds(index, array): # index is tuple a[0][1] -> (0,1)
    array = np.array(array)
    assert isinstance(index,tuple)
    assert len(index) == len(array.shape) # check dimensions
    for i in range(len(index)):
        if not (index[i] >= 0 and index[i] < array.shape[i]):
            return False
    return True



# ---------- game of life class ----------
class Game:
    def __init__(self,size,initial_state=None):
        # check for valid parameters
        assert isinstance(size,tuple)
        assert len(size) == 2
        if initial_state is not None:
            initial_state = np.array(initial_state)
            assert initial_state.shape == size
        
        # initialize
        self.state = np.zeros(size)
        self.size  = size
        
        self.dead_char  = '. '
        self.alive_char = '# '
        self.dead_lines = 2
        
        if initial_state is not None: self.state = initial_state
        
        pass
    
    def nextGeneration(self):
        nextGen = np.zeros(self.size)
        # neighbors_arr = np.zeros(self.size)
        
        # check though every cell (left->right, top->bottom)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                
                # check each neighbor (upper bound on range is not inclusive)
                neighbors = []
                for a in range(-1,2):
                    for b in range(-1,2):
                        if not inBounds((i+a,j+b),self.state): continue
                        if a == 0 and b == 0: continue # leave out current cell
                        neighbors.append(self.state[i+a][j+b]) # get neighbor
                pass
            
                # eval living or dead
                neighbors = np.sum(neighbors)
                # neighbors_arr[i][j] = neighbors
                if neighbors < 2:
                    nextGen[i][j] = 0
                elif neighbors == 2:
                    nextGen[i][j] = self.state[i][j]
                elif neighbors == 3:
                    nextGen[i][j] = 1
                elif neighbors > 3:
                    nextGen[i][j] = 0
                # ^^ loop ^^
        pass
        # print(neighbors_arr)
        return nextGen
    
    # process and set game state to next generation
    def setNextGeneration(self):
        self.state = self.nextGeneration()
        return self.state
    # process, set, and display multiple generations with sleep function
    def run_n_generations(self,generations,s=None,label=False):
        assert isinstance(generations,int)
        
        #display initial condition
        if label: self.display(self.state,0)
        else: self.display(self.state)
        
        # display the rest of the generations
        # (algorithm differs slightly if sleep and label are active)
        if s is not None:
            if label:
                for i in range(generations):
                    time.sleep(s)
                    self.display(self.setNextGeneration(),i+1)
                return
            else:
                for i in range(generations):
                    time.sleep(s)
                    self.display(self.setNextGeneration())
                return
        if label:
            for i in range(generations):
                self.display(self.setNextGeneration(),i+1)
        else:
            for i in range(generations):
                self.display(self.setNextGeneration())
        return
    
    # makes displaying easier 0_0
    def toChar(self,x):
        if x == 0: return self.dead_char
        return self.alive_char
    
    # display game state (see alive and dead char variables)
    def display(self,state=None,label=None):
        if state is None: state = self.state
        else: state = np.array(state)
        
        # print dead lines
        for i in range(self.dead_lines): print()
        # add label (if necessary)
        if label is not None:
            print('Generation: '+str(label))
        # print each character
        for i in range(state.shape[0]):
            for j in range(state.shape[1]):
                print(self.toChar(state[i][j]),end='')
            print()
        return

import os
import numpy as np
import time

ROW_MAX = 60 
ROW_MIN = 0 

COL_MAX = 240
COL_MIN = 0

class cell: # x,y coordinate of cell
    def __init__(self, row: int, col: int, curr_state: int, next_state: int): 
        # make sure to keep the coordinate within the max and min

        if row > ROW_MAX:
            row = ROW_MAX 
        elif row < ROW_MIN:
            row = ROW_MIN
        if col > COL_MAX:
            col = COL_MAX
        elif col < COL_MIN:
            col = COL_MIN

        if curr_state != 1: # state == 1 means cell is alive, and 0 means cell is dead
            curr_state = 0
        if next_state != 1:  
            next_state = 0
    
        # make sure to get x,y
        self.row = int(row)
        self.col = int(col)
        self.curr_state = curr_state
        self.next_state = next_state
    
    def draw_cell(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.row};{self.col}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        if self.curr_state == 1:
            print("\033[32mC\033[0m") # drawing a star with text color being green
        else:
            print(" ") # printing white space, indicating that the cell is dead

    def check_neighbours(self, cell_matrix): # checking how many neighbours are alive, and return number of live cells
        row = self.row
        col = self.col

        r_bound_max = True
        r_bound_min = True
        c_bound_max = True
        c_bound_min = True

        live_count = 0

        if row >= ROW_MAX:
            r_bound_max = False
        if row <= ROW_MIN:
            r_bound_min = False
        
        if col >= COL_MAX:
            c_bound_max = False
        if col <= COL_MIN:
            c_bound_min = False
        
        if r_bound_max == True and c_bound_min == True:
            for i in range(-1, 2):
                if i != 0:
                    if cell_matrix[row+i][col+i].curr_state == 1:
                        live_count += 1
                    if cell_matrix[row+i][col].curr_state == 1:
                        live_count += 1
                    if cell_matrix[row][col + i].curr_state == 1:
                        live_count += 1
                    if cell_matrix [row + i][col - i].curr_state == 1:
                        live_count += 1
            
            return live_count 
        else:
            print("ERROR!!!!! OUT OF BOUND")
    

def clear_terminal():
    if os.name == 'posix': # Linux or macOS
        os.system('clear') # clears the terminal
    elif os.name == 'nt': # Windows
        os.system('cls') # clears the terminal
    else: 
        print("operating system: " + os.name)



# Conway's game of life rules
# Any live cell with fewwer than two live neighbours dies, as if caused by underpopulation
# Any live cell with two or three live neighbours live on to the next generation
# Any live cell with more than three live neighbours dies, as if by overpopulation
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

if __name__ == "__main__":
    # make cell matrix with all cells being dead
    clear_terminal()

    cell_matrix = np.empty((ROW_MAX, COL_MAX), dtype=cell)

    for row in range (len(cell_matrix)): # row = y
        for col in range (len(cell_matrix[0])): # col = x
            c = cell(row, col, 0, 0) # make a cell at proper row and col, with cell state being dead
            cell_matrix[row][col] = c
    
    
    # oscillator (blinker)
    cell_matrix[15, 60].curr_state = 1
    cell_matrix[15, 61].curr_state = 1
    cell_matrix[15, 62].curr_state = 1
    cell_matrix[14, 61].curr_state = 1
    cell_matrix[16, 61].curr_state = 1

    # oscillator (lighthouse)
    cell_matrix[30, 100].curr_state = 1
    cell_matrix[30, 101].curr_state = 1
    cell_matrix[31, 100].curr_state = 1
    cell_matrix[32, 103].curr_state = 1
    cell_matrix[33, 103].curr_state = 1
    cell_matrix[33, 102].curr_state = 1

    # oscillator (glider)

    cell_matrix[5, 30].curr_state = 1
    cell_matrix[6, 31].curr_state = 1
    cell_matrix[6, 32].curr_state = 1
    cell_matrix[5, 32].curr_state = 1
    cell_matrix[4, 32].curr_state = 1



    for row in range (len(cell_matrix)): # row = y
        for col in range (len(cell_matrix[0])): # col = x
            cell_matrix[row][col].draw_cell()

    while(True):
        for row in range (2, 50):
            for col in range (2, 200):
                c = cell_matrix[row][col]
                live_count = c.check_neighbours(cell_matrix)
                if c.curr_state == 1: # when cell is alive
                    if live_count < 2:
                        c.next_state = 0
                    elif live_count > 1 and live_count < 4:
                        c.next_state = 1
                    elif live_count > 3:
                        c.next_state = 0
                else: # when cell is dead
                    if live_count == 3:
                        c.next_state = 1
        
        for row in range (len(cell_matrix)): # row = y
            for col in range (len(cell_matrix[0])): # col = x
                next_cell = cell_matrix[row][col]
                next_cell.curr_state = next_cell.next_state
                next_cell.next_state = 0 
                next_cell.draw_cell()
        
        time.sleep(0.01)
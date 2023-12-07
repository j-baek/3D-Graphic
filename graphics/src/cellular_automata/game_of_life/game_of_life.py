import os
import numpy as np
import time

ROW_MAX = 50 
ROW_MIN = 0 

COL_MAX = 180
COL_MIN = 0

def is_valid_index(row, col): # checking whether the index is within max and min of row and col
    if row < ROW_MAX and row >= ROW_MIN:
        if col < COL_MAX and col >= COL_MIN:
            return True
    return False 


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
        print(f"\033[{self.row};{self.col}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        # 'u2588' is unicode for full block
        if self.curr_state == 1:
            print("\033[32m" + "\u2588" + "\033[0m") # drawing a star with text color being green
        else:
            print(" ") # printing white space, indicating that the cell is dead

    def check_neighbours(self, cell_matrix): # checking how many neighbours are alive, and return number of live cells
        row = self.row
        col = self.col

        i = -1
        live_count = 0
        while(i < 2):
            if is_valid_index(row+i, col+i):
                if cell_matrix[row+i][col+i].curr_state == 1:
                    live_count += 1
            if is_valid_index(row+i, col):
                if cell_matrix[row+i][col].curr_state == 1:
                    live_count += 1
            if is_valid_index(row, col+i):
                if cell_matrix[row][col + i].curr_state == 1:
                    live_count += 1
            if is_valid_index(row+i, col - i):
                if cell_matrix [row + i][col - i].curr_state == 1:
                    live_count += 1
            i += 2

        return live_count
    

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
    cell_matrix[5, 60].curr_state = 1
    cell_matrix[5, 61].curr_state = 1
    cell_matrix[5, 62].curr_state = 1
    cell_matrix[4, 61].curr_state = 1
    cell_matrix[6, 61].curr_state = 1

    # oscillator (lighthouse)
    cell_matrix[10, 100].curr_state = 1
    cell_matrix[10, 101].curr_state = 1
    cell_matrix[11, 100].curr_state = 1
    cell_matrix[12, 103].curr_state = 1
    cell_matrix[13, 103].curr_state = 1
    cell_matrix[13, 102].curr_state = 1

    # Spaceship (glider)
    cell_matrix[5, 30].curr_state = 1
    cell_matrix[6, 31].curr_state = 1
    cell_matrix[6, 32].curr_state = 1
    cell_matrix[5, 32].curr_state = 1
    cell_matrix[4, 32].curr_state = 1

    # Spaceship (glider)
    cell_matrix[5, 25].curr_state = 1
    cell_matrix[6, 26].curr_state = 1
    cell_matrix[6, 27].curr_state = 1
    cell_matrix[5, 27].curr_state = 1
    cell_matrix[4, 27].curr_state = 1

     # Spaceship (glider)
    cell_matrix[5, 35].curr_state = 1
    cell_matrix[6, 36].curr_state = 1
    cell_matrix[6, 37].curr_state = 1
    cell_matrix[5, 37].curr_state = 1
    cell_matrix[4, 37].curr_state = 1

    # Spaceship (glider)
    cell_matrix[20, 60].curr_state = 1
    cell_matrix[20, 61].curr_state = 1
    cell_matrix[21, 60].curr_state = 1
    cell_matrix[21, 62].curr_state = 1
    cell_matrix[22, 60].curr_state = 1

    # Spaceship (glider)
    cell_matrix[20, 65].curr_state = 1
    cell_matrix[20, 66].curr_state = 1
    cell_matrix[21, 65].curr_state = 1
    cell_matrix[21, 67].curr_state = 1
    cell_matrix[22, 65].curr_state = 1

    # Spaceship (glider)
    cell_matrix[20, 70].curr_state = 1
    cell_matrix[20, 71].curr_state = 1
    cell_matrix[21, 70].curr_state = 1
    cell_matrix[21, 72].curr_state = 1
    cell_matrix[22, 70].curr_state = 1

    # Spaceship (glider)
    cell_matrix[15, 70].curr_state = 1
    cell_matrix[15, 71].curr_state = 1
    cell_matrix[16, 70].curr_state = 1
    cell_matrix[16, 72].curr_state = 1
    cell_matrix[17, 70].curr_state = 1

    # Spaceship (glider)
    cell_matrix[25, 70].curr_state = 1
    cell_matrix[25, 71].curr_state = 1
    cell_matrix[26, 70].curr_state = 1
    cell_matrix[26, 72].curr_state = 1
    cell_matrix[27, 70].curr_state = 1

    # replicator
    cell_matrix[15, 50].curr_state = 1
    cell_matrix[16, 50].curr_state = 1
    cell_matrix[17, 50].curr_state = 1

    cell_matrix[17, 51].curr_state = 1
    cell_matrix[17, 52].curr_state = 1

    cell_matrix[14, 51].curr_state = 1

    cell_matrix[16, 53].curr_state = 1

    cell_matrix[15, 54].curr_state = 1
    cell_matrix[14, 54].curr_state = 1
    cell_matrix[13, 54].curr_state = 1

    cell_matrix[13, 53].curr_state = 1
    cell_matrix[13, 52].curr_state = 1

    R_M = int(ROW_MAX/2)
    COL_M = int(COL_MAX /2)
    r_off_set = -5
    c_off_set = -50

    cell_matrix[R_M + r_off_set, COL_M + c_off_set].curr_state = 1
    cell_matrix[R_M+1 + r_off_set, COL_M + c_off_set].curr_state = 1
    cell_matrix[R_M+2 + r_off_set, COL_M + c_off_set].curr_state = 1

    cell_matrix[R_M+2 + r_off_set, COL_M+1 + c_off_set].curr_state = 1
    cell_matrix[R_M+2 + r_off_set, COL_M+2 + c_off_set].curr_state = 1

    cell_matrix[R_M-1 + r_off_set, COL_M+1 + c_off_set].curr_state = 1

    cell_matrix[R_M+1 + r_off_set, COL_M+3 + c_off_set].curr_state = 1

    cell_matrix[R_M + r_off_set, COL_M+4 + c_off_set].curr_state = 1
    cell_matrix[R_M-1 + r_off_set, COL_M+4 + c_off_set].curr_state = 1
    cell_matrix[R_M-2 + r_off_set, COL_M+4 + c_off_set].curr_state = 1

    cell_matrix[R_M-2 + r_off_set, COL_M+3 + c_off_set].curr_state = 1
    cell_matrix[R_M-2 + r_off_set, COL_M+2+ c_off_set].curr_state = 1

    for row in range (len(cell_matrix)): # row = y
        for col in range (len(cell_matrix[0])): # col = x
            cell_matrix[row][col].draw_cell()

    while(True):
        for row in range (ROW_MIN, ROW_MAX):
            for col in range (COL_MIN, COL_MAX):
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
                
        time.sleep(0.1)
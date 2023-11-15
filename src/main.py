import os
import time

X_MAX = 261
X_MIN = 0
Y_MAX = 0
Y_MIN = 60

X_MID = 131 # approximate mid of x 
Y_MID = 30  # mid of y

class coord: # x,y coordinate
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    
    def draw(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.y};{self.x}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        print("\033[32m*\033[0m") # drawing a star with text color being green

    def draw_horizontal(self,end_c): # take self, and end coordinate
        for x in range(self.x, end_c.x):
            dot = coord(x, end_c.y)
            dot.draw()
            time.sleep(0.02)
    
    def draw_vertical(self, end_c): # take self, and end coordinate
        for y in range(self.y, end_c.y, -1): # since y = 0 at the top of the terminal, drawing vertically upward would need y to be continuously decremented
            dot = coord(end_c.x, y)
            dot.draw()
            time.sleep(0.02)



# clear terminal before display an ojbect on terminal
def clear_terminal():
    if os.name == 'posix': # Linux or macOS
        os.system('clear') # clears the terminal
    elif os.name == 'nt': # Windows
        os.system('cls') # clears the terminal
    else: 
        print("operating system: " + os.name)

if __name__ == "__main__":
    clear_terminal()

    start_coord = coord(X_MID, Y_MID)
    end_coord = coord(X_MAX, Y_MID)
    start_coord.draw_horizontal(end_coord)

    end_coord2 = coord(X_MID, Y_MAX)
    start_coord.draw_vertical(end_coord2)

    
    
else:
    print("imported")
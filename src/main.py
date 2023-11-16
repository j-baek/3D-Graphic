import os
import time

X_MAX = 260
X_MIN = 0
Y_MAX = 0 # first row of terminal is at y = 0
Y_MIN = 60 # last row of terminal is at y = Y_MIN

X_MID = 130 # mid of x
Y_MID = 30  # mid of y

DELAY = 0.02 # delay of drawing 

class dot: # x,y coordinate
    def __init__(self, x, y): 
        # make sure to keep the coordinate within the max and min
        if x > X_MAX:
            x = X_MAX
        elif x < X_MIN:
            x = X_MIN
        if y < Y_MAX: # first row is at y = 0
            y = Y_MAX
        elif y > Y_MIN: # last row is at y = Y_MIN
            y = Y_MIN
    
        self.x = x
        self.y = y
    
    def draw_dot(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.y};{self.x}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        print("\033[32m*\033[0m") # drawing a star with text color being green

    def draw_line(self,end_c): # take self, and end coordinate
        # X_MAX : Y_MIN
        # 260 : 60
        # approximation: 4:1 
        c_x = 1 # counter for x
        if self.x > end_c.x:
            c_x = -1 # if self.x is bigger, it needs to decrement to reach end_c.x
        
        c_y = 1 # counter for y
        if self.y > end_c.y:
            c_y = -1

        x_diff = abs(self.x - end_c.x)
        y_diff = abs(self.y - end_c.y)
        slope = y_diff/x_diff

        for x in range(self.x, end_c.x, c_x):
            y = int(slope * x)
            coord = dot(x,y)
            coord.draw_dot()
            time.sleep(DELAY)




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

    start_coord = dot(-23423432, 23423423)
    end_coord = dot(2343242342, -23423432)
    start_coord.draw_line(end_coord)

    
    
else:
    print("imported")
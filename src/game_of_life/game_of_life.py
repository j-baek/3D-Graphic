X_MAX = 120
X_MIN = -120
Y_MAX = -30 # first row of terminal is at y = 0
Y_MIN = 30 # last row of terminal is at y = Y_MIN

X_OFFSET = 120
Y_OFFSET = 30

class pixel: # x,y coordinate of pixel
    def __init__(self, x: int, y: int): 
        # make sure to keep the coordinate within the max and min

        if x > X_MAX:
            x_m = x % X_MAX # e.g. x = 270, X_MAX = 250, then x_m = 20
            x = X_MAX - x_m # x = 250 - 20 = 230
        elif x < X_MIN:
            x = abs(x) % X_MAX # e.g. x = - 270, X_MAX = 250, then x_m = 20
        
        if y < Y_MAX:
            y = abs(y) % Y_MIN # e.g. y = -70, Y_MIN = 60, then y = 10
        elif y > Y_MIN:
            y_m = y % Y_MIN # e.g. y = 70, Y_MIN = 60, then y_m = 10
            y = Y_MIN - y_m # y = 60 - 10 = 50
    
        # make sure to get x,y,z to be integer 
        self.x = int(x)
        self.y = int(y)
    
    def draw_dot(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.y + Y_OFFSET};{self.x + X_OFFSET}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        print("\033[32m*\033[0m") # drawing a star with text color being green

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



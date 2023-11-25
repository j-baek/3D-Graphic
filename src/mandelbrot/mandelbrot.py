import os 
import math
import time

X_MAX = 260 # x = column
Y_MAX = 60 # y = row
X_MIN = 0
Y_MIN = 0

X_POS_MAX = 120
X_NEG_MAX = -120
Y_POS_MAX = 30
Y_NEG_MAX = -30

SLOPE = 1/4 # since y is about 1/4 smaller than x, to get the proportion right, multiply slope when drawing a graph

X_OFF_SET = 120
Y_OFF_SET = 30

ZOOM_RANGE = 300
TIME_DELAY = 0.01

# clear terminal before display an ojbect on terminal
def clear_terminal():
    if os.name == 'posix': # Linux or macOS
        os.system('clear') # clears the terminal
    elif os.name == 'nt': # Windows
        os.system('cls') # clears the terminal
    else: 
        print("operating system: " + os.name)

def draw_point(x,y):
    x = int(x)
    y = int(y)
    # moving cursor to appropriate position
    # Y_MIN - y value is for setting y position upside down as in terminal, y increases as it goes down
    print(f"\033[{Y_MIN - y+Y_OFF_SET};{x+X_OFF_SET}H", end="") 
    print("\033[32m" + "." + "\033[0m") # draw dot 

def x_square_func(x):
    y = x*x*SLOPE
    return y

def draw_function(math_func, scale): # take math funciton and scale for zooming
    for x in range(X_NEG_MAX, X_POS_MAX):
        if x < X_NEG_MAX: 
            x = X_NEG_MAX
        elif x > X_POS_MAX:
            x = X_POS_MAX
        y = math_func(x) * scale
        if y >= Y_NEG_MAX and y <= Y_POS_MAX:
            draw_point(x,y)

def zoom_in():
    for i in range(1, ZOOM_RANGE):
        scale = 1/i
        draw_function(x_square_func, scale)
        time.sleep(TIME_DELAY)
        clear_terminal()

def zoom_out():
    for i in range(ZOOM_RANGE, 0, -1):
        scale = 1/i
        draw_function(x_square_func, scale)
        time.sleep(TIME_DELAY)
        clear_terminal()


if __name__ == "__main__":
    clear_terminal()

    draw_function(x_square_func, 1)

    zoom_in()
    clear_terminal()
    print("now zooming out")
    time.sleep(3)
    zoom_out()

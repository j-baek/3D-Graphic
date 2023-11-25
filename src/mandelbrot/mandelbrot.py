import os 
import math

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

def sin_func(x):
    x = math.radians(x)
    y = math.sin(x)
    return y



def draw_function(math_func):
    for x in range(X_NEG_MAX, X_POS_MAX):
        y = math_func(x)
        if y >= Y_NEG_MAX and y <= Y_POS_MAX:
            draw_point(x,y)







if __name__ == "__main__":
    clear_terminal()

    draw_function(x_square_func)
    draw_function(sin_func)

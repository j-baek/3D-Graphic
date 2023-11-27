import os 
import time
import numpy as np

X_MAX = 260 # x = column
Y_MAX = 60 # y = row
X_MIN = 0
Y_MIN = 0

X_POS_MAX = 120
X_NEG_MAX = -120
Y_POS_MAX = 30
Y_NEG_MAX = -30

SLOPE = 1 # since y is about 1/4 smaller than x, to get the proportion right, multiply slope when drawing a graph

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

def mandelbrot_iteration(x,y, max_iteration): # number of iterations it takes to fall out of mandelbrot set
    # complex number takes (real, imag), so if x = 3, y =2, z0 = 3 + 2j, where j indicates imaginary number
    z0 = complex(x,y) 
    z = 0 # initial val of z

    for i in range(0, max_iteration):
        z = z**2 + z0
        if abs(z) > 2:
            return i
    return max_iteration 

def get_ascii(iteration, max_iteration): # get ascii character based on the iterations. the darker it is, the more iteration it tkaes
    ascii_char = [" ", ",", "-", "~", ":", ";", "=", "!", "*","#", "$", "@"] #darkest to brightest
    if iteration == 0:
        iteration = 1
    i = int(max_iteration/iteration) -1 # index starts at 0 so - 1 required
    if i >= len(ascii_char):
        i = len(ascii_char) -1
    
    return ascii_char[i]


if __name__ == "__main__":
    clear_terminal()
    matrix = [["."]*X_MAX for _ in range(Y_MAX)] # make a matrix with row = Y_MAX and col = X_MAX
    max_iteration = 5000

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # col - X_POS_MAX and row - Y_POS_MAX centers the image at the origin (0,0) in mathematical space
            # scaling factor scales x and y accordingly. e.g. to set x and y to range from (-2,2), set scaling factor to be 2.
            # e.g. when col = 260 (at max), then x = (260 - 130) / (130/2) = 130 / (130/2) = 130 * 2 / 130 = 2. 
            scale = 1.5
            x = (col - X_POS_MAX) * (scale/X_POS_MAX)
            y = (row - Y_POS_MAX) * (scale/Y_POS_MAX)

            m_set_iteration = mandelbrot_iteration(x,y, max_iteration)
            matrix[row][col] = get_ascii(m_set_iteration, max_iteration)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")
        print() # for new line for every row
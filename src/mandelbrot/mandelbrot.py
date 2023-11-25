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


def is_point_in_m_set(x,y, max_iteration):
    # complex number takes (real, imag), so if x = 3, y =2, z0 = 3 + 2j, where j indicates imaginary number
    z0 = complex(x,y) 
    z = 0 # initial val of z

    for i in range(0, max_iteration):
        z = z**2 + z0
        if abs(z) > 2:
            return False
    return True

if __name__ == "__main__":
    clear_terminal()
    matrix = [["."]*X_POS_MAX for _ in range(Y_MAX)] # make a matrix with row = Y_MAX and col = X_MAX
    max_iteration = 100
    x = -2
    for row in range(len(matrix)):
        y = -2
        for col in range(len(matrix[0])):
            z = complex(x,y)
            in_m_set = is_point_in_m_set(x,y, max_iteration)
            if in_m_set == True:
                matrix[row][col] = "@"
            else:
                matrix[row][col] = " "
            y += 0.066666666666* col
        x += 0.03076923076 * row
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(matrix[row][col], end=" ")







    '''
    max_iteration = 1000
    for x in range(X_NEG_MAX, X_POS_MAX):
        for y in range(Y_NEG_MAX, Y_POS_MAX):
            in_m_set = is_point_in_m_set(x,y, max_iteration)
            if in_m_set == True:
                draw_point(x,y)
    '''

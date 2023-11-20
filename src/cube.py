import os
import time
import math
import numpy as np

X_MAX = 261
X_MIN = 0
Y_MAX = 0 # first row of terminal is at y = 0
Y_MIN = 60 # last row of terminal is at y = Y_MIN

X_MID = 120 # mid of x
Y_MID = 30  # mid of y

DELAY = 0 # delay of drawing 

class dot: # x,y coordinate
    def __init__(self, x: int, y: int, z: int): 
        # make sure to keep the coordinate within the max and min
        if x > X_MAX:
            x = X_MAX
        elif x < X_MIN:
            x = X_MIN
        if y < Y_MAX: # first row is at y = 0
            y = Y_MAX
        elif y > Y_MIN: # last row is at y = Y_MIN
            y = Y_MIN
    
        # make sure to get x,y,z to be integer 
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    
    def draw_dot(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.y};{self.x}H", end="") # move the point to the appropriate position
        # '\033[32m' makes the text colour to be green, and '\033[0m' resets the text formmating back to the default
        print("\033[32m*\033[0m") # drawing a star with text color being green

    def draw_line(self,end_c): # take self, and end coordinate
        c_x = 1 # counter for x
        if self.x > end_c.x:
            c_x = -1 # if self.x is bigger, it needs to decrement to reach end_c.x
        c_y = 1 # counter for y
        if self.y > end_c.y:
            c_y = -1 # if self.y is bigger, it needs to decrement to reach end_c.y
        
        x_diff = self.x - end_c.x
        y_diff = self.y - end_c.y

        if x_diff == 0 or y_diff == 0: # when it is a horizontal or vertical line
            slope = 0 # if y_diff = 0, then slope = 0 and if x_diff = 0, slope undefined
        else:
            slope = y_diff/x_diff # slope = y/x

        x_i = self.x # initial x val
        y_i = self.y # initial y val 

        # draw a line with y = a*x function or a horizontal line
        if x_diff != 0:
            for x in range(self.x, end_c.x, c_x):
                if slope != 0:
                    y = round(slope*(x - x_i)) + y_i # y = k(x - x_i) + y_i
                else: # when slope is 0 
                    y = y_i
                print("x = " + str(x) + " y = " + str(y) + " z = " + str(self.z))
                coord = dot(x,y, self.z)
                #print("x = " + str(coord.x) + " y = " + str(coord.y))
                coord.draw_dot()
                time.sleep(DELAY)
        else: # draw a vertical line
            for y in range(self.y, end_c.y, c_y):
                coord = dot(end_c.x, y, self.z)
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


def trd_twod(coord: dot): # get a dot and change it into 2d- vector
    vec = [coord.x, coord.y, coord.z]
    return vec


def rotate_x(vec: list, angle): # rotate on x-axis
    #rot_mat_x = [
    #    [math.cos(angle_rad), -math.sin(angle_rad), 0],
    #    [math.sin(angle_rad), math.cos(angle_rad), 0]
    #]

    rot_mat_x = [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]]

    result = np.matmul(vec, rot_mat_x)

    return dot(result[0], result[1], 1)

if __name__ == "__main__":
    clear_terminal()
    # 8 vertices of a cube
    p1 = dot(100,20, 1)
    p2 = dot(140,20, 1)
    p3 = dot(100,40, 1)
    p4 = dot(140,40, 1)

    p5 = dot(130,10, 1)
    p6 = dot(170,10, 1)
    p7 = dot(130,30, 1)
    p8 = dot(170,30, 1)

    for r in range(0, 90):
        clear_terminal()
        angle = math.radians(r)
        p1_rot = rotate_x(trd_twod(p1),angle)
        p2_rot = rotate_x(trd_twod(p2),angle)
        p3_rot = rotate_x(trd_twod(p3),angle)
        p4_rot = rotate_x(trd_twod(p4),angle)
        #p1_rot.draw_dot()
        #p2_rot.draw_dot()

        p1_rot.draw_line(p2_rot)
        p3_rot.draw_line(p4_rot)
        
        p2_rot.draw_line(p4_rot)
        p3_rot.draw_line(p1_rot)
        time.sleep(0.01)
        
        #p2_rot.draw_line(p4_rot)
        #p3_rot.draw_line(p1_rot)
        #p4_rot.draw_line(p2_rot)


    #p1.draw_dot()
    #p2.draw_dot()
    #p3.draw_dot()
    #p4.draw_dot()





    #p5.draw_dot()
    #p6.draw_dot()
    #p7.draw_dot()
    #p8.draw_dot()

    #p1.draw_line(p2)
    #p1.draw_line(p3)
    #p2.draw_line(p4)
    #p4.draw_line(p3)




else:
    print("imported")
import os
import time
import math
import numpy as np

# x from 0 to 260, and y from 0 to 60,
# but setting the mid point on x,y plane to be origin (x = 0, y = 0)
X_MAX = 120
X_MIN = -120
Y_MAX = -30 # first row of terminal is at y = 0
Y_MIN = 30 # last row of terminal is at y = Y_MIN

X_OFFSET = 120
Y_OFFSET = 30

X_MID = 60
Y_MID = 15

THETA = math.radians(45)


DELAY = 0 # delay of drawing 

class dot: # x,y coordinate
    def __init__(self, x: int, y: int, z: int): 
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
        self.z = int(z)
        self.vec = [self.x, self.y, self.z] # vector form of a dot (point)
    
    def draw_dot(self):
        # ANSI escape code used. '\033' is the escape character in Python strings, 
        # which is equivalent to the ASCII value of the escape character.
        print(f"\033[{self.y + Y_OFFSET};{self.x + X_OFFSET}H", end="") # move the point to the appropriate position
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

def projection():
    proj = [
        [1, 0, 0],
        [0, 1, 0]
    ]

    return proj

def rotation_x(theta): # rotate on x-axis
    rot_mat_x = [
        [1, 0, 0],
        [0, math.cos(theta), -math.sin(theta)],
        [0, math.sin(theta), math.cos(theta)]]

    return rot_mat_x

def rotation_y(theta): # rotate on y-axis
    rot_mat_y = [
        [math.cos(theta), 0, math.sin(theta)],
        [0, 1, 0],
        [-math.sin(theta), 0, math.cos(theta)]
    ]

    return rot_mat_y

def rotation_z(theta): # rotate on z-aix
    rot_mat_z = [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0,1]
    ]

    return rot_mat_z

if __name__ == "__main__":
    clear_terminal()
    # 8 vertices of a cube
    p1 = dot(X_MID/3, Y_MID/3,1)
    p3 = dot(X_MID*2/3, Y_MID/3,1)
    p5 = dot(X_MID*2/3, Y_MID*2/3,1)
    p7 = dot(X_MID/3, Y_MID*2/3,1)

    p2 = dot(X_MID/3, Y_MID/3,1)
    p4 = dot(X_MID*2/3, Y_MID/3,1)
    p6 = dot(X_MID*2/3, Y_MID*2/3,1)
    p8 = dot(X_MID/3, Y_MID*2/3,1)

    for i in range (0, 100):
        vertices = [p1, p2, p3, p4, p5, p6, p7, p8]
        for r in range(0, 180):
            clear_terminal()
            theta = math.radians(r)
            for i in range(0, 3):
                #print(rotation_y(theta))
                #rotated = np.matmul(rotation_y(theta), vertices[i].vec)
                rotated = np.matmul(rotation_x(theta), vertices[i].vec)
                #rotated = np.matmul(rotation_z(theta), rotated)
                vertices[i] = dot(rotated[0], rotated[1], 1)
            
            theta = math.radians(180-r)
            for i in range(4, 7):
                rotated = np.matmul(rotation_x(theta), vertices[i].vec)
                #rotated = np.matmul(rotation_z(theta), rotated)
                vertices[i] = dot(rotated[0], rotated[1], 1)

            vertices[0].draw_line(vertices[1])
            vertices[1].draw_line(vertices[2])
            vertices[2].draw_line(vertices[3])
            vertices[3].draw_line(vertices[0])

            vertices[4].draw_line(vertices[5])
            vertices[5].draw_line(vertices[6])
            vertices[6].draw_line(vertices[7])
            vertices[7].draw_line(vertices[4])

            vertices[0].draw_line(vertices[4])
            vertices[1].draw_line(vertices[5])
            vertices[2].draw_line(vertices[6])
            vertices[3].draw_line(vertices[7])
            
            time.sleep(0.1)




else:
    print("imported")
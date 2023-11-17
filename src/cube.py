import os
import time
import math

X_MAX = 261
X_MIN = 0
Y_MAX = 0 # first row of terminal is at y = 0
Y_MIN = 60 # last row of terminal is at y = Y_MIN

X_MID = 120 # mid of x
Y_MID = 30  # mid of y

DELAY = 0.01 # delay of drawing 

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

        counter = 1

        # draw a line with y = a*x function or a horizontal line
        if x_diff != 0:
            for x in range(self.x, end_c.x, c_x):
                if slope > 0: # when diff of x,y both pos or neg. The line is in between top-left and bot-right
                    # case 1: when diff of x,y both pos, line going down from top-left to bot-right. As x increases, y increases (reaching towards bot of screen) 
                    # case 2: when diff of x,y both neg, line going up from bot-right to top-left. As x decreases, y decreases (reaching towards top of screen) 
                    y = self.y + round(slope*counter) 
                    counter+=1
                elif slope < 0: # if x_diff > 0, y_diff < 0, and vice versa. The line is in between top-right and bot-left
                    # case 1: when x_diff > 0, and y_diff < 0, line going up from bot-left to top-right. As x increases, y decreases (reaching towards top of screen)
                    # case 2: when x_diff < 0, and y_diff > 0, line going down from top-right to bot-left. As x decreases, y increases (reaching towards bot of screen)
                    y = self.y + round(slope*counter)
                    counter+=1
                else: # when slope is 0 
                    y = end_c.y
                print("x = " + str(x) + " y = " + str(y))
                coord = dot(x,y)
                #print("x = " + str(coord.x) + " y = " + str(coord.y))
                coord.draw_dot()
                time.sleep(DELAY)
        else: # draw a vertical line
            for y in range(self.y, end_c.y, c_y):
                coord = dot(end_c.x, y)
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
    # 8 vertices of a cube
    p1 = dot(100,20)
    p2 = dot(140,20)
    p3 = dot(100,40)
    p4 = dot(140,40)

    p5 = dot(130,10)
    p6 = dot(170,10)
    p7 = dot(130,30)
    p8 = dot(170,30)

    p1.draw_dot()
    p5.draw_dot()
    p1.draw_dot()
    p2.draw_dot()
    p3.draw_dot()
    p4.draw_dot()
    p5.draw_dot()
    p6.draw_dot()
    p7.draw_dot()
    p8.draw_dot()

    p1.draw_line(p2)
    p1.draw_line(p3)
    p2.draw_line(p4)
    p4.draw_line(p3)

    p5.draw_line(p6)
    p6.draw_line(p8)
    p8.draw_line(p7)
    p7.draw_line(p5)

    p1.draw_line(p5)
    p2.draw_line(p6)
    p3.draw_line(p7)
    p4.draw_line(p8)


else:
    print("imported")
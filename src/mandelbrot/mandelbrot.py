import os 

X_MAX = 240 # x = column
Y_MAX = 56 # y = row

X_POS_MAX = 120
Y_POS_MAX = 28

X_CENTER = 0.3001301496 # found this point on youtube
Y_CENTER = 0.025500022629245 # found this point on youtube

# clear terminal before display an ojbect on terminal
def clear_terminal():
    if os.name == 'posix': # Linux or macOS
        os.system('clear') # clears the terminal
    elif os.name == 'nt': # Windows
        os.system('cls') # clears the terminal
    else: 
        print("operating system: " + os.name)

def in_mandelbrot_set(x,y, max_iteration): # calculate if the point is in mandelbrot set
    # complex number takes (real, imag), so if x = 3, y =2, z0 = 3 + 2j, where j indicates imaginary number
    z0 = complex(x,y) 
    z = 0 # initial val of z

    for i in range(0, max_iteration):
        z = z**2 + z0
        if abs(z) > 2:
            return False
    return True 

def zoom(matrix, type, zoom_iter_max, max_iteration): # zoom in or out, or stay not zoomed, depending on type
    # type 0: no zoom
    # type >= 1: zoom out
    # type =< -1: zoom in
    zoom_iter = 0
    zoom_iter_max = abs(zoom_iter_max) # make sure to get zoom iteration ends

    if type == 0:
        zoom_iter = zoom_iter_max # render fractal just once
        scale = 1
        zoom_scale = 1
    if type >= 1:
        scale = 0.0001
        zoom_scale = 5
    if type <= -1:
        scale = 5
        zoom_scale = 2/3
        
    while(zoom_iter < zoom_iter_max):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # col - X_POS_MAX and row - Y_POS_MAX centers the image at the origin (0,0) in mathematical space
                # scaling factor scales x and y accordingly. e.g. to set x and y to range from (-2,2), set scaling factor to be 2.
                # e.g. when col = 260 (at max), then x = (260 - 130) / (130/2) = 130 / (130/2) = 130 * 2 / 130 = 2. 
                # need to center and zoom properly to see the patterns continuously
                x = (col - X_POS_MAX) * (scale/X_POS_MAX) + X_CENTER
                y = (row - Y_POS_MAX) * (scale/Y_POS_MAX) - Y_CENTER

                in_m_set = in_mandelbrot_set(x,y, max_iteration)
                if in_m_set:
                    matrix[row][col] = "."
                else:
                    matrix[row][col]= " "

        clear_terminal() # clear terminal before rendering

        # display mandelbrot fractal
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                print(matrix[row][col], end="")
            print() # for new line for every row
        
        zoom_iter += 1
        scale *= zoom_scale
    

if __name__ == "__main__":
    clear_terminal()
    matrix = [["."]*X_MAX for _ in range(Y_MAX)] # make a matrix with row = Y_MAX and col = X_MAX
    max_iteration = 1000
    
    zoom(matrix, -1, 500, max_iteration)
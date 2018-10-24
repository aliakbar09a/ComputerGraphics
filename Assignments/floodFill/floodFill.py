import math as m

# reading from input file
o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
xC = int(data[2].split()[-1])
yC = int(data[3].split()[-1])
length = int(data[4].split()[-1])
breadth = int(data[5].split()[-1])
o.close()

def draw_x(mat):
    for i in range(width):
        if mat[int(height/2)][i] == '10 ':
            mat[int(height/2)][i] = '50 '

def draw_y(mat):
    for i in range(height):
        if mat[i][int(width/2)] == '10 ':
            mat[i][int(width/2)] = '50 '

def mod(a):
    if a < 0:
        return -1*a
    return a
def shiftx(x):
    x = int(width/2 + x)
    return x
def shifty(y):
    y = int(height/2 - y)
    return y
def drawLine(mat, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if(mod(dx) > mod(dy)):
        steps = mod(dx)
    else:
        steps = mod(dy)
    xinc = float(dx) / float(steps)
    yinc = float(dy) / float(steps)

    for i in range(steps):
        x1 = x1 + xinc
        y1 = y1 + yinc
        mat[int(round(y1))][int(round(x1))] = '255 '

def plot_first_quad_Circle(mat, r, x_center, y_center,):
    x0, y0 = 0, r
    P = 1.25 - r
    x, y = x0, y0
    mat[shifty(yC+y+y_center)][shiftx(xC+x+x_center)] = '255 '
    mat[shifty(yC+x+y_center)][shiftx(xC+y+x_center)] = '255 '
    while (x <= y):
        if(P > 0):
            x = x + 1
            y = y - 1
            P = P + 2*x - 2*y + 1
        else:
            x = x + 1
            P = P + 2*x + 1
        mat[shifty(yC+y+y_center)][shiftx(xC+x+x_center)] = '255 '
        mat[shifty(yC+x+y_center)][shiftx(xC+y+x_center)] = '255 '
def plot_second_quad_Circle(mat, r, x_center, y_center,):
    x0, y0 = 0, r
    P = 1.25 - r
    x, y = x0, y0
    mat[shifty(yC+y+y_center)][shiftx(xC-x+x_center)] = '255 '
    mat[shifty(yC+x+y_center)][shiftx(xC-y+x_center)] = '255 '
    while (x <= y):
        if(P > 0):
            x = x + 1
            y = y - 1
            P = P + 2*x - 2*y + 1
        else:
            x = x + 1
            P = P + 2*x + 1
        mat[shifty(yC+y+y_center)][shiftx(xC-x+x_center)] = '255 '
        mat[shifty(yC+x+y_center)][shiftx(xC-y+x_center)] = '255 '
def plot_third_quad_Circle(mat, r, x_center, y_center,):
    x0, y0 = 0, r
    P = 1.25 - r
    x, y = x0, y0
    mat[shifty(yC-y+y_center)][shiftx(xC-x+x_center)] = '255 '
    mat[shifty(yC-x+y_center)][shiftx(xC-y+x_center)] = '255 '
    while (x <= y):
        if(P > 0):
            x = x + 1
            y = y - 1
            P = P + 2*x - 2*y + 1
        else:
            x = x + 1
            P = P + 2*x + 1
        mat[shifty(yC-y+y_center)][shiftx(xC-x+x_center)] = '255 '
        mat[shifty(yC-x+y_center)][shiftx(xC-y+x_center)] = '255 '
def plot_fourth_quad_Circle(mat, r, x_center, y_center,):
    x0, y0 = 0, r
    P = 1.25 - r
    x, y = x0, y0
    mat[shifty(yC-y+y_center)][shiftx(xC+x+x_center)] = '255 '
    mat[shifty(yC-x+y_center)][shiftx(xC+y+x_center)] = '255 '
    while (x <= y):
        if(P > 0):
            x = x + 1
            y = y - 1
            P = P + 2*x - 2*y + 1
        else:
            x = x + 1
            P = P + 2*x + 1
        mat[shifty(yC-y+y_center)][shiftx(xC+x+x_center)] = '255 '
        mat[shifty(yC-x+y_center)][shiftx(xC+y+x_center)] = '255 '

def floodFill(mat, x, y):
    if mat[y][x] == '10 ':
        mat[y][x] = '100 '
        floodFill(mat, x+1, y)
        floodFill(mat, x-1, y)
        floodFill(mat, x, y+1)
        floodFill(mat, x, y-1)

def writeToFile(mat):
    # opening the pgm file
    filename = 'hex.pgm'
    f = open(filename, 'w')
    # outputting the initial lines to pgm file
    first_four_lines = ['P2\n', str(width) + ' ' + str(height) + '\n', '255\n']
    f.writelines(first_four_lines)
    draw_x(mat)
    draw_y(mat)
    for i in range(height):
        f.writelines(mat[i])
        f.write('\n')

def main():
    mat = [['10 ' for i in range(width)] for j in range(height)]

    drawLine(mat, shiftx(xC - length/2), shifty(yC - breadth/2), shiftx(xC + length/2), shifty(yC - breadth/2))
    drawLine(mat, shiftx(xC - length/2), shifty(yC + breadth/2), shiftx(xC + length/2), shifty(yC + breadth/2))
    # drawing semi circles of left side of the design
    plot_second_quad_Circle(mat, breadth/4, -length/2, breadth/4)
    plot_third_quad_Circle(mat, breadth/4, -length/2, breadth/4)
    plot_first_quad_Circle(mat, breadth/4, -length/2, -breadth/4)
    plot_fourth_quad_Circle(mat, breadth/4, -length/2, -breadth/4)
    # drawing semi circles of right side of the design
    plot_second_quad_Circle(mat, breadth/4, length/2, -breadth/4)
    plot_third_quad_Circle(mat, breadth/4, length/2, -breadth/4)
    plot_first_quad_Circle(mat, breadth/4, length/2, breadth/4)
    plot_fourth_quad_Circle(mat, breadth/4, length/2, breadth/4)
    floodFill(mat, shiftx(xC), shifty(yC))
    writeToFile(mat)

# executing main()
main()

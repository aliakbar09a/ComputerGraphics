import math as m

# reading from input file
o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
xC = int(data[2].split()[-1])
yC = int(data[3].split()[-1])
a = int(data[4].split()[-1])
fi = float(data[5].split()[-1])
o.close()

fi = fi*(22.0/7.0)/180.0

def draw_x(mat):
    for i in range(width):
        mat[int(height/2)][i] = '50 '
def draw_y(mat):
    for i in range(height):
        mat[i][int(width/2)] = '50 '
# modulus function
def mod(a):
    if(a < 0):
        return -1*a;
    return a;
# function to get next point of hexagon
def rotate(x, y, theta):
    xh = int(round(x*m.cos(theta) - y*m.sin(theta)))
    yh = int(round(x*m.sin(theta) + y*m.cos(theta)))
    return xh, yh
# function to shift the hexagon points
def shift(x, y):
    x = int(width/2 + x)
    y = int(height/2 - y)
    return x, y
def drawLine(mat, x1, y1, x2, y2):
    dx = x2 - x1;
    dy = y2 - y1;
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

def main():
    mat = [['10 ' for i in range(width)] for j in range(height)]
    x, y = rotate(a, 0, fi)
    for i in range(6):
        theta = 22.0/21.0
        xh, yh = rotate(x, y, theta)
        # print(x, y, xh, yh, theta)
        xShift, yShift = shift(x + xC, y + yC)
        xhShift, yhShift = shift(xh + xC, yh +yC)
        drawLine(mat, xShift, yShift, xhShift, yhShift)
        x, y = xh, yh
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
# executing main()
main()

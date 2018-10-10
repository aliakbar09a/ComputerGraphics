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
o.close()

def draw_x(mat):
    for i in range(width):
        if mat[int(height/2)][i] == '10 ':
            mat[int(height/2)][i] = '50 '
def draw_y(mat):
    for i in range(height):
        if mat[i][int(width/2)] == '10 ':
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
def nchk(x):
    if x == '255 ':
        return False
    else:
        return True
def checkThreePixel(mat, j, i):
    found = 0
    if chk(mat[j][i-1]):
        found = found + 1
    if chk(mat[j][i]):
        found = found + 1
    if chk(mat[j][i+1]):
        found = found + 1
    return found
def chk(x):
    if x == '255 ':
        return True
    else:
        return False
def polyFill(mat):
    for j in range(height):
        points = []
        # boundary condition
        if chk(mat[j][0]) and nchk(mat[j][1]):
            points.append(0)
        for i in range(1, width-1):
            upper_found, lower_found = 0, 0
            if len(points)%2 == 0:
                if chk(mat[j][i]) and nchk(mat[j][i+1]):
                    # intersection point found
                    # now checking if it has to be counted once or twice
                    upper_found = checkThreePixel(mat, j-1, i)
                    lower_found = checkThreePixel(mat, j+1, i)
                    points.append(i)
                    if upper_found > 1 and lower_found == 0:
                        points.append(i)
                    if lower_found > 1 and upper_found == 0:
                        points.append(i)
            else:
                if chk(mat[j][i]) and nchk(mat[j][i-1]):
                    # intersection point found
                    # now checking if it has to be counted once or twice
                    upper_found = checkThreePixel(mat, j-1, i)
                    lower_found = checkThreePixel(mat, j+1, i)
                    points.append(i)
                    if upper_found > 1 and lower_found == 0:
                        points.append(i)
                    if lower_found > 1 and upper_found == 0:
                        points.append(i)
        if chk(mat[j][width-1]) and nchk(mat[j][width-2]):
            points.append(i)
        print(points)
        pair = 0
        while pair < len(points):
            for point in range(points[pair] + 1, points[pair+1]):
                mat[j][point] = '100 '
            pair = pair + 2

def main():
    mat = [['10 ' for i in range(width)] for j in range(height)]
    x, y = rotate(a, 0, 0)
    for i in range(6):
        theta = 22.0/21.0
        xh, yh = rotate(x, y, theta)
        xShift, yShift = shift(x + xC, y + yC)
        xhShift, yhShift     = shift(xh + xC, yh +yC)
        drawLine(mat, xShift, yShift, xhShift, yhShift)
        x, y = xh, yh
    polyFill(mat)
    writeToFile(mat)
# executing main()
main()

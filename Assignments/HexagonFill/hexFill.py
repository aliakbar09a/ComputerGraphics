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

fi = fi*(22.0/7)/180.0


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
        return -1*a
    return a
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
        len_points = 0
        i = 0
        while i < width:
            if chk(mat[j][i]):
                # for finding the first point of pair
                if len_points % 2 == 0:
                    while chk(mat[j][i+1]):
                        i = i + 1
                    upper_found = checkThreePixel(mat, j-1, i)
                    lower_found = checkThreePixel(mat, j+1, i)
                    if (upper_found == 2 and lower_found == 0) or (lower_found == 2 and upper_found == 0):
                        points.append(i)
                        points.append(i)
                    else:
                        pair1 = i
                        len_points = len_points + 1
                # the second point of pair
                else:
                    points.append(pair1)
                    points.append(i)
                    len_points = len_points + 1
            i = i + 1
        pair = 0
        while pair < len(points):
            for point in range(points[pair] + 1, points[pair+1]):
                mat[j][point] = '100 '
            pair = pair + 2


def main():
    mat = [['10 ' for i in range(width)] for j in range(height)]
    x, y = rotate(a, 0, fi)
    for i in range(6):
        theta = 22.0/21.0
        xh, yh = rotate(x, y, theta)
        xShift, yShift = shift(x + xC, y + yC)
        xhShift, yhShift = shift(xh + xC, yh + yC)
        drawLine(mat, xShift, yShift, xhShift, yhShift)
        x, y = xh, yh
    polyFill(mat)
    writeToFile(mat)    


# executing main()
main()

o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
r = int(data[2].split()[-1])
xC = int(data[3].split()[-1])
yC = int(data[4].split()[-1])
o.close()
# opening the pgm file
filename = 'circles.pgm'
f = open(filename, 'w')

# getting the 2d list
mat = [['0 ' for i in range(width)] for i in range(height)]

# outputting the initial four lines
first_four_lines = ['P2\n', '# This creates circle\n',
                    str(width) + ' ' + str(height) + '\n', '255\n']
f.writelines(first_four_lines)


# function to plot the points
def plotCircle(x, y, xC, yC):
    # full circle
    mat[xC + x][yC + y] = '255 '
    mat[xC + x][yC - y] = '255 '
    mat[xC - x][yC + y] = '255 '
    mat[xC - x][yC - y] = '255 '
    mat[xC + y][yC + x] = '255 '
    mat[xC - y][yC + x] = '255 '
    mat[xC + y][yC - x] = '255 '
    mat[xC - y][yC - x] = '255 '
    # lower semi circle
    mat[xC + x][yC + 2*r + y] = '255 '
    mat[xC + y][yC + 2*r + x] = '255 '
    mat[xC + x][yC + 2*r - y] = '255 '
    mat[xC + y][yC + 2*r - x] = '255 '
    # upper semi circle
    mat[xC - x][yC - 2*r + y] = '255 '
    mat[xC - y][yC - 2*r + x] = '255 '
    mat[xC - x][yC - 2*r - y] = '255 '
    mat[xC - y][yC - 2*r - x] = '255 '
# to plot the middle line
def plotLine(xc, yc, r):
    i = yc - 3*r
    while(i <= yc + (3*r)):
        mat[xc][i] = '255 '
        i = i + 1

x0, y0 = 0, r
P = 1.25 - r
x, y = x0, y0
plotCircle(x, y, xC, yC)
while (x <= y):
    if(P > 0):
        x = x + 1
        y = y - 1
        P = P + 2*x - 2*y + 1
    else:
        x = x + 1
        P = P + 2*x + 1
    plotCircle(x, y, xC, yC)
plotLine(xC, yC, r)
for i in range(height):
    f.writelines(mat[i])
    f.write('\n')
f.close()

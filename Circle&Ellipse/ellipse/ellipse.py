import math as m

o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
ry = int(data[2].split()[-1])
rx = int(data[3].split()[-1])
xC = int(data[4].split()[-1])
yC = int(data[5].split()[-1])
theta = float(data[6].split()[-1])
o.close()
print(theta)
# opening the pgm file
filename = 'ellipse.pgm'
f = open(filename, 'w')

# getting the 2d list
mat = [['0 ' for i in range(width)] for i in range(height)]

# outputting the initial four lines
first_four_lines = ['P2\n', '# This creates circle\n',
                    str(width) + ' ' + str(height) + '\n', '255\n']
f.writelines(first_four_lines)


def rox(x, y):
    x = int(x*m.cos(theta) - y*m.sin(theta))
    return x


def roy(x, y):
    y = int(x*m.sin(theta) + y*m.cos(theta))
    return y
# function to plot the points


def plotCircle(x, y, xC, yC):
    # full circle
    mat[xC + rox(x, y)][yC + roy(x, y)] = '255 '
    mat[xC + rox(x, -y)][yC + roy(x, -y)] = '255 '
    mat[xC + rox(-x, y)][yC + roy(-x, y)] = '255 '
    mat[xC + rox(-x, -y)][yC + roy(-x, -y)] = '255 '


theta = theta*22/(7*180)
print(theta)
# for region 1
x0, y0 = 0, ry
P = ry**2 + (rx**2)*(0.25 - ry)
x, y = x0, y0
plotCircle(x, y, xC, yC)
c, a = 2*(rx**2)*y0, 0
while ((ry**2)*x <= (rx**2)*y):
    if(P > 0):
        x = x + 1
        a = a + 2*(ry**2)
        y = y - 1
        c = c - 2*(rx**2)
        P = P + ry**2 + a - c
    else:
        x = x + 1
        a = a + 2*(ry**2)
        P = P + ry**2 + a
    plotCircle(x, y, xC, yC)
# for region 2
x0, y0 = rx, 0
P = rx**2 + (ry**2)*(0.25 - rx)
x, y = x0, y0
plotCircle(x, y, xC, yC)
c, a = 2*(ry**2)*x0, 0
while((ry**2)*x > (rx**2)*y):
    if(P > 0):
        y = y + 1
        a = a + 2*(rx**2)
        x = x - 1
        c = c - 2*(ry**2)
        P = P + rx**2 + a - c
    else:
        y = y + 1
        a = a + 2*(rx**2)
        P = P + rx**2 + a
    plotCircle(x, y, xC, yC)
for i in range(height):
    f.writelines(mat[i])
    f.write('\n')

f.close()

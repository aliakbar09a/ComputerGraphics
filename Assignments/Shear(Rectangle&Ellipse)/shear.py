o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
xC = int(data[2].split()[-1])
yC = int(data[3].split()[-1])
a = int(data[4].split()[-1])
b = int(data[5].split()[-1])
o.close()
# opening the pgm file
filename = 'shear.pgm'
f = open(filename, 'w')
# getting the 2d list for the window
mat = [['0 ' for i in range(width)] for j in range(height)]
# outputting the initial lines to pgm file
first_four_lines = ['P2\n', str(width) + ' ' + str(height) + '\n', '255\n']
f.writelines(first_four_lines)
# shear function
def shearx(x, y, shear):
    x = int(x + shear * y)
    return x
# shifting coordinates to center
def shift(x, y):
    x = int(width/2 + x)
    y = int(height/2 - y)
    return x, y
# modulus function
def mod(a):
    if(a < 0):
        return -1*a;
    return a;
# draw line function
def drawLine(x1, y1, x2, y2, shear):
    x1 = shearx(x1, y1, shear)
    x2 = shearx(x2, y2, shear)
    print(x1, y1,"  ", x2, y2)
    x2, y2 = shift(x2, y2)
    x1, y1 = shift(x1, y1)
    dx = x2 - x1;
    dy = y2 - y1;
    if(mod(dx) > mod(dy)):
        steps = mod(dx)
    else:
        steps = mod(dy)
    xinc = dx / steps
    yinc = dy / steps
    for i in range(steps):
        mat[y1][x1] = '255 '
        x1 = int(x1 + xinc)
        y1 = int(y1 + yinc)
drawLine(int(-a/2), int(b/2), int(a/2), int(b/2), 0.1)
drawLine(int(a/2), int(b/2), int(a/2), int(-b/2), 0.1)
drawLine(int(a/2), int(-b/2), int(-a/2), int(-b/2), 0.1)
drawLine(int(-a/2), int(-b/2), int(-a/2), int(b/2), 0.1)
for i in range(height):
    f.writelines(mat[i])
    f.write('\n')

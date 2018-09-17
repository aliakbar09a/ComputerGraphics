import math as m
# shear function
def shearx(x, y, shear):
    x = int(x + shear * y)
    return x, y
# shifting coordinates to center
def shift(x, y, height, width):
    x = int(width/2 + x)
    y = int(height/2 - y)
    return x, y
# modulus function
def mod(a):
    if(a < 0):
        return -1*a;
    return a;
# draw line function
def drawLine(mat, x1, y1, x2, y2, shear, height, width, center):
    x1, y1 = shearx(x1, y1, shear)
    x2, y2 = shearx(x2, y2, shear)
    x1, y1 = shift(x1 + center['xC'], y1 + center['yC'], height, width)
    x2, y2 = shift(x2 + center['yC'], y2 + center['yC'], height, width)
    dx = x2 - x1;
    dy = y2 - y1;
    if(mod(dx) > mod(dy)):
        steps = mod(dx)
    else:
        steps = mod(dy)
    xinc = dx / steps
    yinc = dy / steps
    for i in range(steps - 1):
        x1 = x1 + xinc
        y1 = y1 + yinc
        mat[round(y1)][round(x1)] = '255 '
# drawing ellipse
def plotEllipse(mat, x, y, xC, yC):
    mat[xC + rox(x, y)][yC + roy(x, y)] = '255 '
    mat[xC + rox(x, -y)][yC + roy(x, -y)] = '255 '
    mat[xC + rox(-x, y)][yC + roy(-x, y)] = '255 '
    mat[xC + rox(-x, -y)][yC + roy(-x, -y)] = '255 '
# rotation of x
def rox(x, y):
    theta = 3.14 / 2
    x = int(x*m.cos(theta) - y*m.sin(theta))
    return x

# rotation of y
def roy(x, y):
    theta = 3.14 / 2
    y = int(x*m.sin(theta) + y*m.cos(theta))
    return y
# ellipse drawing algorithm
def ellipseAlgo(mat, rx, ry, xC, yC ):
    x0, y0 = 0, ry
    P = ry**2 + (rx**2)*(0.25 - ry)
    x, y = x0, y0
    plotEllipse(mat, x, y, xC, yC)
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
        plotEllipse(mat, x, y, xC, yC)
    # for region 2
    x0, y0 = rx, 0
    P = rx**2 + (ry**2)*(0.25 - rx)
    x, y = x0, y0
    plotEllipse(mat, x, y, xC, yC)
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
        plotEllipse(mat, x, y, xC, yC)
def main():
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
    mat = [['10 ' for i in range(width)] for j in range(height)]
    # outputting the initial lines to pgm file
    first_four_lines = ['P2\n', str(width) + ' ' + str(height) + '\n', '255\n']
    f.writelines(first_four_lines)
    # dictionary of center
    center = {'xC':xC, 'yC':yC}
    # taking middle as the origin
    ysC, xsC = shift(center['xC'], center['yC'], height, width)
    # points to plot rectangle
    x, y = int(a/2), int(b/2)
    # drawing the shear rectangle
    drawLine(mat, -x, y, x, y, 0.5, height, width, center)
    drawLine(mat, x, y, x, -y, 0.5, height, width, center)
    drawLine(mat, x, -y, -x, -y, 0.5, height, width, center)
    drawLine(mat, -x, -y, -x, y, 0.5, height, width, center)
    # calling function to draw ellipse
    ellipseAlgo(mat, b/4, b/2, xsC, ysC)
    for i in range(height):
        f.writelines(mat[i])
        f.write('\n')

# executing main()
main()

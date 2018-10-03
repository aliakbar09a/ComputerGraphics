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
b = int(data[5].split()[-1])
o.close()

# modulus function
def mod(a):
    if(a < 0):
        return -1*a;
    return a;
# shear function
def shearx(x, y, shear):
    x = int(x + shear * y)
    return x, y
# shifting coordinates to center
def shift(x, y):
    x = int(width/2 + x)
    y = int(height/2 - y)
    return x, y
# shifting coordinates to center
def shift_refl(x, y):
    x = int(width/2 + x)
    y = int(height/2 + y)
    return x, y
# draw line function
def drawLine(mat, x1, y1, x2, y2, shear, reflection):
    x1, y1 = shearx(x1, y1, shear)
    x2, y2 = shearx(x2, y2, shear)
    # p, q, r, s = x1, y1, x2, y2
    if reflection == False:
        x1, y1 = shift(x1 + xC, y1 + yC)
        x2, y2 = shift(x2 + xC, y2 + yC)
    else:
        x1, y1 = shift_refl(x1 + xC, y1 + yC)
        x2, y2 = shift_refl(x2 + xC, y2 + yC)
    # x1, y1 = x1 + xC , y1 + yC
    # x2, y2 = x2 + yC, y2 + yC
    dx = x2 - x1;
    dy = y2 - y1;
    if(mod(dx) > mod(dy)):
        steps = mod(dx)
    else:
        steps = mod(dy)
    xinc = float(dx) / steps
    yinc = float(dy) / steps
    for i in range(steps - 1):
        x1 = x1 + xinc
        y1 = y1 + yinc
        mat[int(round(y1))][int(round(x1))] = '255 '
# drawing ellipse
def plotEllipse(mat, x, y, xC, yC):
    mat[yC + roy(x, y)][xC + rox(x, y)] = '255 '
    mat[yC + roy(x, -y)][xC + rox(x, -y)] = '255 '
    mat[yC + roy(-x, y)][xC + rox(-x, y)] = '255 '
    mat[yC + roy(-x, -y)][xC + rox(-x, -y)] = '255 '
def draw_x(mat):
    for i in range(width):
        mat[int(height/2)][i] = '100 '
# rotation of x
def rox(x, y):
    theta = 0
    x = int(x*m.cos(theta) - y*m.sin(theta))
    return x
# rotation of y
def roy(x, y):
    theta = 0
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
    # opening the pgm file
    filename = 'shear.pgm'
    f = open(filename, 'w')
    # getting the 2d list for the window
    mat = [['10 ' for i in range(width)] for j in range(height)]
    # outputting the initial lines to pgm file
    first_four_lines = ['P2\n', str(width) + ' ' + str(height) + '\n', '255\n']
    f.writelines(first_four_lines)
    # points to plot rectangle
    x, y = int(a/2), int(b/2)
    # draw x axis
    draw_x(mat)
    # drawing the shear rectangle
    drawLine(mat, -x, y, x, y, 0.5, False)
    drawLine(mat, x, y, x, -y, 0.5, False)
    drawLine(mat, x, -y, -x, -y, 0.5, False)
    drawLine(mat, -x, -y, -x, y, 0.5, False)
    # drawing the reflected shear rectangle
    drawLine(mat, -x, y, x, y, 0.5, True)
    drawLine(mat, x, y, x, -y, 0.5, True)
    drawLine(mat, x, -y, -x, -y, 0.5, True)
    drawLine(mat, -x, -y, -x, y, 0.5, True)
    # calling function to draw ellipse
    exC, eyC = shift(xC, yC)
    ellipseAlgo(mat, b/4, b/2, exC, eyC)
    # drawing reflection of ellipse
    exC_refl, eyC_refl = shift_refl(xC, yC)
    ellipseAlgo(mat, b/4, b/2, exC_refl, eyC_refl)
    for i in range(height):
        f.writelines(mat[i])
        f.write('\n')

# executing main()
main()

o = open('input.txt', 'r')
data = o.readlines()
# getting the required inputs
width = int(data[0].split()[-1])
height = int(data[1].split()[-1])
xC = int(data[2].split()[-1])
yC = int(data[3].split()[-1])
o.close()
# opening the pgm file
filename = 'circles.pgm'
f = open(filename, 'w')
# getting the 2d list for the window
mat = [['0 ' for i in range(width)] for j in range(height)]
# outputting the initial lines
first_four_lines = ['P2\n', str(width) + ' ' + str(height) + '\n', '255\n']
f.writelines(first_four_lines)

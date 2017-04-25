from display import *
from matrix import *
from math import *

def add_polygon(points, x0, y0, z0, x1, y1, z1, x2, y2, z2):
     #print "\n~~1~~" + str(x0) + ", " + str(y0) + ", " + str(z0) + """
      #    \n~~2~~""" + str(x1) + ", " + str(y1) + ", " + str(z1) + """
      #    "\n~~3~~""" + str(x2) + ", " + str(y2) + ", " + str(z2) + "\n"
    
    add_point(points, x0, y0, z0)
    add_point(points, x1, y1, z1)
    add_point(points, x2, y2, z2)


def draw_polygons(matrix, screen, color):
    if len(matrix) < 3:
        print 'Need at least 3 points to draw'
        return
    point = 0
    while point < len(matrix) - 2:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)
        
        draw_line( int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   int(matrix[point+2][0]),
                   int(matrix[point+2][1]),
                   screen, color)
        
        draw_line( int(matrix[point+2][0]),
                   int(matrix[point+2][1]),
                   int(matrix[point][0]),
                   int(matrix[point][1]),
                   screen, color)
        
        point+= 3

def add_box( points, x, y, z, width, height, depth ):
    #front half
    """
    add_polygon(points, x, y, z,
                x+width, y, z,
                x, y, z-depth)
    add_polygon(points, x+width, y, z-depth,
                x+width, y, z,
                x, y, z-depth)
    add_polygon(points, x, y, z,
                x+width, y, z,
                x, y-height, z)
    add_polygon(points, x+width, y-height, z,
                x+width, y, z,
                x, y-height, z)
    add_polygon(points, x, y, z,
                x, y-height, z,
                x, y, z-depth)
    add_polygon(points, x, y-height, z-depth,
                x, y, z-depth,
                x, y-height, z)
    #back half
    add_polygon(points, x+width, y-height, z-depth,
                x+width, y-height, z,
                x, y-height, z-depth)
    add_polygon(points, x, y-height, z,
                x+width, y-height, z,
                x, y-height, z-depth)
    add_polygon(points, x+width, y-height, z-depth,
                x+width, y, z-depth,
                x, y-height, z-depth)
    add_polygon(points, x, y, z-depth,
                x+width, y, z-depth,
                x, y-height, z-depth)
    add_polygon(points, x+width, y-height, z-depth,
                x+width, y-height, z,
                x+width, y, z-depth)
    
    add_polygon(points, x+width, y, z,
                x+width, y-height, z,
                x+width, y, z-depth)
    
    """
    
    add_polygon(points, 100, 100, 100,
                        20, 300, 100,
                        40, 100, 200)
    
    add_polygon(points, 20, 300, 100,
                        40, 100, 200,
                        100, 50, 300)
    
def add_spherical( points, cx, cy, cz, r, step):
    i = 0;
    matrix = generate_sphere(points, cx, cy, cz, r, step)
    while i < len(matrix) - 1:
        add_edge(points, matrix[i][0], matrix[i][1], matrix[i][2],
                         matrix[i][0]+2, matrix[i][1]+2, matrix[i][2])
        i += 1

   
def add_sphere( points, cx, cy, cz, r, step ):
    i = 0;
    matrix = generate_sphere(cx, cy, cz, r, step)
    while i < len(matrix)-2:
        add_polygon(points, matrix[i][0], matrix[i][1], matrix[i][2],
                         matrix[i+1][0], matrix[i+1][1], matrix[i+1][2],
                         matrix[i+2][0], matrix[i+2][1], matrix[i+2][2])
        i += 1
    
def generate_sphere(cx, cy, cz, r, step ):
    i = 0
    matrix = []
    while i < step:
        j = 0
        while j < step:
            theta = i * 2 * math.pi / step
            phi = j * math.pi / step
           # theta = j * math.pi / step
           # phi = i * 2 * math.pi / step
            #print "~~~~~~~~~~~~~~~~~~~~~~~~~~\ntheta=" + str(theta) + "phi=" + str(phi) + "\n"
            x = r * math.cos(theta) + cx
            y = r * math.sin(theta) * math.cos(phi) + cy
            z = r * math.sin(theta) * math.sin(phi) + cz
            matrix.append([x, y, z])
            j += 1
        i += 1
	#print len(matrix[len(matrix)-1])
    return matrix
        

def add_torus( points, cx, cy, cz, r0, r1, step ):
    i = 0;
    matrix = generate_torus(cx, cy, cz, r0, r1, step)
    while i < len(matrix):
        add_edge(points, matrix[i][0], matrix[i][1], matrix[i][2],
                 matrix[i][0]+1, matrix[i][1]+1, matrix[i][2]+1)
        i += 1

def generate_torus(cx, cy, cz, r0, r1, step ):
    i = 0
    matrix = []
    while i < step:
        j = 0
        while j < step:
            theta = i * 2 * math.pi / step
            phi = j * 2 * math.pi / step
            x = math.cos(theta) * (r0 * math.cos(phi) + r1) + cx
            y = r0 * math.sin(phi) + r1 + cy
            z = math.sin(theta) * (r0 * math.cos(phi) + r1) + cz
            matrix.append([x, y, z, 1])			
            j += 1
        i += 1
    return matrix

def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    t = 1

    while t <= step:
        x1 = r * math.cos(2*math.pi * t / step) + cx
        y1 = r * math.sin(2*math.pi * t / step) + cy

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        t+= 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    t = 1
    while t <= step:
        t = t / step
        x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]
                
        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        t = t * step
        t+= 1

def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print 'Need at least 2 points to draw'
        return
    
    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line

'''  what formulas:
    distance, pythagorean theorem,
    area of trapezoid,area of circle,
    midpoint.
    
'''

import math
import doctest
#doctest.testmod()

#
#if choice == 1:
#    x1= input("insert your first x coordinate:")
#    x2 = input("insert your second x coordinate:")
#    y1 = input("insert your first y coordinate:")
#    y2 = input("insert your second y coordinate:")
def distance(x1,x2,y1,y2):
        '''returns the distance between two points
        >>> distance(4,2,-5,6)
        11.18033988749895
        >>> distance(5,9,4,7)
        5
        >>> distance(10,15,6,12)
        7.810249675906654
        >>> distance(1,0.5,2,7.6)
        5.622277118748239
        >>> distance(-7,9,5,6.5)
        16.0701586799882
        '''
        a=x2-x1
        b= y2-y1
        c= a*a
        d= b*b
        e=c + d
        f=math.sqrt(e)
        return f
        
    
def area_trapezoid(b1,b2,h):
    '''returns the area of a trapezoid
    >>>area_trapezoid(4,6,5)
    25
    >>>area_trapezoid(7,8,10)
    75
    >>>area_trapezoid(11,2,3)
    19.5
    >>>area_trapezoid(-4,6,12)
    12
    >>>area_trapezoid(11,0.5,7.6)
    43.7
    '''
    b3 = b1+b2
    a= b3*h
    t= a/2
    return t
    
def area_circ(r):
    '''returns the area of a circle
    >>>area_circ(6)
    113.04
    >>>area_circ(-2)
    12.56
    >>>area_circ(11)
    379.94
    >>>area_circ(1.05)
    3.46185
    >>>area_circ(-8.9)
    248.7194
    '''
    r2= r**2
    r3 = r2*3.14
    return r3
    
def midpoint(x1,x2,y1,y2):
    '''returns the midpoint of a line
    >>>midpoint(4,10,6,8)
    (7,7)
    >>>midpoint(6,11,16,-4)
    (8.5,6)
    >>>midpoint(18,20,21,6)
    (19,13.5)
    >>>midpoint(11,0.5,6.5,8)
    (5.75, 7.25)
    >>>midpoint(16,2.6,100,-8)
    (9.3,46)
    '''
    x3= x1+x2
    y3= y1+y2
    x = x3/2
    y = y3/2
    print(f"({x},{y})")
    
def pythag_thrm(a,b):
    '''returns the length, or size, of the side of a triangle that is missing
    >>>pythag_thrm(10,2)
    c=10.19803902718557
    >>>pythag_thrm(5,7)
    c=8.602325267042627
    >>>pythag_thrm(-6,-8)
    c=10
    >>>pythag_thrm(4,7)
    c=8.062257748
    >>>pythag_thrm(-3.5,7.2)
    c=8.005623024
    '''
    a2=a**2
    b2=b**2
    a3=a2+b2
    a4= math.sqrt(a3)
    print(f"c= {a4}")
def run_dist():
    x1= int(input("Enter your first x coordinate: "))
    x2= int(input("Enter your second x coordinate: "))
    y1= int(input("Enter your first y coordinate: "))
    y2= int(input("Enter your second y coordinate: "))
    distance(x1,x2,y1,y2)
def main():
    choice=input("Choose a formula from these options:(1)distance, (2)area of a trapezoid, (3)area of a circle, (4)midpoint, or (5)pythag theorem:")
    if choice == "1":
        run_dist()
if __name__ == "__main__":
    main()
    
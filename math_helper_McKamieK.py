'''  what formulas:
    distance, pythagorean theorem,
    area of trapezoid,area of circle,
    midpoint.
    
'''

import math

#choice=input("Choose a formula from these options:(1)distance, (2)area of a trapezoid, (3)area of a circle, (4)midpoint, or (5)pythag theorem:")
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
    '''
    r2= r**2
    r3 = r2*3.14
    return r3
    
def midpoint(x1,x2,y1,y2):
    '''returns the midpoint of a line
    >>>midpoint(4,10,6,8)
    (7,7)
    >>>midpoint()
    
    >>>midpoint()
    '''
    x3= x1+x2
    y3= y1+y2
    x = x3/2
    y = y3/2
    print(f"({x},{y})")
    
def pythag_thrm(a,b):
    '''returns the length, or size, of the side of a triangle that is missing
    '''
    a2=a**2
    b2=b**2
    a3=a2+b2
    a4= math.sqrt(a3)
    return a4

#def main():
#    
#if __name__ == "__main__":
#    main()
    
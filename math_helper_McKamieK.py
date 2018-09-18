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
        '''
        a=x2-x1
        b= y2-y1
        c= a*a
        d= b*b
        e=c + d
        f=math.sqrt(e)
        return f
        
    
def area_trapezoid(b1,b2,h):
    '''gives area of a trapezoid
    '''
    b3 = b1+b2
    a= b3*h
    t= a//2
    return t
    
def area_circ(r):
    '''gives area of a circle
    '''
    r2= r**2
    r3 = r2*3.14
    return r3
    
def midpoint(x1,x2,y1,y2):
    '''gives the midpoint of a line
    '''
    x3= x1+x2
    y3= y1+y2
    x = x3/2
    y = y3/2
    print(f"({x},{y})")
    
def pythag_thrm(a,b):
    '''gives the length, or size, of the side of a triangle that is missing
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
    
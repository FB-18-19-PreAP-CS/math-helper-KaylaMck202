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
        11.18
        
        >>> distance(5,9,4,7)
        5.0
        
        >>> distance(10,15,6,12)
        7.81
        
        >>> distance(1,0.5,2,7.6)
        5.62
        
        >>> distance(-7,9,5,6.5)
        16.07
        '''
        a=x2-x1
        b= y2-y1
        c= a*a
        d= b*b
        e=c + d
        f=math.sqrt(e)
        return(round(f,2))
        
    
def area_trapezoid(b1,b2,h):
    '''returns the area of a trapezoid

     >>> area_trapezoid(4,6,5)
     25.0
     
     >>> area_trapezoid(7,8,10)
     75.0
     
     >>> area_trapezoid(11,2,3)
     19.5
     
     >>> area_trapezoid(-4,6,12)
     12.0
     
     >>> area_trapezoid(11,0.5,7.6)
     43.7
    '''
    b3 = b1+b2
    a= b3*h
    t= a/2
    return(round(t,1))
    
def area_circ(r):
    '''returns the area of a circle

    >>> area_circ(6)
    113.04
    
    >>> area_circ(-2)
    12.56
    
    >>> area_circ(11)
    379.94
    
    >>> area_circ(1.05) 
    3.46185
    
    >>> area_circ(-8.9)
    248.7194
    '''
    r2= r**2
    r3 = r2*3.14
    return(round(r3,5))
    
def midpoint(x1,x2,y1,y2):
    '''returns the midpoint of a line

    >>> midpoint(4,10,6,8)
    (7.0, 7.0)
    
    >>> midpoint(6,11,16,-4)
    (8.5, 6.0)
    
    >>> midpoint(18,20,21,6)
    (19.0, 13.5)
    
    >>> midpoint(11,0.5,6.5,8)
    (5.75, 7.25)
    
    >>> midpoint(16,2.6,100,-8)
    (9.3, 46.0)
    '''
    x3= x1+x2
    y3= y1+y2
    x = x3/2
    y = y3/2
    return x,y
    #print(f"({x},{y})")
    
def pythag_thrm(a,b):
    '''returns the length, or size, of the side of a triangle that is missing

    >>> pythag_thrm(10,2)
    10.2
    
    >>> pythag_thrm(5,7)
    8.6
    
    >>> pythag_thrm(-6,-8)
    10.0
    
    >>> pythag_thrm(4,7)
    8.06
    
    >>> pythag_thrm(-3.5,7.2)
    8.01
    '''
    a2=a**2
    b2=b**2
    a3=a2+b2
    a4= math.sqrt(a3)
    return(round(a4,2))
    #print(f"c= {a4}")
def run_dist():
    print("You selected distance.")
    x1= int(input("Enter your first x coordinate: "))
    x2= int(input("Enter your second x coordinate: "))
    y1= int(input("Enter your first y coordinate: "))
    y2= int(input("Enter your second y coordinate: "))
    print("The distance is {}".format(distance(x1,x2,y1,y2)))
     
def run_trap():
    print("You selected area of a trapezoid.")
    b1= int(input("Enter the first base: "))
    b2= int(input("Enter the second base: "))
    h= int(input("Enter the height: "))
    print("The area of the trapezoid is {}".format(area_trapezoid(b1,b2,h)))
    
def run_circ():
    print("You selected area of a circle.")
    r= int(input("Enter the radius: "))
    print("The area of the circle is {}".format(area_circ(r)))
    
def run_mid():
    print("You selected midpoint.")
    x1= int(input("Enter your first x coordinate: "))
    x2= int(input("Enter your second x coordinate: "))
    y1= int(input("Enter your first y coordinate: "))
    y2= int(input("Enter your second y coordinate: "))
    print("The midpoint is {}".format(midpoint(x1,x2,y1,y2)))

def run_pythag():
    print("You selected pythagorean Theorem.")
    a= int(input("Enter the first side of a triangle: "))
    b= int(input("Enter the second side of a triangle: "))
    print("The missing length is {}".format(pythag_thrm(a,b)))
    
def main():
    while True:
        choice=input("Choose a formula from these options:(1)distance, (2)area of a trapezoid, (3)area of a circle, (4)midpoint, or (5)pythag theorem:")
        if choice == "1":
            run_dist()
        elif choice == "2":
            run_trap()
        elif choice == "3":
            run_circ()
        elif choice == "4":
            run_mid()
        elif choice == "5":
            run_pythag()
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
    
'''  what formulas:
    distance, pythagorean theorem,
    area of trapezoid,area of circle,
    midpoint.
    
'''

import math

choice=input("Choose a formula from these options:(1)distance, (2)area of a trapezoid, (3)area of a circle, (4)midpoint, or (5)pythag theorem:")
if choice == 1:
    x1= input("insert your first x coordinate:")
    def distance(x1,x2,y1,y2):
            '''should give the distance between two points
            '''
            a=x2-x1
            b= y2-y1
            c= a*a
            d= b*b
            e=c + d
            f=math.sqrt(e)
            return f
        
    
def area_trapezoid(b1,b2,h):
    ''
    pass
    
def area_circ(r):
    pass
def midpoint(x1,x2,y1,y2):
    pass
def pythag_thrm(a,b,c):
    pass

#def main():
#    
#if __name__ == "__main__":
#    main()
    
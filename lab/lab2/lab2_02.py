# 3.2 checking if the traingle can be formed and if yes, calculating perimeter and area

#importing necessary modules
from math import sqrt


a = float(input('Enter side a of triangle: '))
b = float(input('Enter side b of triangle: '))
c = float(input('Enter side c of triangle: '))


if (a+b)>c and (b+c)>a and (c+a)>b:
    perimeter = a+b+c
    s = perimeter/2
    area = sqrt(s*(s-a)*(s-b)*(s-c)) 
    print(f"The area and perimeter of the given triangle are {area} and {perimeter} respectively")
else:
    print(f"The area and perimeter of triangles cannot be calculated as the sides of triangles fulfills the Triangle Inequality Theorem.")
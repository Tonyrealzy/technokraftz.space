#finding the area of circle

from math import pi
r = int(input("Enter radius: "))
A = pi * r *r
print("Area = " + str(A))
print("The area of the circle is", A)

#to round up the result to n decimal places
#we use round(int, n)
a = round(A, 2)
print("Area = " + str(a))
print("The area of the circle is", a)

#taking only the integer
print("Area = " + str(int(A)))
print("The area of the circle is", int(A))
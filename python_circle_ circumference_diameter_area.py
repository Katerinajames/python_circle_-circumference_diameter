import math
print("Calculation of diameter and circumference")

radius=float(input("Enter the radius of our circle\n"))
diameter=2*radius
print("Our diameter is",diameter)
print("-----------------------------------")
circumference =2*math.pi*radius
print("Our circumference  is",circumference)
print("-----------------------------------")
area = math.pi*math.pow(radius ,2)
print("Our area is",area)

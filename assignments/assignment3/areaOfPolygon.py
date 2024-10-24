import math

number_of_sides = int(input("\nInput the number of sides on the polygon: "))
length_of_side = int(input("\nInput the length of one of the sides: "))
π = 3.14159265
area_of_polygon = (number_of_sides * length_of_side ** 2) / (4 * math.tan(π / number_of_sides))

print(f"\nThe area is: {area_of_polygon}")

import math

print("\nInput the  coordinates of two points [(x1,y1) & (x2,y2)]: ")
x1 = float(input("\nInput the latitude of coordinate 1, x1: "))
y1 = float(input("Input the longitude of coordinate 1, y1: "))

x2 = float(input("\nInput the latitude of coordinate 2, x2: "))
y2 = float(input("Input the longitude of coordinate 2, y2: "))

x1 = math.radians(x1)
y1 = math.radians(y1)

x2 = math.radians(x2)
y2 = math.radians(y2)


RADIUS_OF_THE_EARTH = 6371.01 
distance_between_both_points =  6371.01 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print(f"\nThe distance between those points is: {distance_between_both_points} km")

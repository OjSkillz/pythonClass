import math

print("\nEnter the coefficients a, b and c of the quadratic equation: ")
a = float(input("\na: "))
b = float(input("\nb: "))
c = float(input("\nc: "))

DETERMINANT = math.pow(b, 2) - (4 * a * c)
        
if (a != 0):
    if (DETERMINANT > 0):
        firstRoot = (-b + math.pow(DETERMINANT, 0.5)) / (2 * a)
        secondRoot = (-b - math.pow(DETERMINANT, 0.5)) / (2 * a)
        print(f"\nThe roots are {firstRoot} and {secondRoot}")
            
    elif (DETERMINANT < 0):
        realRoot = -b  / (2 * a)
        imaginaryRoot = (math.pow(-DETERMINANT, 0.5)) / (2 * a)
        print(f"\nThe roots are {realRoot}i and {imaginaryRoot}j")       
          
    else:
        sameRoot = -b  / (2 * a)
        print(f"\nThe roots are same: {sameRoot}")
else: 
    print("You have entered an invalid input for a")
   

# BMI Calculator 

weight_in_Kg = float(input("\nEnter your weight in Kilograms: "))

height_in_meters = float(input("\nEnter your height in meters: "))

EXPONENT_CONSTANT = 2

bmi = weight_in_Kg / (height_in_meters ** 2)

print(f"\nYour Body Mass Index (BMI) is {bmi:.2f}")

print(f"\nCheck your BMI category using the data below: ")

print("\n\tBMI Category\tValues")
print("\n\tUnderweight\t<18.5\n")
print("\tNormal Weight\t18.5-24.9\n")
print("\tOverweight\t25-29.9\n")
print("\tObesity\t\t30 and above\n")

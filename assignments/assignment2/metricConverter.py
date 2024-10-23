# Metric Conversion

number_in_feet = float(input("\nEnter a value for feet: "))

CONVERSION_CONSTANT = 0.305

number_in_meters = number_in_feet * CONVERSION_CONSTANT

print(f"\n{number_in_feet} feet is {number_in_meters: .4f} meters")


total_miles = 0
total_gallons = 0
total_miles_gallon = 0
gallons  = float(input("Enter the gallons used (-1 to end) : "))
miles = float(input("Enter the miles driven: "))

while gallons != -1:
    
    miles_gallon = miles / gallons
    total_miles += miles
    total_gallons += gallons
    total_miles_gallon = total_miles / total_gallons
    print(f"The miles/gallon for this tank was {miles_gallon}")
    gallons  = float(input("Enter the gallons used (-1 to end) : "))
    if gallons == -1: break
    miles = float(input("Enter the miles driven: "))

print(f"The overall average miles/gallon was {total_miles_gallon}")

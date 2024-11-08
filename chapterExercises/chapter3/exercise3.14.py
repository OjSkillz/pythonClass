number_of_terms = int(input("\nEnter number of terms for approximation of π: "))

PI_CONSTANT = 4
count = 1
divisor = 1
divisor_two = 3
approximation = 0

while count  <= number_of_terms: 
    π = (PI_CONSTANT / divisor) - (PI_CONSTANT / divisor_two)
    
   
    divisor += 4
    divisor_two += 4
    approximation += π
    count +=  1
print(f"\nπ approximated by {number_of_terms} is {approximation}")

# Number of Positives, Negatives and Zeros Checker

number_counter = 1
positives_counter = 0
negatives_counter = 0
zeros_counter = 0

while number_counter <= 5 :
	print(f"Enter number {number_counter}: ")
	number = float(input( ))
	number_counter += 1
		
	if number == 0 :
		zeros_counter += 1
	if number > 0 : 
		positives_counter += 1
	if number < 0 :
		negatives_counter += 1

print(f"\nThe number of negative numbers input is/are {negatives_counter}")
print(f"\nThe number of positive numbers input is/are {positives_counter}")
print(f"\nThe number of zeros input is/are {zeros_counter}")
	

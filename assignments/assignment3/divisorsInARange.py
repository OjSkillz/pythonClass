print("""\nWelcome, you can check the number of integers within a given range x..y that are divisible by any given value "p" """)
first_number = int(input("""\nEnter first number "x": """))
second_number = int(input("""\nEnter second number "y": """))
divisor = int(input("""\nEnter a value "p": """))

integer_count = 0
integer = 0

for integer in range(first_number, second_number):
	if integer % divisor == 0 :
		integer_count += 1

print(f"\n{integer_count} integers are divisible by {divisor} within the range {first_number}..{second_number}")

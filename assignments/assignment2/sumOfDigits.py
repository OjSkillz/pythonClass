# Sum the digits in an integer

initial_integer = int(input("\nEnter an integer between 0 and 1000: "))

last_digit = initial_integer % 10 

next_integer = initial_integer // 10 

middle_digit = next_integer % 10

first_digit = next_integer // 10

sum_of_all_digits = first_digit + middle_digit + last_digit

print(f"\nThe sum of all the digits of {initial_integer} is {sum_of_all_digits}")

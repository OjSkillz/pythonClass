# Palidrome Integer

users_integer = int(input("\nEnter a three-digit integer: "))

last_digit = users_integer % 10

new_integer = users_integer // 10

middle_digit = new_integer % 10

first_digit = new_integer // 10

if first_digit == last_digit :
	print(f"\n{users_integer} is a palindrome")
	
else:
	print(f"\n{users_integer} is not a palindrome")




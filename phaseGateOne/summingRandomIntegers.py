"""
Pseudocode for summing random integers

Generate two random integers not greater than 100
Prompt user to enter the sum of both integers
If user's input is same as the sum of both integers:
	print "True"
else:
	print "False"
"""
import random
integer_one = int(random.random() * 100)
integer_two = int(random.random() * 100)

user_response = int(input(f"what is the sum of {integer_one} and {integer_two} ? >>  "))

if user_response == integer_one + integer_two:
    print(True)
else :
    print(False)

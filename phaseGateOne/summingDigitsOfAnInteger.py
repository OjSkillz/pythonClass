"""
Pseudocode for summing the digits of an integer

Prompt user to enter an integer between 0 and 1000
while the user's input is not within the stated range:
    print an error message
    prompt the user to give another input
Else:
    Cast the user input to a string type
    create an empty list to store the characters in the string
    extract the characters of the string and add them to the empty list
    Sum the elements of the list
    Cast the result back to an integer type
    Display the result as the sum of the digits in the integer
"""
print()
user_input = int(input("Enter any integer between 0 and 1000 to find the sum of its digits >>  "))
while user_input < 1 or user_input >= 1000:
    print("Invalid input! Enter an integer between 0 and 1000")
    print()
    user_input = int(input("Enter any integer between 0 and 1000 to find the sum of its digits >>  "))
user_input_to_string = str(user_input)
user_input_to_sum = []
result = 0
for character in user_input_to_string:
    user_input_to_sum.append(character)
for element in user_input_to_sum: 
    result += int(element)

print(f"The sum of the digits in {user_input} is {result}")

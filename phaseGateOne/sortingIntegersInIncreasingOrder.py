""" Pseudocode for sorting integers in increasing order
initialize an index counter
Create an empty list "numbers" to store user input
Create another empty list "sorted_list" to store sorted user input

Prompt user to enter three integers
Store the three numbers in "numbers"
Sort the three numbers in increasing order
Add all the elements in "numbers" to "sorted_list"
Display the elements of the sorted list in increasing order
"""
index = 0
numbers = []
sorted_list = []
for index in range(3):
    print()
    number = int(input(f"Enter number {index + 1} >> "))
    numbers.append(number)

sorted_list.extend(sorted(numbers))
print()
print(f"{sorted_list[0]},{sorted_list[1]},{sorted_list[2]}")



    


""" Pseudocode for sorting integers in increasing order

Prompt user to enter three integers
Store the three numbers in an empty list
Sort the three numbers in increasing order
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



    


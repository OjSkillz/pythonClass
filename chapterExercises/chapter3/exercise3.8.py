
number = int(input("Enter a number: "))
counter = 0
sum = 0
product = 1
average = 0
largest = number
smallest = number

for number in range(1, 4):
    number = int(input(f"Enter another number: "))
    sum += number
    product *= number
    counter += 1
    average = sum / counter

    if number > largest:
        largest = number
    elif number < smallest and number < largest:
        smallest = number
print(f"Sum is: {sum}\nAverage is: {average:.2f}\nProduct is: {product}\nLargest number is: {largest}\nSmallest number is: {smallest}")

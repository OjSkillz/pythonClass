
integer = int(input("\nEnter any non-negative integer n to compute the factorial, n!: "))

count = 0
factorial = 1
while count < integer :
    factor = integer - count
    count += 1
    factorial = factorial * factor
print(f"\n{integer}! = {factorial}")

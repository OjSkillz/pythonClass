userInput = int(input("Enter a number: "))

for count in range(1, userInput + 1):
    for number in range(1, count+1):
        print(number, end='')
    print()
for count in range(userInput, 1, -1):
    for number in range(1, count):
        print(number, end='')
    print()
    

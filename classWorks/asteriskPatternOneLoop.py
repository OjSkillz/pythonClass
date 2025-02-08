userInput = int(input("Enter any number of choice:  "))

y = "*" * userInput
while userInput >= 1 and y >= "*": 
    print(y)
    y = y-y
    userInput += -1


    

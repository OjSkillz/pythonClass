userInput = int(input("Enter any number of choice for multiplication up to 10 times: "))

count = 0
for count in range(1, 11):
    print(f"{userInput} x {count} = {userInput * count}")
    count += 1
    print()
    

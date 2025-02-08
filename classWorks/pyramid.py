number_of_lines = int(input("Enter an integer between 1 and 13 to display a pyramid: "))

for count in range(number_of_lines + 1 , 1, -1):
    for number in range(count, number_of_lines + 1):    
        print(number, end='')
    print()

   

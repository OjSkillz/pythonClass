print(f"(a)")

for asterisk in range(0,11,1):
    for asterisks in range(0, asterisk+1):
        print("*", end="")
    print()
print(end="")
print(f"(b)")
for number in range(11,1,-1):
    for number_two in range(number, 1 , -1):
        print("*", end="")
    print()
 
print("(c)")
for x in range(1, 11):
    for space in range(x -1):
        print(" ", end="")
    for column in range (x, 11):
      print("*", end = "")
    print()
    
    
print("(d)")
for column in range(1, 11):
    for space in range(10, column, -1):
        print(" ",end="")
    for row in range(column):
            print("*", end="")
    print()
        
    

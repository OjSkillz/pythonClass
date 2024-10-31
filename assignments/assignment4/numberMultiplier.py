
print("\nInput a number and a level to generate a corresponding multiplication table: ")

number = int(input("\nNumber: "))
level = int(input("Level: "))

for level in range(1, level+1):
    print(f"{number}  x  {level}  =  {number * level}")

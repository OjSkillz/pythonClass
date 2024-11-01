import math

repeat = "yes"

while repeat.lower() == "yes":

    first_number = float(input("\nEnter first number: "))
    second_number = float(input("\nEnter second number: "))
    third_number = float(input("\nEnter third number: "))

    greatest_number = max(first_number, second_number, third_number)
    smallest_number = min(first_number, second_number, third_number)

    if first_number == greatest_number and third_number == smallest_number:
        print("\nNumbers are in decreasing order ⏬")
    
    elif first_number == smallest_number and third_number == greatest_number:
        print("\nNumbers are in increasing order ⏫")
    
    else : 
        print("\nNumbers are neither decreasing nor increasing in order")

    repeat = input("""\nDo you want to go again? Enter "yes" or "no": """)
print("\nThanks and bye 👋")

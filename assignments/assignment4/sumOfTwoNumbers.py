
response = "yes"
while response.lower() == "yes":

    firstNumber= int(input("\nEnter first number: "))

    secondNumber = int(input("\nEnter second number: "))

    sum = firstNumber + secondNumber
      
    print(f"\nThe sum of {firstNumber} and {secondNumber} is {sum}")

    print("\nDo you wish to perform the operation once again?")
    response = input("\nType Yes or No: ")
    
print(f"\nGoodbye 👋")

    

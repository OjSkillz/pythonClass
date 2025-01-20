#Write a function sum_of_even_numbers that takes an integer n and returns the sum of all even numbers from 1 to n

def sum_of_even_numbers(integer: int):
    sum_of_even_numbers = 0
    for number in range(1, integer+1):
        if number % 2 == 0:
            sum_of_even_numbers += number
    return sum_of_even_numbers
    
userInput = int(input("Enter any integer n:  "))

print(f"The sum of even numbers between 1 to n is {sum_of_even_numbers(userInput)}")

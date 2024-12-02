"""
Pseudocode for application to perform and grade subtraction operations

intialize a score counter "score" at 0
initialize a question counter at 0
Generate random subtraction problems
    *Make sure minuend(first number) is greater than subtrahend(second number)
Record the start time
While displaying each problem sequentially up to 10 problems
    Prompt user to enter their answers
    If user's answer per problem is correct
        increment "score" by 1 
At the end of the exercise, record the end time
Calculate the total time taken to answer all questions in seconds

Diaplay the final value of score and the total time taken in seconds
"""

from datetime import datetime
import random

score = 0

def generate_random_number():
    number = int(random.random() * 10)
    return number
    
random_numbers = []
sorted_random_numbers = []
for count in range(1,11):
    for index in range(2):
        random_numbers.append(generate_random_number())
    sorted_random_numbers.extend(sorted(random_numbers))
    user_answer = int(input(f"Question {count}. What is the result of {sorted_random_numbers[1]} - {sorted_random_numbers[0]} ? >> "))
    if user_answer == sorted_random_numbers[1] - sorted_random_numbers[0]:
        score += 1
print(f"Your score at the end of this exercise is {score}/10")

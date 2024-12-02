"""
Pseudocode for predicting future days

Create a dictionary to hold weekdays as keys and their corresponding values 
Prompt user to enter an integer for today's day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6)
Prompt user to enter the number of days after today to predict the future day
Add the number of days elapsed to the integer for today's day
while the result is greater than 7,
    subtract 7 from the result 
When the result is between 1 and 6 :
    set the future day to the key that holds a value corresponding to that result
if the result is equal to 7, 
    set the future day to the key holding the same value as the integer for today's day
"""
weekdays = {"Sunday" : 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

today_integer = int(input("Enter today's day >> "))
days_elapsed = int(input("Enter the number of days elapsed since today >> "))

result = today_integer + days_elapsed
if result <= 6:
    for key, value in weekdays.items():
        if result == value:
            print(f"The future day is {key}")
elif result == 7:
    for key, value in weekdays.items():
        if today_integer == value: 
            print(f"The future day is {key}")

elif result > 7 :
    while result > 7:
        result = result - 7
    for key, value in weekdays.items():
        if result == value: 
            print(f"The future day is {key}")
 
    
    
    
    

# exercise2.15.py

"""Sorting numbers in ascending order irrespective of duplication or order scrambling"""

first_number = float(input("\nEnter a floating-point/decimal number: "))

second_number = float(input("Enter a second floating-point/decimal number: "))

third_number = float(input("Enter a third floating-point/decimal number: "))

lowest_number = min(first_number, second_number, third_number)
highest_number = max(first_number, second_number, third_number)
middle_number = 0

if first_number != lowest_number and first_number != highest_number:
   middle_number = first_number 
   
if second_number != lowest_number and second_number != highest_number:
   middle_number = second_number

if third_number != lowest_number and third_number !=  highest_number:
   middle_number = third_number
   
if first_number == second_number and first_number != highest_number:
   middle_number = first_number = second_number

if first_number == second_number and first_number == highest_number:
   middle_number = first_number = second_number
   
if first_number == third_number and first_number != highest_number:
   middle_number = first_number = third_number

if first_number == third_number and first_number == highest_number:
   middle_number = first_number = third_number

if second_number == third_number and second_number != highest_number:
   middle_number = second_number = third_number

if second_number == third_number and second_number == highest_number:
   middle_number = second_number = third_number
       
if first_number == second_number == third_number :
   middle_number = lowest_number = highest_number

print(lowest_number, middle_number, highest_number)



   


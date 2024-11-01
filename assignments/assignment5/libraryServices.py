number_of_days_late = int(input("Enter number of days late: "))

if number_of_days_late <= 30:
    if number_of_days_late <= 5: 
        print("Your fine is 50 paise.")
   
    elif number_of_days_late > 5 and number_of_days_late <= 10:
        print("Your fine is 1 rupee.")
    
    elif number_of_days_late > 10:
        print("Your fine is 5 rupees.")
        
else : print ("Too late...Your membership is cancelled")

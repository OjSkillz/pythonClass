
userInput = int(input("\nEnter a number from 1 - 7 to" + 
  " check the weekday it corresponds to: "))

if (userInput % 7 == 0) :
 print(f"\n {userInput} is a Sunday")
  
elif (userInput % 7 == 1) :
 print(f"\n {userInput} is a Monday")
    
elif (userInput % 7 == 2) :
 print(f"\n {userInput} is a Tuesday")

elif (userInput % 7 == 3) :
 print(f"\n {userInput} is a Wednesday")
      
elif (userInput % 7 == 4) :
 print(f"\n {userInput} is a Thursday")
         
elif (userInput % 7 == 5) :
 print(f"\n {userInput} is a Friday")
        
elif (userInput % 7 == 6) :
 print(f"\n {userInput} is a Saturday")

import random 
 
random_number = random.randint(1, 1000)

print("\nGuess my number between 1 and 1000")

user_guess = 0

while user_guess != random_number :
    user_guess = int(input("Your guess?  ")) 

    if user_guess > random_number :
        print("\nToo high, try again!🤪")
    
    elif user_guess < random_number :
        print("\nToo low, try again!😝")
     
    else :
        print("\nCongratulations. You guessed the number!🤩")


    

import random 
 
random_number = random.randint(1, 1000)

print("\nGuess my number between 1 and 1000")
user_guess = 0
user_guess_count = 0
while user_guess != random_number :
    user_guess = int(input("Your guess?  ")) 

    if user_guess > random_number :
        print("\nToo high, try again!🤪")
    
    elif user_guess < random_number :
        print("\nToo low, try again!😝")
        
    else :
        print("\nCongratulations. You guessed the number!🤩")
        if user_guess_count <= 10: 
            print("\nEither you know the secret or you got lucky!")
        else : print("\nYou should be able to do better!")    
    user_guess_count += 1


    

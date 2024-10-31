import random 
 
randomNumber = random.randint(0, 20)

print("\nCan you guess a lucky number between 0 and 20?")

while True :
    print("\nEnter your guess: ")

    userGuess = int(input()) 

    if userGuess > randomNumber :
        print("\nToo high, try again!🤪")
    
    elif userGuess < randomNumber :
        print("\nToo low, try again!😝")
     
    else :
        print("\nCongratulations, you have guessed the lucky number right!🤩")
        break

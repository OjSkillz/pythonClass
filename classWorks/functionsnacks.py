
vowels =  "AEIOU"

def get_vowels (string: str) :
    count = 0
    for vowel in vowels:
        for character in string:
            if  character.lower() == vowel.lower():
                count += 1
    return count

userInput = input("Enter a string of words:  ")
print(get_vowels(userInput))
    
    
    
    # Write a function that takes a string and returns the number of vowels in the string.
       # Example "python is sweet" Output: 4

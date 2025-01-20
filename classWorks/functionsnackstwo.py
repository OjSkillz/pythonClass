def get_acronym(string: str) :
        count = ""
        for character in string:
            if character == character.upper():
                count += character.upper()
        return count

userInput = input("Enter a string of words:  ")
print(get_acronym(userInput))
    
    
    
    # Write a function that takes a string and returns the number of vowels in the string.
       # Example "python is sweet" Output: 4

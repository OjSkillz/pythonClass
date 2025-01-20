#Write a function count_occurrences that takes a character and a string as input and returns how many times that character appears in the string (using a loop)
#example e, elephant >> 2


def count_occurrences(character, string):
    character_counter = 0
    while len(character) == 1:
        for member in string:
            if member.lower() == character.lower():
                character_counter += 1
        return character_counter
    return "provide a single character" 
        
print("\nProvide a character and a string in the form (character, string): ")

character = input("\ncharacter: ")
string = input("\nstring: ")

print(f"number of occurrences of {character} in {string} is {count_occurrences(character, string)}")
            
    

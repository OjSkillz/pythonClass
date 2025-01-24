#PSEUDOCODE FOR ENCRYPTION FUNCTION
#Pass string to the function

#The function should iterate through the string, checking for characters that are alphabets

#If any character is an alphabet, the character is replaced by the character value of that character's unicode value moved 13 places further

#If the character's unicode value is between 97 and 122 and
# the sum of the character's unicode and 13 is greater than 122, subtract double the movement(13 * 2 = 26) from that sum to get the unicode value for the encrypt character

#If the character's unicode value is between 65 and 90, and the sum of that value and 13 is greater than 90, subtract double the movement(13 * 2 = 26)
# from that sum to get the unicode value for the encrypt character





def encrypt_text(string):
    characters = []
    try :
        for char in string:
            if char.isalpha():
                characters.append(chr(get_encrypt_value(char)))
            else:
                characters.append(char)
    except TypeError:
        print("object is not a string")

    return "".join(characters)


def get_encrypt_value(char):
    encrypted = ord(char) + 13
    if char.isalpha() and 97 <= ord(char) <= 122 < ord(char) + 13:
        encrypted -= 26
    elif char.isalpha() and 65 <= ord(char) <= 90 < ord(char) + 13:
        encrypted -= 26

    return encrypted



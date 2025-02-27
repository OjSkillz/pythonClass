def rearrange(string):
    upper_string = [character for character in string if character.isupper()]
    lower_string =[character for character in string if character.islower()]
    return "".join(upper_string + lower_string)
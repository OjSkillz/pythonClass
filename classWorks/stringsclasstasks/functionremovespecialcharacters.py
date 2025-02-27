def remove_special_characters(string):
    for character in string:
        if not character.isalpha():
            string = string.replace(character, "")
    return string
def get_character_frequency(string):
    character_frequency = {}
    for character in string:
        character_frequency[character] = string.count(character)
    return character_frequency
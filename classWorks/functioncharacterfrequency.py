def get_character_frequency(string):
    character_frequencies = {}
    for character in string:
        character_frequencies[character] = string.count(character)
    return character_frequencies
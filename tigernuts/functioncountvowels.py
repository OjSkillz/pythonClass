def get_vowel_count(string)-> int:
    count = 0
    vowels = ["a", "e","i","o","u"]
    for vowel in vowels:
        for characters in string:
            if characters.lower() == vowel:
                count += 1
    return count

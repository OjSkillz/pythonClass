def check_anagram_status(string_1, string_2)-> bool:
    counter = 0
    count = 0
    for character_1 in string_1:
        for character_2 in string_2:
            while count < len(string_2):
                if character_1 == character_2:
                    counter += 1
                count += 1
        if count == len(string_2) and count == len(string_1):
            return True 
        else:
            return False

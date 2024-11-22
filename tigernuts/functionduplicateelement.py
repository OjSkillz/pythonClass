def check_duplicate(_list: list)-> bool:
    count = 0
    for index in range(1, len(_list)):
        if sorted(_list)[index] == sorted(_list)[index - 1]:
            count += 1
    if count >= 1:
        return True
    else: 
        return False
        

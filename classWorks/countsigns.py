def count_signs(numbers: list) :
    positive = 0
    negative = 0
    for number in numbers:
        if number >= 0 : positive += 1
        else : negative += 1
    return f"Positive : {positive} \nNegative : {negative}" 
    


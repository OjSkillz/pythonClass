def sum_digits(integer):
    extracted = []
    total = 0
    for count in range(len(str(integer))):
        extracted.append(str(integer)[count : count+1])  
        total += int(extracted[count])
    return total

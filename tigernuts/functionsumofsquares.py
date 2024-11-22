def sum_squares(numbers:list)->int:
    total = 0
    for number in numbers:
        total += (number * number)
    return total

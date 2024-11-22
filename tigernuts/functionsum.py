def get_sum(numbers:list):
    total = 0
    for even_number in numbers:
        if even_number % 2 == 0:
            total += even_number
    return total

def print_odd_elements(numbers:list)->list:
    odd_elements = []
    for number in numbers:
        if number % 2 > 0:
            odd_elements.append(number)
    return odd_elements

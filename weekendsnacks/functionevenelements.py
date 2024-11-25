def print_even_elements(numbers:list)->list:
    even_elements = []
    for number in numbers:
        if number % 2 == 0:
            even_elements.append(number)
    return even_elements

def print_even_elements(numbers:list)->list:
    even_elements = [number for number in numbers if number % 2 == 0]
    return even_elements

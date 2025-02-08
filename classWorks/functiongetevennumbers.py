def get_even_numbers(string) :
    return [int(x) for x in string if x.isdigit() and int(x) % 2 == 0 ]

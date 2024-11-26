def is_prime_number(integer)->bool:
    if integer == 2:
        return True
    for number in range(2, integer):
        if integer % number != 0:
            return True
        return False

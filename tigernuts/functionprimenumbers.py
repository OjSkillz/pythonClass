def check_prime_status(integer: int)->bool:
    for count in range(2, integer):
        if integer % count != 0:
            return True
        else:
            return False

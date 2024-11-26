def is_palindrome(integer)->bool:
    reverse = str(integer)[: : -1]
    if integer == int(reverse):
        return True
    return False

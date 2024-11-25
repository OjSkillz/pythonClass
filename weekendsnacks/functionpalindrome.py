def check_palindrome(string)->bool:
    reverse = string[: : -1]
    if string == reverse:
        return True
    else:
        return False

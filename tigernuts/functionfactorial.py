def get_factorial(integer):
    factorial = 1
    for count in range(integer):
        factorial *= (integer - count)
    return factorial

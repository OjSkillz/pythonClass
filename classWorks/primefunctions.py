
number = int(input("Enter a number: "))
def get_prime(number):
    for values in range(2, number):
        if number % values == 0: 
            return False
    return True
print(get_prime(number))

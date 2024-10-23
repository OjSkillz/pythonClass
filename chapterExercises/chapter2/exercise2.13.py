# exercise2.13
"""Finding out how big Python integers can be."""

base = int(input("Enter an integer: "))
exponent = int(input("Enter a very large exponent: "))
number = base ** exponent 

print(base, "^" , exponent,"=",number)

# test values: 
# 1. base; 35 exponent; 100 - Valid
# 2. base; 100 exponent; 500 - Valid
# 3. base; 1000 exponent; 1000 - Valid
# 4. base; 1000 exponent; 250000 - ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
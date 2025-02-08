def sum_of_multiples(integer1, integer2):
    sum_of_multiples = 0
    for multiples in range(integer1, integer2 + 1):
        if multiples % integer1 == 0:
            sum_of_multiples += multiples
    return sum_of_multiples

print("\nEnter two integers x and n to find the sum of multiples of x from x to n: ")
first_integer = int(input("\nx: "))
second_integer = int(input("\nn: "))

print(f"The sum of multiples of {first_integer} from {first_integer} to {second_integer} is {sum_of_multiples(first_integer, second_integer)}")

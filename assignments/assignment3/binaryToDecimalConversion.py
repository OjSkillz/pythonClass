integer = bytes(input('\nEnter a binary number: '), encoding='utf8')
decimal_integer = int(integer, 2)
print(f'\nDecimal number is: {decimal_integer}')

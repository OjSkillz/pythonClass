#2.11 Separating the digits in an integer

integer = int(input('Enter a 5-digit integer: '))

lastDigit = integer % 10

integer2 = integer // 100

thirdDigit = integer2 % 10

firstDigit = integer2 // 100

integer3 = integer2 % 100

secondDigit = integer3 // 10

integer4 = integer % 100

fourthDigit = integer4 // 10

print("\n", firstDigit, "   ", secondDigit, "   ",  thirdDigit, "   ", fourthDigit, "   ", lastDigit)
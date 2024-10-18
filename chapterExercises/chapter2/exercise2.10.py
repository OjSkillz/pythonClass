#2.10 Arithmetic, Smallest and Largest

integer1 = int(input('\nEnter first integer: '))

integer2 = int(input('\nEnter second integer: '))

integer3 = int(input('\nEnter third integer: '))

sum = integer1 + integer2 + integer3

average = sum / 3

product = integer1 * integer2 * integer3

smallest = integer1

if integer2 < integer1 :
   smallest = integer2

if integer3 < integer1 :
   smallest = integer3

largest = integer3

if integer1 > integer3 :
   largest = integer1

if integer2 > integer3 :
   largest = integer2 


print('\nThe sum of all three integers is', sum)
print('\nThe average of all three integers is', average)
print('\nThe product of all three integers is', product)
print('\nThe smallest of all three integers is', smallest)
print('\nThe largest of all three integers is', largest)
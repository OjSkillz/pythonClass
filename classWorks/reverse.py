number = int(input("Enter three digit number: "))

digit_three = number % 10 
number_one = number // 10
digit_two = number_one % 10
digit_one = number_one // 10

print(number,"in reverse is", digit_three, digit_two, digit_one)

even = 0
odd = 0

if (digit_three%2 == 0 ) : even += 1
else : odd += 1
if (digit_two%2 == 0 ) : even += 1
else : odd += 1
if (digit_one%2 == 0 ) : even += 1
else : odd += 1

print("Number of even digits =", even )
print("Number of odd digits =", odd)


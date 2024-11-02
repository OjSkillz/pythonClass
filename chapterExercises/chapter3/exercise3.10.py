

principal = 1000

annual_return_rate = 7/100

for number_of_years in range(1, 31):

    amount_on_deposit = principal * ((1 + annual_return_rate) ** number_of_years)


    print(f"The amount on deposit at the end of year {number_of_years} is \t${amount_on_deposit:>.2f} ")



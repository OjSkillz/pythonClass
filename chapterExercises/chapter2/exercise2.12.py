#2.12 

principal = 1000

annual_return_rate = 7/100

amount_on_deposit_10 = principal * ((1 + annual_return_rate) ** 10)
amount_on_deposit_20 = principal * ((1 + annual_return_rate) ** 20)
amount_on_deposit_30 = principal * ((1 + annual_return_rate) ** 30)

print('The amount on deposit at the end of the 10th, 20th and 30th years are','$', round(amount_on_deposit_10, 2),x`'$',round(amount_on_deposit_20, 2), 'and', '$',round(amount_on_deposit_30, 2))



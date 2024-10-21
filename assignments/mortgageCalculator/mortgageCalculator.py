principal = int(input("\nEnter the principal amount: "))

annual_rate = int(input("Enter the annual interest rate: "))

duration = int(input("Enter the duration in years: "))

percent_monthly_rate = annual_rate / (100 * 12)

monthly_duration = duration * 12

monthly_payment_numerator = percent_monthly_rate * ((1 + percent_monthly_rate) ** monthly_duration)

monthly_payment_denominator = (((1 + percent_monthly_rate) ** (monthly_duration) - 1))

monthly_payment = principal * (monthly_payment_numerator / 						monthly_payment_denominator)

print("Your monthly payment is $", round(monthly_payment, 2))



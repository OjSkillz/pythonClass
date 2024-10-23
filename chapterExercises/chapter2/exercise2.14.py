# exercise2.14.py
"""Calculating Target Heart-Rate."""

users_age = int(input("\nEnter your age: "))

max_heart_rate = 220 - users_age

lower_range_value = (50/100) * max_heart_rate

upper_range_value = (85/100) * max_heart_rate

print('Your maximum heart rate is:', max_heart_rate, 'beats per minute\n')

print('Your target heart rate range is',lower_range_value,'-',round(upper_range_value, 1),'beats per minute')
 
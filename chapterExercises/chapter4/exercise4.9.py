def convert_temperature(celsius):
    return (9 / 5) * celsius + 32


print(f"Celsius{'Fareinheit' :>13}")
for celsius_temperatures in range(101):
    print(f"{celsius_temperatures: >7}{convert_temperature(celsius_temperatures) :>13.1f}")

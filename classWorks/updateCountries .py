def update_countries(country, state, city_one, city_two, population_one, population_two):
    countries = {
    "USA" : {"California" : {"Los Angeles" : 40000000, "San Francisco" : 870000}},
    "Canada" : {"Ontario" : {"Toronto": 2930000, "Ottawa": 994837}},
    }
    cities = [city_one, city_two]
    populations = [population_one, population_two]
    cities_and_populations = {}
    
    for key, value in zip(cities, populations):
        cities_and_populations[key] = value
    state_and_cities = {state: cities_and_populations}
    update = {country : state_and_cities}
    for key,value in update.items():
        countries[country] = state_and_cities
    return f'Countries = {countries}'
    
country = input("Enter Country :  ")
state  = input("Enter State: ")
city_one = input("Enter first city: ")
pop_one = int(input(f"Enter population for {city_one}: "))
city_two = input("Enter second city: ")
pop_two = int(input(f"Enter population for {city_two}: "))


print(update_countries(country,state, city_one, city_two, pop_one, pop_two))

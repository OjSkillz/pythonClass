def get_population(country, state):
    countries = {
     "Canada" : {"Ontario" : {"Toronto": 2930000, "Ottawa": 994837}},
    "Usa" : {"California" : {"Los Angeles" : 40000000, "San Francisco" : 870000}},
   
    }
    citiesPopulation = ""
    try:
        for cities in countries[country.title()].values():
            for key,value in cities.items():
                if(validate_entries(country, state) == False):
                    break
                else: 
                    citiesPopulation += f'{key}: {value}\n'
    except KeyError :
        print("Invalid entry. Try again later")

    return citiesPopulation

def validate_entries(country, state):
    countries = {
     "Canada" : {"Ontario" : {"Toronto": 2930000, "Ottawa": 994837}},
    "Usa" : {"California" : {"Los Angeles" : 40000000, "San Francisco" : 870000}},
    }
    check = 0
    for keys,values in countries.items():
        for key, value in values.items():
            if (country.title() == keys and key != state.title()) or (country.title() != keys and key == state.title()) :
                check+= 1
            elif (country.title() != keys and key == state.title()) or (country.title() == keys and key != state.title()):
                check += 1
    if check > 1:
        for key,value in countries[country.title()].items():
            right_state = key
        if country.title() == "Usa":
            country = "USA"
        else: country = country.title()
        print(f"Invalid Pair. Did you mean {country} and {right_state}? ")
        return False

        return True

country = input("Enter Country :  ")
state  = input("Enter State: ")
print(get_population(country, state))


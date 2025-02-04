def convertListToDictionary(numbers: list) :
    my_dict = {}
    for element in sorted(numbers) :
        my_dict[element] = numbers.count(element)
    return my_dict

elements = [2,2,1,3,5,5]
print(convertListToDictionary(elements))

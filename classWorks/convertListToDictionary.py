def convertListToDictionary(numbers: list) :
    return {element:numbers.count(element) for element in sorted(numbers)}

elements = [2,2,1,3,5,5]
print(convertListToDictionary(elements))

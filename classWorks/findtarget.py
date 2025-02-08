def find_target(numbers : list, target) :
    if target in numbers :
        return numbers.index(target)
    else :
        return "not found"

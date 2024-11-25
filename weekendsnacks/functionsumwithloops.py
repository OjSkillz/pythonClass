def sum_lists_with_for_loop(numbers:list):
    total = 0
    for number in numbers:
        total += number
    return total

def sum_lists_with_while_loop(numbers:list):
    total = 0
    count = 0
    while count < len(numbers):
        total += numbers[count]
        count += 1
    return total

def sum_lists_with_loops(numbers:list):
    sum_list = []
    sum_lists_with_for_loop(numbers)
    sum_lists_with_while_loop(numbers)
    sum_list.append(sum_lists_with_for_loop(numbers))
    sum_list.append(sum_lists_with_while_loop(numbers))
    return sum_list
    


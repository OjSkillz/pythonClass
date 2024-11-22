def get_total_sum(numbers: list)->int:
    new_list = []
    for counter in range(0, len(numbers)):
        new_sum = sum(numbers) - numbers[counter]
        new_list.append(new_sum)
    return sum(new_list)
        

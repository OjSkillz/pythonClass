def get_running_totals(numbers:list)->list:
    running_totals = []
    running_totals.append(numbers[0])
    for index in range(1, len(numbers)):
        running_totals.append(numbers[index] + running_totals[index -1])
    return running_totals

def factor_of(integer) -> int:
    count = 0
    for number in range(1,integer+1):
        if integer % number == 0:
            count += 1
    return count

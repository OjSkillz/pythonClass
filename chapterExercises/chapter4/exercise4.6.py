def average(arg, *args):
    return sum(args, arg)  / (len(args) + 1)

print(average (1, 2, 3, 4, 5))
print(average())

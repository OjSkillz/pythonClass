

print(f"number\tsquare\tcube")
for number in range(0,6):
    square = number ** 2
    cube = number ** 3
    print(f"{number:>6}{square:>8}{cube:>6}")
    

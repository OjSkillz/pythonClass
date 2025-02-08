
count = 0
success = 0
failure = 0

for count in range(15):
    grade = int(input("Enter grade:  ")) 
    count += 1

    if grade >= 45: 
        success += 1
    elif grade < 45:
        failure += 1

print(f"Number of Passes: {success}\nNumber of Failures: {failure}")

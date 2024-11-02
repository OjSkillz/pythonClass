first_test = input("What is your problem?")
second_test = input("Have you had this problem before (yes or no)? ")
if second_test.lower() == "yes":
    print("Well, you have it again.")
elif second_test.lower() == "no":
    print("Well, you have it now.")
else:
    print("Invalid response")

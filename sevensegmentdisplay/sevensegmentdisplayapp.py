from sevensegmentdisplay import display_output_for
print("\nWelcome to the Seven-Segment Display Application")

def menu():
    try :
        display_code = input("Enter 8-digit display code: ")
        print(f"Here is the Seven-Segment display of input code:\n{display_output_for(display_code)}")
    except ValueError as error:
        print(f"\n{error}")
        menu()
    except TypeError as error:
        print(f"\n{error}")
        menu()

menu()
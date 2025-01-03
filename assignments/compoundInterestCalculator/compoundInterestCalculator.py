from compoundInterest import CompoundInterest


def display_fields() :
    print("\nStep 1: Initial Investment\nInitial Investment * ")
    initial_investment = float(input('Amount of money that you have available to invest initially >>> '))
    compound_interest.set_principal(initial_investment)

    print("\nStep 2: Contribute\nMonthly Contribution")
    monthly_contribution = float(input("Amount that you plan to add to the principal every month, or a negative\nnumber for  the amount that you plan to withdraw every month,\nor 0 for neither deposit nor withdrawal >>> "))
    compound_interest.set_monthly_contribution(monthly_contribution)
    
    print("\nLength of Time In Years *")
    duration = int(input("Length of time, in years, that you plan to save >>> "))
    compound_interest.set_duration(duration)
    
    print("\nStep 3: Interest Rate\nEstimated Interest Rate * ")
    interest_rate =float(input("Your estimated annual interest rate in %  >>> "))
    compound_interest.set_interest_rate(interest_rate)
    
    print("\nStep 4: Compound It\nCompound Frequency\n")
    frequency = int(input("""Times per year that interest will be compounded : 1️⃣ Daily
    \t\t\t\t\t\t  2️⃣ Monthly
    \t\t\t\t\t\t  3️⃣ Quarterly
    \t\t\t\t\t\t  4️⃣ Semi-Annually
    \t\t\t\t\t\t  5️⃣ Annually
    \t\t\t\t\t\t  >>>\t"""))
    compound_interest.set_frequency(frequency)
        
compound_interest = CompoundInterest(0.0, 0, 0.0, 0.0, 1)
print("Determine how much your money can grow using the power of compound interest.\n\n* DENOTES A REQUIRED FIELD")

display_fields()

print("All Entries Sucessfully Recorded.")
choice = int(input(""" 
      \nReady to calculate your compound interest?  1️⃣ CALCULATE
      \t\t\t\t\t    2️⃣ RESET
      \t\t\t\t\t    >>>\t"""))
    
match choice :
    case 1: 
        compound_interest.get_future_value
      
    case 2: 
        print("All Entries Cleared. Ready To Go Again? \n")
        display_fields()

    case _ : print("Invalid Selection! Try again later...")



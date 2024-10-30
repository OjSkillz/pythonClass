  
    
for counter in range(0, 3, 1) :
    name = input("\nName: ")
    earning = float(input("\nEarnings in USD: "))  
    
    if (earning <= 30000) :
        tax = (15 / 100) * earning;
        print(f"\nDear {name}, your total tax is ${tax}")
    
    if (earning > 30000) :
        tax = (20 / 100) * earning;
        print(f"\nDear {name}, your total tax is ${tax}")
         

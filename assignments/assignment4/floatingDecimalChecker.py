   
print("\nEnter two floating-point numbers up to three decimal places")

firstNumber = float(input("\nFirst number: "))
secondNumber = float(input("\nSecond number: "))    
    
firstNumberQuotient = (int(firstNumber))
secondNumberQuotient = (int(secondNumber))
    
firstNumberRemainder = firstNumber - firstNumberQuotient
secondNumberRemainder = secondNumber - secondNumberQuotient
    
if firstNumberQuotient == secondNumberQuotient and firstNumberRemainder == secondNumberRemainder :
    print("\nBoth numbers are same")
else :
    print("\nBoth numbers are different")
    

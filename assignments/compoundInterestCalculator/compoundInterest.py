from decimal import Decimal 

class CompoundInterest :
    def __init__(self, principal, duration, interest_rate, monthly_contribution, frequency) :
        self.__principal = principal
        self.__duration = duration
        self.__interest_rate = interest_rate
        self.__monthly_contribution = monthly_contribution
        self.__frequency = frequency
        self.PERCENTAGE = 1.0 / 100
        self.MONTHS = 12
        self.QUARTERS = 4
        self.HALF_YEAR = 2
        self.DAYS = 365
    
    
    def set_principal(self, initial_investment) :
        while (initial_investment < 0.0) :
            print("\nInvalid entry! Enter a value greater than 0")
            initial_investment = Decimal(input('Amount of money that you have available to invest initially >>> '))
        self.__principal = initial_investment
    
 
    def set_duration(self, years) :
        while (years < 0 ) :
            print("\nInvalid entry! Year must be greater than 0")
            duration = int(input("Length of time, in years, that you plan to save >>> "))
        self.__duration = years
    

    def set_interest_rate(self, rate) :
        while (rate < 0.0) :
            print("\nInvalid entry! Enter a value greater than 0")
            initial_investment = float(input('Your estimated annual interest rate in %   >>>  '))
        self.__interest_rate = rate
    
 
    def set_monthly_contribution(self, monthly_contribution): 
        self.__monthly_contribution = monthly_contribution
        
  
    def set_frequency (self, frequency) :
        match frequency :
            case 1: self.__frequency = self.DAYS 
       
            case 2: self.__frequency = self.MONTHS

            case 3: self.__frequency = self.QUARTERS
      
            case 4: self.__frequency = self.HALF_YEAR
   
            case 5: self.__frequency = 1
            
            case _ : 
            
                print("Invalid Selection! Try again...\n")
            
                frequency = int(input("""Times per year that interest will be compounded : 1️⃣ Daily
                \t\t\t\t\t\t 2️⃣ Monthly
                \t\t\t\t\t\t 3️⃣ Quarterly
                \t\t\t\t\t\t 4️⃣ Semi-Annually
                \t\t\t\t\t\t 5️⃣ Annually
                \t\t\t\t\t\t  >>>\t """))

                set_frequency(frequency)
    @property
    def get_principal(self) :
        return self.__principal
        
    @property
    def get_interest_rate(self) :
        return self.__interest_rate
    
    @property
    def get_duration(self) :
        return self.__duration
    
    @property
    def get_monthly_contribution(self) :
        return self.__monthly_contribution
     
    @property
    def get_frequency(self) :
        return self.__frequency
    
    @property
    def get_future_value(self) :
        rate_per_frequency = (self.get_interest_rate * self.PERCENTAGE) / self.get_frequency
        
        frequency_by_duration = self.get_frequency * self.get_duration
        
        recurring_factor = (1 + rate_per_frequency ) ** frequency_by_duration
        
        future_value = ( self.get_principal * recurring_factor ) + ( self.get_monthly_contribution *  
        ( (recurring_factor - 1) / rate_per_frequency ) ) 
        
        print(f"\n          The Results Are In\nIn {self.get_duration} years, you will have #{future_value :,.2f} ")
        
    
    

 


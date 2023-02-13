class RentalProperty:
    properties = []

    def __init__(self, rental_income, taxes, insurance, utilities, HOA, lawn, vacancy, repairs, cap_x, property_management, mortgage, down_payment, closing_cost, repair_budget, miscellaneous):
        self.rental_income = float(rental_income)
        self.taxes = float(taxes)
        self.insurance = float(insurance)
        self.utilities = float(utilities)
        self.HOA = float(HOA)
        self.lawn = float(lawn)
        self.vacancy = float(vacancy)
        self.repairs = float(repairs)
        self.cap_x = float(cap_x)
        self.property_management = float(property_management)
        self.mortgage = float(mortgage)
        self.down_payment = float(down_payment)
        self.closing_cost = float(closing_cost)
        self.repair_budget = float(repair_budget)
        self.miscellaneous = float(miscellaneous)
        
    def cash_flow(self):
        return self.rental_income - (self.taxes + self.insurance + self.utilities + self.HOA + self.lawn + self.vacancy + self.repairs + self.cap_x + self.property_management + self.mortgage)
    
    def cash_on_cash_return(self):
        total_investment = self.down_payment + self.closing_cost + self.repair_budget + self.miscellaneous
        annual_cash_flow = self.cash_flow() * 12
        return (annual_cash_flow / total_investment) * 100
    
    def show_properties(cls):
        if cls.properties:
            for i, prop in enumerate(cls.properties):
                print(f"{i+1}. Rental Income: {prop.rental_income}, Taxes: {prop.taxes}, Insurance: {prop.insurance}, Utilities: {prop.utilities}")
        else:
            print("No properties added yet")

    def delete_property(cls, index):
        try:
            del cls.properties[index - 1]
            print(f"Property {index} deleted successfully")
        except IndexError:
            print(f"Invalid index, no property found with index {index}")

property = RentalProperty(
    rental_income= input('Enter Rental Income:'), 
    taxes=input('Enter Taxes: '), 
    insurance=input('Enter Insurance: '), 
    utilities=input('Enter Utilities: '), 
    HOA=input('Enter HOA fees: '), 
    lawn=input('Enter lawn cost:'), 
    vacancy=input('Enter Vacancy: '), 
    repairs=input('Enter repairs: '), 
    cap_x=input('Enter Cap_X: '), 
    property_management=input('Enter Property Management cost:'), 
    mortgage=input('Enter Mortgage: '), 
    down_payment=input('Enter DownPayment: '), 
    closing_cost=input('Enter Closing Cost:'), 
    repair_budget=input('Enter Repair Budget: '), 
    miscellaneous=input('Enter Miscellaneous Expenses: ')
)

print("Cash Flow: $", format(property.cash_flow(), '.2f'))
print("Cash on Cash Return: %", format(property.cash_on_cash_return(), '.2f'))

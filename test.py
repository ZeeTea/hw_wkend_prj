class RentalProperty:
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
        def add_property(self, rental_income, taxes, insurance, utilities, HOA, lawn, vacancy, repairs, cap_x, property_management, mortgage, down_payment, closing_cost, repair_budget, miscellaneous):
            property = RentalProperty(rental_income, taxes, insurance, utilities, HOA, lawn, vacancy, repairs, cap_x, property_management, mortgage, down_payment, closing_cost, repair_budget, miscellaneous)
            self.properties.append(property)

        def show_properties(self):
            for i, prop in enumerate(self.properties):
                print("Property ", i + 1)
                print("Rental Income: $", format(prop.rental_income, '.2f'))
                print("Taxes: $", format(prop.taxes, '.2f'))
                print("Insurance: $", format(prop.insurance, '.2f'))
                print("Utilities: $", format(prop.utilities, '.2f'))
                print("HOA fees: $", format(prop.HOA, '.2f'))
                print("Lawn cost: $", format(prop.lawn, '.2f'))
                print("Vacancy: $", format(prop.vacancy, '.2f'))
                print("Repairs: $", format(prop.repairs, '.2f'))
                print("Cap_X: $", format(prop.cap_x, '.2f'))
                print("Property Management cost: $", format(prop.property_management, '.2f'))
                print("Mortgage: $", format(prop.mortgage, '.2f'))
                print("DownPayment: $", format(prop.down_payment, '.2f'))
                print("Closing Cost: $", format(prop.closing_cost, '.2f'))
                print("Repair Budget: $", format(prop.repair_budget, '.2f'))
                print("Miscellaneous Expenses: $", format(prop.miscellaneous, '.2f'))
                print("Cash Flow: $", format(prop.cash_flow(), '.2f'))
                print("Cash on Cash Return: %", format(prop.cash_on_cash_return(), '.2f'))
                print("\n")

        def delete_property(self, index):
            del self.properties[index]

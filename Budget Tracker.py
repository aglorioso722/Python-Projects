#Budget Tracker Project Andrew Glorioso
class Budget:
    def __init__(self,income=0,expenses=0,netFlow=0):
        self.income=income
        self.expenses=expenses
        self.netFlow=netFlow
    # Prints a table of Income, Expenses, Recurring Costs, and Net flow
    def __str__(self):
        return f"Income: {self.income}\nExpenses: {self.expenses} "

    def get_income(self):
        self.income=int(input("Monthly Income: "))
        return self.income

    def get_expenses(self):
        total=0
        x=int(input("Enter number of expenses: "))
        expenselist = []
        for i in range(x):
            i += 1
            name=input(f"Expense # {i}: ")
            cost=int(input(f"Cost of {name}:$ "))
            expenselist.append(cost)
            self.expenses=sum(expenselist)
        return self.expenses

    def get_net_flow(self):
        self.net_Flow = self.income-self.expenses
        if self.income>self.expenses:
            print(f"Net gain of {self.net_Flow}")
        elif self.income<self.expenses:
            print(f'Net loss of {self.net_Flow}')
        return self.net_Flow

















# Instantantiate the object
House=Budget()

House.get_income()
House.get_expenses()
print(House)
House.get_net_flow()




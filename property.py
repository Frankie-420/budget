from loan import Loan
from income import Income
from expenses import Expenses

class Property:
    def __init__(self,property_name:str) -> None:
        self.property_name = property_name
        self.address = None
        self.property_price = 200_000
        self.income:Income = self._read_income_data()
        self.expenses:Expenses = self._read_expense_data()
        self.loan:Loan = self._read_loan_data()
    
    def _read_loan_data(self) -> Loan:
        loan = Loan(self.property_name)
        return loan

    def _read_expense_data(self) -> Expenses:
        expense = Expenses(self.property_name)
        return expense

    def _read_income_data(self) -> Income:
        income = Income(self.property_name)
        return income

    def total_cash_invested(self) -> float:
        return self.expenses.total_expenses() + self.loan.total_loan_payment() - self.income.total_income()

    def gross_rental_yield(self) -> float:
        return round((self.income.average_annual_income() / self.property_price) * 100,2)
    
    def average_annual_cash_flow(self) -> float:
        return self.income.average_annual_income() - (self.expenses.average_annual_expenses() + self.loan.average_annual_loan_payment())
    
    def cash_on_cash_return(self) -> float:
        return round(self.average_annual_cash_flow()/ self.total_cash_invested(),2)*100
    
    def operating_expense_ratio(self) -> float:
        return round((self.expenses.total_operating_expenses() / self.income.total_income()) * 100,2)
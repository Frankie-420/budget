import sqlite3

class ExpensePayment:
    def __init__(self, date, proprety_taxes, insurance, property_management_fees, transfer_fees, repairs_maintenance, legal_accounting_fees, Lease_Renewal_Contract_Fees, Capital_Improvements):
        self.date = date
        
        # Fixed Expenses
        self.property_taxes = proprety_taxes
        self.insurance = insurance
        self.property_management_fees = property_management_fees

        # Variable Expenses
        self.transfer_fees = transfer_fees
        self.repairs_maintenance = repairs_maintenance
        self.legal_accounting_fees = legal_accounting_fees

        # Vacancy & Turnover Costs
        self.Lease_Renewal_Contract_Fees = Lease_Renewal_Contract_Fees

        # Capital Expenditures
        self.Capital_Improvements = Capital_Improvements

    def total_month_expenses(self) -> float:
        return sum([self.property_taxes, self.insurance, self.property_management_fees, self.transfer_fees, self.repairs_maintenance, self.legal_accounting_fees, self.Lease_Renewal_Contract_Fees, self.Capital_Improvements])

    def total_month_operating_expenses(self) -> float:
        return sum([self.property_taxes, self.insurance, self.property_management_fees, self.transfer_fees, self.repairs_maintenance, self.legal_accounting_fees, self.Lease_Renewal_Contract_Fees])

    @classmethod
    def read_expense_data(cls, file_path: str) -> list['ExpensePayment']:
        expense = []
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        for row in rows:
            expense.append(cls(*row))
        conn.close()
        return expense

class Expenses:
    def __init__(self, database):
        self.expense_data = ExpensePayment.read_expense_data(database)

    def total_expenses(self) -> float:
        return sum([expense.total_month_expenses() for expense in self.expense_data])

    def average_annual_expenses(self) -> float:
        return (self.total_expenses() / len(self.expense_data)) * 12
    
    def total_operating_expenses(self) -> float:
        return sum([expense.total_month_operating_expenses() for expense in self.expense_data])
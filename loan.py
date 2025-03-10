import sqlite3

class LoanPayments:
    def __init__(self,date, loan_payment,loan_interest, loan_package_cost):
        self.date = date
        self.loan_payment = loan_payment
        self.loan_interest = loan_interest
        self.loan_package_cost = loan_package_cost

        self.princple_payment = self.loan_payment - self.loan_interest

    def total_loan_payment(self) -> float:
        return sum([self.loan_payment, self.loan_package_cost])

    @classmethod
    def read_loan_payments_data(cls, file_path: str) -> list['LoanPayments']:
        income = []
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM loan")
        rows = cursor.fetchall()
        for row in rows:
            income.append(cls(*row))
        conn.close()
        return income

class Loan:
    def __init__(self, database:str):
        self.loan_playments = LoanPayments.read_loan_payments_data(database)

    def total_loan_payment(self) -> float:
        return sum([loan.total_loan_payment() for loan in self.loan_playments])

    def average_annual_loan_payment(self) -> float:
        return (self.total_loan_payment() / len(self.loan_playments)) * 12
import sqlite3

class IncomePayments:
    def __init__(self,date, amount):
        self.date = date
        self.amount = amount

    @classmethod
    def read_income_data(cls, file_path: str) -> list['IncomePayments']:
        income = []
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT date, income FROM income")
        rows = cursor.fetchall()
        for row in rows:
            date, amount = row
            income.append(cls(date, amount))
        conn.close()
        return income

class Income:
    def __init__(self, database:str):
        self.income_playments = IncomePayments.read_income_data(database)

    def total_income(self) -> float:
        return sum([income.amount for income in self.income_playments])
    
    def average_annual_income(self) -> float:
        return (self.total_income()/ len(self.income_playments)) *12
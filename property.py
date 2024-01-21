
'''
noi = Net Operating Income
'''
class property():
    def __init__(self):
        pass

    def get_net_operating_income(self,gross_income:float,total_expense:float) -> float:
        'Net operating income is the income excluding all costs that are not re-invested'
        return gross_income - total_expense
    def get_cap_rate(self,noi:float,property_value:float):
        'The higher the cap rate the better'
        return (noi / self.property_value) * 100
    def get_dept_service_ratio(self,noi:float,dept_service:float):
        '''dept service is the total amount of dept we are paying including,
        principle + intrest + etc.'''
        return (noi / dept_service)
    def get_return_on_investment(net_profit:float,cost_of_investment:float):
        '''this in essence is a the return we recieve for the amount of money we put in'''
        return(net_profit / cost_of_investment) * 100

class Employee :

    def __init__(self,base_salary,bonus_hrs,sales,name):
        self.base_salary = base_salary
        self.bonus_hrs = bonus_hrs
        self.sales = sales
        self.name = name

    def calculate_net_salary(self):
        net_salary = self.base_salary + self.bonus_hrs 
        print("Hi ",self.name," your net salary is : ",net_salary)

emp1 = Employee(1000,400,100,"ayoub")
emp1.calculate_net_salary()
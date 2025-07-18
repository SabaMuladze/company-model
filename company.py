class Employee:
    increase_percent = 1.05
    def __init__(self,first,last,salary):
        self.first= first
        self.last = last
        self.salary = salary
    
    def __str__(self):
        return f'{self.first} {self.last}'
    
    def increase_salary(self):
     self.salary = self.salary * self.increase_percent
     return self.salary

employee1 = Employee('Saba','Muladze',1000)
print(employee1)
employee1.increase_salary()
print(employee1.salary)
        


        
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

class Developer(Employee):
   increase_percent = 1.2
   def __init__(self, first, last, salary,language):
      super().__init__(first, last, salary)
      self.language = language
    

# test Employee part
employee1 = Employee('Saba','Muladze',5000)
print(employee1)
employee1.increase_salary()
print(employee1.salary)
#test Developer part
developer1 = Developer('Givi','Pailodze',6000,'Python')
print(developer1)
developer1.increase_salary()
print(developer1.salary)


        
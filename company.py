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
    def __init__(self, first, last, salary,skills):
      super().__init__(first, last, salary)
      self.skills = skills

    def show_skills(self):
        print(f"###### {self.first} {self.last}'s skills are:")
        for skill in self.skills:
            print(skill)
        print('######')
          

class Manager(Employee):
    increase_percent = 1.1

    def __init__(self, first, last, salary,team):
      super().__init__(first, last, salary)
      self.team = team
    
    def add_in_team(self,employee):
      self.team.append(employee)
    
    def delete_from_team(self,employee):
       self.team.remove(employee)
    
    def show_team(self):
        if len(self.team) == 0:
          print('Team is empty')
        else:
            print(f"###### {self.first} {self.last}'s team is:")
            for member in self.team:  
                print(member)
            print('######')
          
      
    

# test Employee part
employee1 = Employee('Saba','Muladze',5000)
print(employee1)
employee1.increase_salary()
print(employee1.salary)
#test Developer part
developer1 = Developer('Givi','Pailodze',6000,['Python','Flask','Selenium'])
developer2 = Developer('Mariam','Nozadze',6100,['JS','HTML','CSS','React'])
print(developer1)
developer1.increase_salary()
print(developer1.salary)
developer1.show_skills()
# test Manager part
manager1 = Manager('Sofo','Menejerishvili',5500,[developer1])
print(manager1)
manager1.increase_salary()
print(manager1.salary)
manager1.show_team()
manager1.add_in_team(employee1)
manager1.add_in_team(developer2)
manager1.show_team()
manager1.delete_from_team(employee1)
manager1.show_team()


        
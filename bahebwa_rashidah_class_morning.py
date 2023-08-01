#classs in this module
#universitystudent
class universitystudent:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display(self):
        print(self.name,self.age,self.course)

        student=universitystudent("bahebwa",22,"BSSE")
        student.display()
        print(student.name,student.age,student.course)

        student1=universitystudent("bahebwa",22,"BSSE")
        student1.display()
        print(student1.name,student1.age,student1.course)


        # calculate and display employee bonus of salary
        # create class employee
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)

    def calculate_bonus(self):
        if self.salary <= 100000:
            bonus = self.salary * 0.1  # 10% bonus for salary <= 100,000
        elif self.salary <= 200000:
            bonus = self.salary * 0.15  # 15% bonus for salary <= 200,000
        else:
            bonus = self.salary * 0.2  # 20% bonus for salary > 200,000
        return bonus


# Create employee instances
employee1 = Employee("employee1", 30, 150000)
employee2 = Employee("employee2", 35, 230000)

# Calculate bonuses
bonus1 = employee1.calculate_bonus()
bonus2 = employee2.calculate_bonus()

# Print the bonuses
print(f"{employee1.name} bonus: ${bonus1}")
print(f"{employee2.name} bonus: ${bonus2}")










#assigment for day four about encaplusation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def calculate_bonus(self):
        bonus = self._salary * 0.15
        return bonus

    def increment_salary(self, increment_amount):
        self._salary += increment_amount

    def get_salary(self):
        return self._salary

# Create employee instance
employee = Employee("John Doe", 850000)

# Calculate current bonus
bonus = employee.calculate_bonus()
print("Current Bonus:", bonus)

# Increment the salary
increment_amount = 150000
employee.increment_salary(increment_amount)

# Get the updated salary
new_salary = employee.get_salary()
print("New Salary:", new_salary)


        

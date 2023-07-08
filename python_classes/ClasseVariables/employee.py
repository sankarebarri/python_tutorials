class Employee:

    # class variable
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}"

        Employee.num_of_employees += 1

    def full_name(self):
        return f"{self.first}.{self.last}"
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

print(f"Number of employees is: {Employee.num_of_employees}")

emp_1 = Employee('Bilal', 'SHerif', 60000)
emp_2 = Employee('Katerine', 'Joe', 80000)
emp_3 = Employee('Jane', 'Doe', 54879)

print(f"Number of employees is: {Employee.num_of_employees}")

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# print namespace of the emp_1
print(emp_1.__dict__)

# print namespace of the Employee
print(Employee.__dict__)

# changing the class variable would affect all instances
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# changing an instance variable would affect just the instance
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)



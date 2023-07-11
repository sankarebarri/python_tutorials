class Employee:

    # class variable
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

        Employee.num_of_employees += 1

    # creating a regular method
    def full_name(self):
        return f"{self.first}.{self.last}"
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


    # creating a class method
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # creating an alternative constructor with a class method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    

    # creating static method
    @staticmethod # it has a logical connection with our class but it doesn't depend on the parameters of our class
    def is_workday(day): # it doesn't take self or cls
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
  

emp_1 = Employee('Bilal', 'SHerif', 60000)
emp_2 = Employee('Katerine', 'Joe', 80000)
emp_3 = Employee('Jane', 'Doe', 54879)

Employee.set_raise_amount(1.06) # == Employee.raise_amount = 1.06


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

### @classmethod as alternative constructor
emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-7800'
emp_str_3 = 'Jane-Doe-8000'

### Way to do if not done with classmethod
first, last, pay = emp_str_1.split('-')
print(first, last, pay)
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)

### Way to do with classmethod
new_emp_11 = Employee.from_string(emp_str_2)
print(new_emp_11.email)
print(new_emp_11.pay)


### staticmethod
import datetime
my_date = datetime.date(2023, 7, 9)

print(Employee.is_workday(my_date))
class Employee:
    
    def __init__(self, first, last, pay):
        self.first_name = first
        self.last_name = last
        self.pay = pay
        self.email = f"{self.first_name}.{self.last_name}@company.com"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

## Creating instances
empl_1 = Employee('Mike', 'November', 50000)
empl_2 = Employee('Oscar', 'Papa', 12000)

print(empl_1.first_name)
print(empl_2.first_name)
print(empl_1.full_name())
print(Employee.full_name(empl_2))


## Creating instance variables
empl_1.first_name = 'Alpha'
empl_1.last_name = 'Bravo'
# empl_1.email = 'Alpha.Bravo@company.com'
empl_1.pay = 20000

empl_2.first_name = 'Charlie'
empl_2.last = 'Delta'
# empl_2.email = 'Charlie.Delta@company.com'
empl_2.pay = 70000

print(empl_1.email)
print(empl_2.email)

print(empl_1.first_name)
print(empl_2.last)




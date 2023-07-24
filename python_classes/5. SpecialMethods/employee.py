class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{self.first}.{self.last}@company.com"
        self.pay = pay

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    ## Magic methods or Dunder methods

    # unambiguous representation of the object, should be used for loggin, debugging, etc
    # meant to be seen by other developers
    def __repr__(self):
        return 'Employee("{}", "{}", {})'.format(self.first, self.last, self.pay)
        # return f'Employee({self.first}, {self.last} {self.pay})'

    # readable representation of the object, meant to be use as a display to the un-user
    def __str__(self):
        return '{} - {}'.format(self.full_name(), self.email)


emp_1 = Employee("John", "Doe", 52131)
emp_2 = Employee('Jane', 'Kate', 69856)


# will print the __str__ if defined, else will fallback to __repr__
print(emp_1)
# print(emp_1.email)

print(2 + 3) # it's actually doing int.__add__(2, 3) at the background
print(int.__add__(2, 3))

print('a' + 'y') # it's actually doing str.__add__('x', 'y') at the background
print(str.__add__('d', 'x'))

# will print both of them 
print(repr(emp_1))
print(str(emp_1))
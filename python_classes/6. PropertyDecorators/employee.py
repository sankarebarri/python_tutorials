class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = f"{self.first}.{self.last}@company.com"
        # self.pay = pay

    @property # this would allow us to call the email method as an attribute
    def email(self):
        return '{}.{}@company'.format(self.first, self.last)

    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    @full_name.setter # this would allow us to call the full_name method as an attribute and also chhange attributes
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter # this is what will happen if we do del emp_1.full_name
    def full_name(self):
        print('Deleted names')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith', 65879)

# this will change the first and last name but not the email. This is where @property gets in
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email) # print(emp_1.email()) is no more necessary since we used @property above
print(emp_1.full_name)

emp_1.full_name = 'Alpha Bravo' # won't work exceptt if do @full_name.setter in the class

# all these will be affected by the above emp_1.full_name = 'Alpha Bravo'
print(emp_1.first)
print(emp_1.email) # print(emp_1.email()) is no more necessary since we used @property above
print(emp_1.full_name)

del emp_1.full_name
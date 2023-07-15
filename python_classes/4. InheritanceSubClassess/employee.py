class Employee:

    # class variable
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@company.com"

    # creating a regular method
    def full_name(self):
        return f"{self.first}.{self.last}"
    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# creating Developer subclasses
class Developer(Employee):
    # Method resolution order(MRO): Developer -> Employee -> builtin methods
    raise_amount = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # same as Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) # same as Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())

    # def print_emps_email(self):
    #     for emp in self.employees:
    #         print('-->', emp.self.email)

dev_1 = Developer('Alpha', 'Bravo', 50206, 'Python')
dev_2 = Employee('Charlie', 'Delta', 85462)

mgr_1 = Manager('Yankee', 'Zulu', 90054, [dev_1])

print(mgr_1.email)
mgr_1.print_emps()
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)

print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Manager))
print(isinstance(dev_1, Manager))
print(issubclass(Manager, Developer))
# mgr_1.print_emps()
# mgr_1.print_emps_email()
# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))

# print(dev_1.pay)
# print(dev_1.prog_lang)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_2.pay)
# dev_2.apply_raise()
# print(dev_2.pay)
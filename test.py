import sys

print(sys.executable)
print(sys.version)


class Employee:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def email(self):
        return '{}.{}@{}.com'.format(self.name, self.surname, 'gmail')

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.surname)


employee = Employee('Alexander', 'Kvapel')

print(employee.name)
print(employee.email)
print(employee.fullname)



class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee:
    def __init__(self, code, name, salary):
        if type(self) == Employee:
            raise TypeError('base class may not be instantiated')

        self.code = code
        self.name = name
        self.salary = salary

    def calc_bonus(self):
        raise NotImplementedError

    def get_hours(self):
        raise NotImplementedError

    def get_department(self):
        raise NotImplementedError

    def set_department(self, department):
        raise NotImplementedError


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return 8

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department = department


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_hours(self):
        return 8

    def get_department(self):
        return self.__department.name

    def set_department(self, department):
        self.__department = department

    def get_sales(self):
        return self.__sales

    def put_sales(self, sale):
        self.__sales += sale

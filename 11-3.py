import unittest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, raisesalary=5000):
        self.salary += raisesalary


class Test_employee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('jason', 5000)

    def test_give_default_raise(self):
        self.employee.give_raise(20)
        self.assertEqual(self.employee.salary, 5020)


if __name__ == '__main__':
    unittest.main()

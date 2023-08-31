
class Employee:
    no_of_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1

    @staticmethod
    def average_salary(femployees, n):
        add = 0
        for employee in femployees:
            add += employee.salary
        return add / n


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)

def main():
    femployees = []
    employees = []
    femp1 = FulltimeEmployee("Kiran", "Kumar", 145000, "Team Lead")
    femployees.append(femp1)
    femp2 = FulltimeEmployee("Manideep", "Reddy", 180000, "Delivery Manager")
    femployees.append(femp2)
    femp3 = FulltimeEmployee("Sushma", "Shetty", 155000, "Project Lead")
    femployees.append(femp3)
    femp4 = FulltimeEmployee("Vaishnavi", "Reddy", 180000, "hr")
    femployees.append(femp4)
    employee1 = Employee("Mahitha", "Reddy", 96000, "Developer")
    employees.append(employee1)
    employee2 = Employee("Bharat", "Kumar", 50000, "Tester")
    employees.append(employee2)
    print("Average salary of fulltimeemployees:", FulltimeEmployee.average_salary(femployees, (len(femployees))))
    print("Average salary of employees:", Employee.average_salary(employees, (len(employees))))

if __name__ == "__main__":
    main()
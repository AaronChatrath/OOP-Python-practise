class employee:
    def __init__(self, id, name, title, gender, salary):
        self.id = id
        self.name = name
        self.title = title
        self.gender = gender
        self.salary = salary

class manager(employee):
    def __init__(self, id, name, title, gender, salary, department, current_project):
        super().__init__(id, name, title, gender, salary)
        self.department = department
        self.current_project = current_project
        self.employee_workers = []
    
    def add_employee(self, employee):
        dict_emp = {}
        
        dict_emp['id'] = employee.id
        dict_emp['name'] = employee.name
        dict_emp['title'] = employee.title
        dict_emp['gender'] = employee.gender
        dict_emp['salary'] = employee.salary

        self.arr_employees.append(dict_emp)

class company:
    def __init__(self, company_name, location):
        self.company_name = company_name
        self.location = location
        self.arr_employees = []
    
    def show_company_details(self):
        print(self.company_name)
        print(self.location)
    
    def add_employee_to_company(self, employee):
        dict_emp = {}
        
        for i in range(len(self.arr_employees)):
            if self.arr_employees[i]['id'] == employee.id:
                print("employee already exists")
                return

        dict_emp['id'] = employee.id
        dict_emp['name'] = employee.name
        dict_emp['title'] = employee.title
        dict_emp['gender'] = employee.gender
        dict_emp['salary'] = employee.salary

        self.arr_employees.append(dict_emp)

        print(len(self.arr_employees))

    
    def show_company_employee_list(self):
        print(self.arr_employees)

if __name__ == "__main__":

    edf_c = company("edf", "London")
    greg_e = employee(1234, "Greg James", "associate engineer", "M", 123000)
    daniel_e = employee(1234, "Daniel James", "senior engineer", "M", 150000)
    edf_c.add_employee_to_company(greg_e)
    edf_c.add_employee_to_company(daniel_e)
    edf_c.show_company_employee_list()
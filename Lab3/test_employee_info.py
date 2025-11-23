import employee_info

def test_age_range():
    lower_limit = 23
    upper_limit = 35
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    
    result = employee_info.get_employees_by_age_range(lower_limit,upper_limit)
    
    assert(result == expected_result)
    
    
def test_average():
    expected_result = 60166.67
    
    result = employee_info.calculate_average_salary()
    assert(result == expected_result)

def test_department():
    department = "Sales"
    expected_result = [    
                        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
                        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result = employee_info.get_employees_by_dept(department)
    assert(result == expected_result)
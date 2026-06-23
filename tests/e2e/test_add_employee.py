from data.employee import Employee
from faker import Faker
from tests.api_fixtures import add_employee
fake = Faker()

def test_add_employee_without_login_details(add_employee_page_fixture):
    employee = Employee(
        first_name=fake.first_name(),
        middle_name=fake.first_name(),
        last_name=fake.last_name(),
    )
    add_employee_page_fixture.add_employee(employee)
    
def test_add_employee_with_login_details(add_employee_page_fixture):
    employee = Employee(
        first_name=fake.first_name(),
        middle_name=fake.first_name(),
        last_name=fake.last_name(),
        username=fake.user_name(),      
        password=fake.password(length=10)
    )
    add_employee_page_fixture.add_employee(employee, save=False)
    add_employee_page_fixture.enable_login_details(employee)


def test_add_employee_api(add_employee,page):
    employee_data = add_employee
    emp_number = employee_data["data"]["empNumber"]

    response = page.request.get(
        f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}"
    )

    assert response.ok
    assert response.json()["data"]["empNumber"] == emp_number
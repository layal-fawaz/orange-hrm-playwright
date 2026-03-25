import time
def test_add_employee_without_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz", "Alhusseini")
def test_add_employee_with_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz","Alhusseini", save=False)
    unique_user = f"layal{int(time.time())}"
    add_employee_page_fixture.enable_login_details(unique_user, "22l44ayyiw")


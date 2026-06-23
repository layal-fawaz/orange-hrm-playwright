def test_add_employee_without_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz")

def test_add_employee_with_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz")
    add_employee_page_fixture.enable_login_details("layal12", "22l44ayyiw")

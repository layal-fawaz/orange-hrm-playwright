def test_add_employee_without_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz", "Alhusseini")
def test_add_employee_with_login_details(add_employee_page_fixture):
    add_employee_page_fixture.add_employee("Layal", "Fawaz","Alhusseini", save=False)
    add_employee_page_fixture.enable_login_details("layal4", "22l44ayyiw")


import pytest
def test_search_employee_by_id(created_employee_fixture, employee_list_page_fixture):
    employee_id = created_employee_fixture["id"]
    employee_list_page_fixture.fill_employee_id_input(employee_id)
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.assert_employee_found(employee_id)

@pytest.mark.parametrize("invalid_id",["999387"])
def test_search_employee_by_not_found_id(employee_list_page_fixture,invalid_id):
    employee_list_page_fixture.fill_employee_id_input(invalid_id)
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.search_fail()

@pytest.mark.parametrize("invalid_name",["juususu"])
def test_search_employee_by_not_found_name(employee_list_page_fixture,invalid_name):
    employee_list_page_fixture.fill_employee_name_input(invalid_name)
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.search_fail()

def test_search_employee_by_name(created_employee_fixture,employee_list_page_fixture):
    name=created_employee_fixture["name"]
    employee_list_page_fixture.fill_employee_name_input(name)
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.assert_employee_found(name)


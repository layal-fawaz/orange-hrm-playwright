def test_search_employee_by_id(employee_list_page_fixture):
    employee_list_page_fixture.fill_employee_id_input("0295")
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.assert_employee_found("0295")

def test_search_employee_by_not_found_id(employee_list_page_fixture):
    employee_list_page_fixture.fill_employee_id_input("099")
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.search_fail()

def test_search_employee_by_not_found_name(employee_list_page_fixture):
    employee_list_page_fixture.fill_employee_name_input("Layal")
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.search_fail()

def test_search_employee_by_name(employee_list_page_fixture):
    employee_list_page_fixture.fill_employee_name_input("Amelia")
    employee_list_page_fixture.click_search()
    employee_list_page_fixture.assert_employee_found("Amelia")

# def test_search_employee_by_full_name(employee_list_page_fixture):
#     employee_list_page_fixture.fill_employee_name_input("aniket t t")
#     employee_list_page_fixture.click_search()
#     employee_list_page_fixture.assert_employee_found("aniket t")

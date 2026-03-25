import pytest
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_list_page import EmployeeListPage

@pytest.fixture(autouse=True)
def login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_valid_admin()
@pytest.fixture
def add_employee_page_fixture(page):
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    return AddEmployeePage(page)
@pytest.fixture
def employee_list_page_fixture(page,login):
    pim_page = PimPage(page)
    pim_page.visit_tab_employee_list()
    return EmployeeListPage(page)
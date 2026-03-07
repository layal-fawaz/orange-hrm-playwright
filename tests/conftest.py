import pytest
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.add_employee_page import AddEmployeePage


@pytest.fixture(autouse=True)
def login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")


@pytest.fixture
def add_employee_page_fixture(page):
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    return AddEmployeePage(page)

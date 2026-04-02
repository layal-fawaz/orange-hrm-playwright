import pytest
from pytest_playwright.pytest_playwright import page
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_list_page import EmployeeListPage
from pages.recruitment_page import RecruitmentPage
from pages.recruitment.vacancy_page import VacancyPage


@pytest.fixture(autouse=True)
def login(page):
    """Log in as admin before every test."""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_with_valid_admin()


@pytest.fixture
def add_employee_page_fixture(page):
    """Navigate to Add Employee page and return the page object."""
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    return AddEmployeePage(page)


@pytest.fixture
def employee_list_page_fixture(page):
    """Navigate to Employee List page and return the page object."""
    pim_page = PimPage(page)
    pim_page.visit_tab_employee_list()
    return EmployeeListPage(page)


@pytest.fixture
def created_employee_fixture(page):
    """Create a temporary employee and yield their ID.
    Guarantees the employee exists in the system for search-by-id tests."""
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    add_page = AddEmployeePage(page)
    first_name = "layalf"
    middle_name = ""
    last_name = "alhusseini"
    employee_id = add_page.add_employee(first_name, middle_name, last_name)
    yield {
        "id": employee_id,
        "name": "layalf",
        "full_name": f"{first_name} {middle_name} {last_name}".strip(),
    }
    pim_page.visit_tab_employee_list()
    employee_list = EmployeeListPage(page)
    employee_list.delete_employee(employee_id)

@pytest.fixture
def created_hiring_manager_fixture(page):
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    add_page = AddEmployeePage(page)
    first_name = "layal_h_manager"
    last_name = "f"
    employee_id = add_page.add_employee(first_name, "", last_name)
    yield {
        "id": employee_id,
        "full_name": f"{first_name} {last_name}".strip(),
    }
    PimPage(page).visit_tab_employee_list()
    EmployeeListPage(page).delete_employee(employee_id)

@pytest.fixture
def vacancy_page_fixture(page, created_hiring_manager_fixture):
    hiring_manager_name = created_hiring_manager_fixture["full_name"]

    recruitment_page = RecruitmentPage(page)
    recruitment_page.navigate_to_Recruitment()
    recruitment_page.go_to_Vacancy()

    vacancy_page = VacancyPage(page)
    vacancy_page.go_to_add_vacancy()

    vacancy_name = "vacname"
    yield vacancy_page, vacancy_name, hiring_manager_name
    RecruitmentPage(page).navigate_to_Recruitment() 
    recruitment_page.go_to_Vacancy()
    VacancyPage(page).delete_vacancy(vacancy_name)


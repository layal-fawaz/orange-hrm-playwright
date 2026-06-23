import pytest
from pytest_playwright.pytest_playwright import page
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.pim.add_employee_page import AddEmployeePage
from pages.pim.employee_list_page import EmployeeListPage
from pages.recruitment_page import RecruitmentPage
from pages.recruitment.vacancy_page import VacancyPage
from pages.recruitment.candidate_page import CandidatePage
from utils.decorators import pw_trace
from data.employee import Employee
from data.vacancy import Vacancy
from data.candidate import Candidate
from utils.data_generator import generate_phone
from faker import Faker
fake=Faker()
pytest_plugins = ["api_fixtures"]


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
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()

    add_page = AddEmployeePage(page)

    employee = Employee()

    employee_id = add_page.add_employee(employee)

    yield {
        "id": employee_id,
        "name": employee.first_name,
        "full_name": f"{employee.first_name} {employee.last_name}".strip(),
    }

    pim_page.visit_tab_employee_list()
    EmployeeListPage(page).delete_employee(employee_id)


@pytest.fixture
def created_hiring_manager_fixture(page):
    pim_page = PimPage(page)
    pim_page.go_to_add_employee()
    add_page = AddEmployeePage(page)
    employee = Employee()
    employee_id = add_page.add_employee(employee)

    yield {
        "id": employee_id,
        "full_name": f"{employee.first_name} {employee.middle_name} {employee.last_name}".strip(),
    }

    PimPage(page).visit_tab_employee_list()
    EmployeeListPage(page).delete_employee(employee_id)

@pytest.fixture
def vacancy_page_fixture(page, created_hiring_manager_fixture):
    """Create a vacancy using the hiring manager, delete after test."""
    hiring_manager_name = created_hiring_manager_fixture["full_name"]
    vacancy = Vacancy()
    vacancy.hiring_manager = hiring_manager_name

    recruitment_page = RecruitmentPage(page)
    recruitment_page.navigate_to_recruitment()
    
    recruitment_page.go_to_vacancy()

    vacancy_page = VacancyPage(page)
    vacancy_page.go_to_add_vacancy()
    vacancy_page.add_vacancy(vacancy)

    yield vacancy.vacancy_name
    RecruitmentPage(page).navigate_to_recruitment() 
    recruitment_page.go_to_vacancy()
    VacancyPage(page).delete_vacancy(vacancy.vacancy_name)

@pytest.fixture
def candidate_fixture(page, vacancy_page_fixture):
    """Setup: navigate to candidate page + prepare data. Teardown: delete candidate."""
    
    RecruitmentPage(page).navigate_to_recruitment()
    RecruitmentPage(page).go_to_candidate()
    candidate_page = CandidatePage(page)

    candidate = Candidate(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        vacancy=vacancy_page_fixture,
        email=fake.email(),
        contact_phone=generate_phone(),
        keywords=fake.word(),
        date_of_application=fake.date_of_birth().strftime("%Y-%d-%m"),
        notes=fake.sentence()
    )

    yield candidate_page, candidate

    # Teardown
    RecruitmentPage(page).navigate_to_recruitment()
    RecruitmentPage(page).go_to_candidate()
    CandidatePage(page).delete_candidate(candidate.full_name)
import pytest
import json
from data.employee import Employee
from data.candidate import Candidate
from data.vacancy import Vacancy

@pytest.fixture
def add_employee(page, login):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"
    employee = Employee()

    response = page.request.post(
        url,
        data={  
            "firstName": employee.first_name,
            "middleName": employee.middle_name,
            "lastName": employee.last_name,
        }
    ) 

    assert response.ok, f"Failed to create employee: {response.text()}"
    employee_data = response.json()
    emp_number = employee_data.get("data", {}).get("empNumber")
    assert emp_number, "Employee number not found in response"

    yield employee_data

    delete_response = page.request.delete(
        url,
        data=json.dumps({"ids": [emp_number]}),
        headers={"Content-Type": "application/json"}
    )
    
    assert delete_response.ok, (
        f"Failed to delete emp {emp_number}: "
        f"[{delete_response.status}] {delete_response.text()}"
    )

@pytest.fixture
def add_vacancy(add_employee, page):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/recruitment/vacancies"
    emp_number = add_employee.get("data", {}).get("empNumber")
    
    vacancy = Vacancy()
    response = page.request.post(
        url,
        data=json.dumps({
            "name": vacancy.vacancy_name,
            "jobTitleId": 1,
            "employeeId": emp_number,
            "numOfPositions": None,
            "description": vacancy.job_description,
            "status": True,
            "isPublished": True
        }),
        headers={"Content-Type": "application/json"}
    )

    assert response.ok, f"Failed to create vacancy: {response.text()}"
    vacancy_data = response.json()
    vacancy_id = vacancy_data.get("data", {}).get("id")
    assert vacancy_id, "Vacancy ID not found"

    yield vacancy_data

    delete_response = page.request.delete(
        url,
        data=json.dumps({"ids": [vacancy_id]}),
        headers={"Content-Type": "application/json"}
    )
    assert delete_response.ok, (
        f"Failed to delete vacancy {vacancy_id}: "
        f"[{delete_response.status}] {delete_response.text()}"
    )

@pytest.fixture
def add_candidate(page, add_vacancy):
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/recruitment/candidates"
    vacancy_id = add_vacancy.get("data", {}).get("id")

    candidate = Candidate()
    response = page.request.post(
        url,
        data=json.dumps({
          "firstName": candidate.first_name,
          "middleName": candidate.middle_name,
          "lastName": candidate.last_name,
          "email": candidate.email,
          "vacancyId": vacancy_id,
          "dateOfApplication": candidate.date_of_application
        }),
        headers={"Content-Type": "application/json"}
    )

    assert response.ok, f"Failed to create candidate: {response.text()}"
    candidate_data = response.json()
    candidate_id = candidate_data.get("data", {}).get("id")
    assert candidate_id, "Candidate ID not found"

    yield candidate_data

    delete_response = page.request.delete(
        url,
        data=json.dumps({"ids": [candidate_id]}),
        headers={"Content-Type": "application/json"}
    )
    assert delete_response.ok, (
        f"Failed to delete candidate {candidate_id}: "
        f"[{delete_response.status}] {delete_response.text()}"
    )
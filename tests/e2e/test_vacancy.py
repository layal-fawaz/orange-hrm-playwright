from data.vacancy import Vacancy

def test_add_vacancy(vacancy_page_fixture):
    vacancy_page_fixture

def test_add_vacancy_api(page, add_vacancy):
    assert add_vacancy["data"]["id"], "Vacancy ID should exist"
    assert add_vacancy["data"]["name"], "Vacancy name should exist"
    




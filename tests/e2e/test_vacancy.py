def test_add_vacancy(vacancy_page_fixture):
    vacancy_page, vacancy_name ,hiring_manager_name= vacancy_page_fixture
    vacancy_page.add_vacancy(vacancy_name,"Software Engineer","Software Engineer",hiring_manager_name,"1")

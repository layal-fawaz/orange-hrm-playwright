from playwright.sync_api import Page,expect
from utils.decorators import pw_trace
from data.vacancy import Vacancy
class VacancyPage: 
    """Page object for Vacancy page."""
    def __init__(self,page:Page):
        self.page = page
   
    @pw_trace("Vacancy > Navigate to Vacancy")
    def go_to_add_vacancy(self):
        self.page.get_by_role("button",name="Add").click()
        expect(self.page.get_by_role("heading", name="Add Vacancy")).to_be_visible()
   
    @pw_trace("Vacancy > Add Vacancy")
    def add_vacancy(self,vacancy:Vacancy):
        self.page.get_by_text("Vacancy Name").locator("..").locator("..").locator(".oxd-input").fill(vacancy.vacancy_name)
        self.page.get_by_text("Job Title").locator("..").locator("..").locator(".oxd-select-wrapper").click()
        self.page.get_by_role("option", name=vacancy.job_title, exact=True).click()
        self.page.get_by_placeholder("Type description here").fill(vacancy.job_description)

        self.page.get_by_text("Hiring Manager").locator("..").locator("..").locator(".oxd-autocomplete-text-input input").fill(vacancy.hiring_manager)
        self.page.get_by_role("option", name=vacancy.hiring_manager).first.click()
        self.page.get_by_text("Number of Positions").locator("..").locator("..").locator(".oxd-input").fill(str(vacancy.number_of_positions))
        if not vacancy.active:
            self.page.get_by_text("Active").locator("..").locator("..").locator(".oxd-switch-input").click()
            self.page.wait_for_timeout(500) 
        self.page.get_by_role("button",name="Save").click()
        expect(self.page.get_by_role("heading", name="Edit Vacancy")).to_be_visible(timeout=10000)
  
    @pw_trace("Vacancy > Search Vacancy")
    def search_vacancy(self, vacancy_name):
        self.page.locator(".oxd-input-group", has_text="Vacancy").locator(".oxd-select-wrapper").click()
        self.page.get_by_role("option", name=vacancy_name).click()
        self.page.get_by_role("button", name="Search").click()
        result_row = self.page.locator(".oxd-table-card").filter(has_text=vacancy_name)
        expect(result_row).to_be_visible(timeout=10000)
        return result_row
    
    @pw_trace("Vacancy > Delete Vacancy")
    def delete_vacancy(self, vacancy_name):
        row = self.search_vacancy(vacancy_name)
        row.locator(".bi-trash").click()
        self.page.get_by_role("button", name="Yes, Delete").click()
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()

from playwright.sync_api import Page,expect
class VacancyPage: 
    """Page object for Vacancy page."""
    def __init__(self,page:Page):
        self.page = page
        
    def go_to_add_vacancy(self):
        self.page.get_by_role("button",name="Add").click()
        expect(self.page.get_by_role("heading", name="Add Vacancy")).to_be_visible()

    def add_vacancy(self,vacancy_name,job_title,description,hiring_manager,number_of_positions):
        self.page.get_by_text("Vacancy Name").locator("..").locator("..").locator(".oxd-input").fill(vacancy_name)
        self.page.get_by_text("Job Title").locator("..").locator("..").locator(".oxd-select-wrapper").click()
        self.page.get_by_role("option", name=job_title, exact=True).click()
        self.page.get_by_placeholder("Type description here").fill(description)

        self.page.get_by_text("Hiring Manager").locator("..").locator("..").locator(".oxd-autocomplete-text-input input").fill(hiring_manager)
        self.page.get_by_role("option", name=hiring_manager).click()
        self.page.get_by_text("Number of Positions").locator("..").locator("..").locator(".oxd-input").fill(number_of_positions)
        self.page.get_by_role("button",name="Save").click()
        # expect(self.page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)
        expect(self.page.get_by_role("heading", name="Edit Vacancy")).to_be_visible(timeout=10000)
    
    def search_vacancy(self, vacancy_name):
        self.page.locator(".oxd-input-group", has_text="Vacancy").locator(".oxd-select-wrapper").click()
        self.page.get_by_role("option", name=vacancy_name).click()
        self.page.get_by_role("button", name="Search").click()
        expect(self.page.locator(".oxd-table-card").filter(has_text=vacancy_name)).to_be_visible()
    
    def delete_vacancy(self, vacancy_name):
        self.search_vacancy(vacancy_name)
        row = self.page.locator(".oxd-table-card").filter(has_text=vacancy_name)
        row.locator(".bi-trash").click()
        self.page.get_by_role("button", name="Yes, Delete").click()
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()

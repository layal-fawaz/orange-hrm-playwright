from playwright.sync_api import Page,expect
from utils.decorators import pw_trace
class RecruitmentPage: 
    """Page object for Recruitment page."""
    def __init__(self,page:Page):
        self.page = page

    @pw_trace("Recruitment > Navigate to Recruitment")
    def navigate_to_Recruitment(self):
        self.page.get_by_role("link", name="Recruitment",exact=True).click()
        expect(self.page.get_by_role("heading", name="Recruitment")).to_be_visible()

    @pw_trace("Recruitment > Go to Vacancy")
    def go_to_Vacancy(self):
        self.page.get_by_text("Vacancies").click()
        expect(self.page.get_by_role("heading", name="Vacancies")).to_be_visible()

    
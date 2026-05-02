from playwright.sync_api import Page,expect
from utils.decorators import pw_trace
class EmployeeListPage:
    """Page object for Employee List page."""
    def __init__(self,page:Page):
        self.page = page

    def fill_employee_id_input(self,employee_id):
        self.page.get_by_text("Employee Id").locator("..").locator(
            "..").locator(".oxd-input").fill(employee_id)

    def fill_employee_name_input(self,employee_name):
        self.page.get_by_text("Employee Name").locator("..").locator(
            "..").locator("input").fill(employee_name)

    def click_search(self):
        self.page.get_by_role("button", name="Search").click()

    def search_fail(self):
        expect(self.page.locator("span").filter(has_text="No Records Found")).to_be_visible()

    def assert_employee_found(self, value):
        expect(self.page.get_by_text(value)).to_be_visible()
    @pw_trace()
    def delete_employee(self,employee_id):
        self.fill_employee_id_input(employee_id)
        self.click_search()
        self.page.locator("i.bi-trash").locator("..").first.click()
        self.page.get_by_role("button", name="Yes, Delete").click()
        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()



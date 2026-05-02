from playwright.sync_api import expect
from utils.decorators import pw_trace
class PimPage:
    """Page object for PIM page."""
    def __init__(self, page):
        self.page = page
        self.page.get_by_role("link", name="PIM", exact=True).click()
        expect(self.page.get_by_role("heading", name="PIM")).to_be_visible()
    @pw_trace("Navigate to Add Employee")
    def go_to_add_employee(self):
        self.page.get_by_text("Add Employee").click()
        expect(self.page.get_by_role("heading", name="Add Employee")).to_be_visible()
    @pw_trace("Navigate to Add Employee")
    def visit_tab_employee_list(self):
        self.page.get_by_text("Employee List").click()
        expect(self.page.get_by_text("Employee Information")).to_be_visible()

from playwright.sync_api import expect

class PimPage:
    """Page object for PIM page."""
    def __init__(self, page):
        self.page = page
        self.page.get_by_text("PIM",exact=True).click()
        expect(self.page.get_by_role("heading", name="PIM")).to_be_visible()

    def go_to_add_employee(self):
        self.page.get_by_text("Add Employee").click()
        expect(self.page.get_by_role("heading", name="Add Employee")).to_be_visible()

    def visit_tab_employee_list(self):
        self.page.get_by_text("Employee List").click()
        expect(self.page.get_by_role("heading", name="Employee List")).to_be_visible()

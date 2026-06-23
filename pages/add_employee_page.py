from playwright.sync_api import expect
class AddEmployeePage:
    """Page object for Add Employee page"""
    def __init__(self, page):
        self.page = page
    def add_employee(self, first_name, last_name,employee_id=None):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        if employee_id is not None:
            self.page.get_by_role("textbox").nth(4).fill(employee_id)
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully Saved")).to_be_visible()

    def enable_login_details(self, username, password):
        self.page.wait_for_selector(".oxd-form-loader", state="detached", timeout=10000)
        self.page.wait_for_selector('input[type="text"]', timeout=5000)
        self.page.wait_for_selector('input[type="password"]', timeout=5000)
        self.page.get_by_role("textbox").nth(5).fill(username)
        self.page.locator('input[type="password"]').first.fill(password)
        self.page.locator('input[type="password"]').nth(1).fill(password)

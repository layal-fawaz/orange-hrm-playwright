class AddEmployeePage:
    """Page object for Add Employee page"""
    def __init__(self, page):
        self.page = page
    def add_employee(self, first_name, last_name,employee_id):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)
        self.page.get_by_role("textbox").nth(4).fill(employee_id)
        self.page.get_by_role("button", name="Save").click()
    def enable_login_details(self, username, password):
        self.page.locator(".oxd-switch-input").click()
        self.page.get_by_role("textbox").nth(5).fill(username)
        self.page.locator('input[type="password"]').first.fill(password)
        self.page.locator('input[type="password"]').nth(1).fill(password)

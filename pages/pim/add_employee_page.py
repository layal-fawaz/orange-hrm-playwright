from playwright.sync_api import expect,Page
class AddEmployeePage:
    """Page object for Add Employee page"""
    def __init__(self, page:Page):
        self.page = page
    def add_employee(self, first_name,middle_name,last_name, save=True):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Middle Name").fill(middle_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)

        employee_id_input = (self.page.get_by_text("Employee Id")
                            .locator("..")
                            .locator("..")
                            .locator(".oxd-input"))
        init_id = employee_id_input.input_value()
        final_id = init_id + "_42"
        employee_id_input.fill(final_id)

        if save:
            self.page.get_by_role("button", name="Save").click()
            expect(self.page.get_by_text("Successfully saved")).to_be_visible(timeout=10000)

    def enable_login_details(self, username, password):
        self.page.locator(".oxd-switch-input").click()
        self.page.get_by_text("Username").locator("..").locator("..").locator(".oxd-input").fill(username)
        self.page.get_by_text("Password").nth(0).locator("..").locator("..").locator("input").first.fill(password)
        self.page.get_by_text("Confirm Password").locator("..").locator("..").locator("input").fill(password)
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully saved")).to_be_visible(timeout=10000)
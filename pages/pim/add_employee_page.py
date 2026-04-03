from playwright.sync_api import expect,Page
from utils.decorators import pw_trace
class AddEmployeePage:
    """Page object for Add Employee page"""
    def __init__(self, page:Page):
        self.page = page
    @pw_trace("Add Employee")
    def add_employee(self, first_name,middle_name,last_name, save=True):
        self.page.get_by_placeholder("First Name").fill(first_name)
        self.page.get_by_placeholder("Middle Name").fill(middle_name)
        self.page.get_by_placeholder("Last Name").fill(last_name)

        init_id = self.get_employee_id()
        final_id = init_id + "_42"
        self.get_id_input_locator().fill(final_id)

        if save:
            self.page.get_by_role("button", name="Save").click()
            expect(self.page.get_by_text("Successfully saved")).to_be_visible(timeout=10000)

        return final_id

    def get_id_input_locator(self):
          return (self.page.get_by_text("Employee Id")
                .locator("..")
                .locator("..")
                .locator(".oxd-input"))
    
    
    def get_employee_id(self):
       return self.get_id_input_locator().input_value()
    @pw_trace("Enable Login Details")
    def enable_login_details(self, username, password):
        self.page.locator(".oxd-switch-input").click()
        self.page.get_by_text("Username").locator("..").locator("..").locator(".oxd-input").fill(username)
        self.page.get_by_text("Password").nth(0).locator("..").locator("..").locator("input").first.fill(password)
        self.page.get_by_text("Confirm Password").locator("..").locator("..").locator("input").fill(password)
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully saved")).to_be_visible(timeout=10000)
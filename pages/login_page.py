from playwright.sync_api import expect
from utils.config import BASE_URL

class LoginPage:
    """Page object for Login page"""
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def login_with_valid_admin(self):
        self.login("Admin", "admin123")
        self.verify_login_ok()

    def invalid_login(self, username, password):
        self.login(username, password)
        expect(self.page.get_by_text("Invalid credentials")).to_be_visible()

    def verify_login_ok(self):
        dashboard_title = self.page.get_by_role("heading", name="Dashboard")
        expect(dashboard_title).to_be_visible()
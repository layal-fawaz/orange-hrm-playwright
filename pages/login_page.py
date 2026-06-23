from utils.config import BASE_URL
from playwright.sync_api import expect

class LoginPage:
    """Page object for Login page"""
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(BASE_URL)
        self.page.set_default_timeout(60000)

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
        expect(self.page.get_by_role("heading", name="Dashboard")).to_be_visible()

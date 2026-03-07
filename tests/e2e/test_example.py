import re
from playwright.sync_api import Page, expect
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
def login(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
def employee_details(page, first_name, last_name, employee_id):
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("link", name="Add Employee").click()
    page.get_by_role("textbox", name="First Name").fill(first_name)
    page.get_by_role("textbox", name="Last Name").fill(last_name)
    page.get_by_role("textbox").nth(4).fill(employee_id)
def test_add_employee_mismatched_passwords(page: Page) -> None:
    login(page)
    employee_details(page, "layal", "f", "1111")
    page.locator(".oxd-switch-input").click()
    page.get_by_role("textbox").nth(5).fill("layal")
    page.locator('input[type="password"]').first.fill("123456layal")
    page.locator('input[type="password"]').nth(1).fill("123456")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Passwords do not match")).to_be_visible()
def test_add_employee_success(page: Page) -> None:
    login(page)
    employee_details(page, "layal", "f", "1111")
    page.locator(".oxd-switch-input").click()
    page.locator('input[type="password"]').nth(1).fill("123456layal")
    page.get_by_role("button", name="Save").click()
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/"
        "pim/viewPersonalDetails/empNumber/186"
    )
def test_add_employee_with_exist_id(page: Page) -> None:
    login(page)
    employee_details(page, "layal", "f", "1111")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Employee ID already exists")).to_be_visible()
def test_add_employee_with_invalid_attachment_size(page: Page) -> None:
    login(page)
    employee_details(page, "layal", "f", "888")
    page.get_by_role("button", name="Choose File").set_input_files(
        "../../attachments/b.jpg"
    )
    page.locator("form").get_by_role("img", name="profile picture").click()
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_text("Attachment Size Exceeded")).to_be_visible()
def test_add_employee_with_valid_attachment_size(page: Page) -> None:
    login(page)
    employee_details(page, "layal", "f", "888")
    page.get_by_role("button", name="Choose File").set_input_files([])
    page.get_by_role("button").nth(4).click()
    page.get_by_role("button", name="Choose File").set_input_files(
        "../../attachments/image.png"
    )
    page.get_by_role("button", name="Save").click()
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/"
        "pim/viewPersonalDetails/empNumber/173"
    )

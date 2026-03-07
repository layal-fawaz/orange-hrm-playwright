class PimPage:
    """Page object for PIM page."""

    def __init__(self, page):
        self.page = page

    def go_to_add_employee(self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.get_by_role("link", name="Add Employee").click()

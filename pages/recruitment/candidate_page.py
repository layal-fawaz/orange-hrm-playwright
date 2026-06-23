# from playwright.sync_api import Page, expect
# from utils.decorators import pw_trace
# from data.candidate import Candidate
# from datetime import datetime
# from pages.recruitment_page import RecruitmentPage
# class CandidatePage:
#     """Page object for Candidate page"""

#     def __init__(self, page: Page):
#         self.page = page

#     @pw_trace("Candidate > Navigate to Add Candidate")
#     def go_to_add_candidate(self):
#         self.page.get_by_role("button", name="Add").click()
#         expect(self.page.get_by_role("heading", name="Add Candidate")).to_be_visible()


#     @pw_trace("Candidate > Add Candidate")
#     def add_candidate(self, candidate: Candidate):
#         self.page.get_by_placeholder("First Name").fill(candidate.first_name)
#         self.page.get_by_placeholder("Middle Name").fill(candidate.middle_name)
#         self.page.get_by_placeholder("Last Name").fill(candidate.last_name)
#         self.page.get_by_text("Vacancy").locator("..").locator("..").locator(".oxd-select-wrapper").click()
#         self.page.get_by_role("option", name=candidate.vacancy).click()
#         self.page.get_by_text("Email").locator("..").locator("..").locator(".oxd-input").fill(candidate.email)
#         self.page.get_by_text("Contact Number").locator("..").locator("..").locator(".oxd-input").fill(candidate.contact_phone)
#         if candidate.resume_path:
#             self.page.set_input_files('input[type="file"]', candidate.resume_path)
#         self.page.get_by_text("Keywords").locator("..").locator("..").locator(".oxd-input").fill(candidate.keywords)
#         self.page.get_by_placeholder("yyyy-dd-mm").fill(candidate.date_of_application)
#         self.page.get_by_text("Notes").locator("..").locator("..").locator(".oxd-textarea").fill(candidate.notes)
#         self.page.get_by_role("button", name="Save").click()
#         self.candidate_added_successfully()

#     def candidate_added_successfully(self):
#         expect(self.page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)

#     def add_candidate_to_shortlist(self):
#         self.page.get_by_role("button", name="Shortlist").click()
#         self.update_hiring_manager()    

#     def reject_candidate(self):
#         self.page.get_by_role("button", name="Reject").click()
#         self.update_hiring_manager()

#     @pw_trace("Candidate > Search Candidate")
#     def search_candidate(self, full_name):
#         self.page.get_by_text("Candidate Name").locator("..").locator("..").locator(".oxd-input").fill(full_name)
#         self.page.get_by_role("button", name="Search").click()
#         result_row = self.page.locator(".oxd-table-card").filter(has_text=full_name)
#         expect(result_row).to_be_visible(timeout=10000)
#         return result_row
        
#     def update_hiring_manager(self):
#         self.page.get_by_role("button",name="Save").click()
#         expect(self.page.get_by_text("Successfully Updated")).to_be_visible(timeout=10000)
    

#         # expect(self.page.get_by_text("Reject Candidate")).to_be_visible()


#     # @pw_trace("Candidate > Delete Candidate")
#     # def delete_candidate(self, full_name):
#     #     row = self.search_candidate(full_name)
#     #     row.locator(".bi-trash").click()
#     #     self.page.get_by_role("button", name="Yes, Delete").click()
#     #     expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()
#     def delete_candidate(self, full_name):

#        RecruitmentPage(self.page).go_to_candidate()
#        row = self.search_candidate(full_name)
#        row.locator(".bi-trash").click()
#        self.page.get_by_role("button", name="Yes, Delete").click()
#        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible()


from playwright.sync_api import Page, expect
from utils.decorators import pw_trace
from data.candidate import Candidate
from pages.recruitment_page import RecruitmentPage


class CandidatePage:
    """Page object for Candidate page"""

    def __init__(self, page: Page):
        self.page = page

    # ----------------------------
    # Navigation
    # ----------------------------
    @pw_trace("Candidate > Navigate to Add Candidate")
    def go_to_add_candidate(self):
        self.page.get_by_role("button", name="Add").click()
        expect(self.page.get_by_role("heading", name="Add Candidate")).to_be_visible()

    def go_to_candidate_list(self):
        recruitment = RecruitmentPage(self.page)
        recruitment.navigate_to_recruitment()
        recruitment.go_to_candidate()

    # ----------------------------
    # Create Candidate
    # ----------------------------
    @pw_trace("Candidate > Add Candidate")
    def add_candidate(self, candidate: Candidate):

        self.page.get_by_placeholder("First Name").fill(candidate.first_name)
        self.page.get_by_placeholder("Middle Name").fill(candidate.middle_name)
        self.page.get_by_placeholder("Last Name").fill(candidate.last_name)

        self.page.get_by_text("Vacancy").locator("..").locator("..").locator(".oxd-select-wrapper").click()
        self.page.get_by_role("option", name=candidate.vacancy).click()

        self.page.get_by_text("Email").locator("..").locator("..").locator(".oxd-input").fill(candidate.email)
        self.page.get_by_text("Contact Number").locator("..").locator("..").locator(".oxd-input").fill(candidate.contact_phone)

        if candidate.resume_path:
            self.page.set_input_files('input[type="file"]', candidate.resume_path)

        self.page.get_by_text("Keywords").locator("..").locator("..").locator(".oxd-input").fill(candidate.keywords)

        # الأفضل أن يكون format = YYYY-MM-DD
        self.page.get_by_placeholder("yyyy-dd-mm").fill(candidate.date_of_application)

        self.page.get_by_text("Notes").locator("..").locator("..").locator(".oxd-textarea").fill(candidate.notes)

        self.page.get_by_role("button", name="Save").click()

        expect(self.page.get_by_text("Successfully Saved")).to_be_visible(timeout=10000)

    # ----------------------------
    # Search Candidate
    # ----------------------------
    @pw_trace("Candidate > Search Candidate")
    def search_candidate(self, full_name: str):
        self.page.get_by_text("Candidate Name").locator("..").locator("..").locator(".oxd-input").fill(full_name)
        self.page.get_by_role("button", name="Search").click()

        return self.page.locator(".oxd-table-card").filter(has_text=full_name)

    # ----------------------------
    # Status Actions
    # ----------------------------
    def update_candidate_status(self):
        self.page.get_by_role("button", name="Save").click()
        expect(self.page.get_by_text("Successfully Updated")).to_be_visible(timeout=10000)

    def add_candidate_to_shortlist(self):
        self.page.get_by_role("button", name="Shortlist").click()
        self.update_candidate_status()

    def reject_candidate(self):
        self.page.get_by_role("button", name="Reject").click()
        self.update_candidate_status()

    # ----------------------------
    # Delete Candidate
    # ----------------------------
    @pw_trace("Candidate > Delete Candidate")
    def delete_candidate(self, full_name: str):

        self.go_to_candidate_list()

        row = self.search_candidate(full_name)
        expect(row).to_be_visible(timeout=10000)

        row.locator(".bi-trash").click()

        self.page.get_by_role("button", name="Yes, Delete").click()

        expect(self.page.get_by_text("Successfully Deleted")).to_be_visible(timeout=10000)
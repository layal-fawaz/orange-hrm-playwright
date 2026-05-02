from faker import Faker
from datetime import date

fake = Faker()

class Candidate:

    def __init__(self):
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.email = fake.email()
        self.middle_name = fake.first_name()
        self.contact_phone = fake.phone_number()

        self.vacancy = ""
        self.keywords = ""

        self.date_of_application = date.today().strftime("%Y-%m-%d")
        self.notes = ""
        self.resume_path = ""

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
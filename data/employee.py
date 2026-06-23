from faker import Faker
fake = Faker()

class Employee:
    def __init__(self):
        self.first_name = fake.first_name()
        self.middle_name = fake.first_name()
        self.last_name = fake.last_name()
        self.username = fake.user_name()
        self.password = fake.password()
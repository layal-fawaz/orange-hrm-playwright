from dataclasses import dataclass, field
from faker import Faker

fake = Faker()

@dataclass
class Vacancy:
    vacancy_name: str = field(default_factory=fake.job)
    job_title: str = "Software Engineer"
    job_description: str = field(default_factory=fake.text)
    hiring_manager: str = ""
    number_of_positions: int = field(default_factory=lambda: fake.random_int(min=1, max=99))
    active: bool = True
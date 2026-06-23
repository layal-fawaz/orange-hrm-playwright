import re
from faker import Faker

fake = Faker()

def generate_phone():
    raw = fake.phone_number()
    return re.sub(r"[^0-9+\-\/()]", "", raw)


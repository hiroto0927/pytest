EMAIL_REGEX = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
PHONE_NUM_REGEX = r"^\d{3}-\d{4}-\d{4}$"


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.email = None
        self.address = None
        self.phone_num = None

    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_address(self, address):
        self.address = address

    def set_phone_num(self, phone):
        self.phone_num = phone

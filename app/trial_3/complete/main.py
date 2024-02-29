import re

EMAIL_REGEX = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
PHONE_NUM_REGEX = r"^\d{3}-\d{4}-\d{4}$"


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.email = None
        self.address = None
        self.phone_num = None

    def set_age(self, age: int):
        if not isinstance(age, int):
            raise TypeError()

        if age < 0:
            raise ValueError()

        self.age = age

    def set_email(self, email: str):
        if email is None:
            raise ValueError()

        if not isinstance(email, str):
            raise TypeError()

        if not re.match(EMAIL_REGEX, email):
            raise ValueError()

        self.email = email

    def set_address(self, address: str):

        if address is None:
            raise ValueError()

        if not isinstance(address, str):
            raise TypeError()

        self.address = address

    def set_phone_num(self, phone_num: str):
        if phone_num is None:
            raise ValueError()

        if not isinstance(phone_num, str):
            raise TypeError()

        if not re.match(PHONE_NUM_REGEX, phone_num):
            raise ValueError()

        self.phone_num = phone_num

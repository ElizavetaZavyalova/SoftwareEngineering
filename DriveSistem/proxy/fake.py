import random
import secrets
import string

from entity.driver import Driver
from entity.passenger import Passenger

first_names = ["John", "Peter", "Michael", "Alex", "David"]
last_names = ["Smith", "Johnson", "Brown", "Williams", "Taylor"]
patronymics = ["Andrewson", "Peterson", "Williamson", "Nickolson", "Michaelson"]

def generate_email(first_name, last_name):
    domains = ["example.com", "mail.ru", "yandex.ru", "gmail.com"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"

def generate_phone():
    return f"+7{random.randint(9000000000, 9999999999)}"

def generate_password(length=10):
    return secrets.token_urlsafe(length)[:length]

def generate_address():
    streets = ["Main", "High", "Oak", "Maple", "Cedar"]
    return f"{random.randint(100, 999)} {random.choice(streets)} St, Apt {random.randint(1, 200)}"

first_name = random.choice(first_names)
last_name = random.choice(last_names)
patronymic = random.choice(patronymics)

def generate_card_number():
    def luhn_checksum(card_number):
        digits = [int(d) for d in card_number]
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        return sum(digits) % 10

    card_number = [str(random.randint(4, 5))] + [str(random.randint(0, 9)) for _ in range(14)]
    checksum = (10 - luhn_checksum(card_number + ["0"])) % 10
    return "".join(card_number) + str(checksum)


def generate_license_plate_russia():
    regions = [77, 99, 50, 90, 61]
    region_code = random.choice(regions)

    letters_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers_part = random.randint(100, 999)
    region_part = random.randint(1, 99)

    return f"{letters_part}{numbers_part} {region_part:02d}"


def generate_passenger() -> Passenger:
    dict={
        "username": first_name.lower() + str(random.randint(100, 999)),
        "email": generate_email(first_name, last_name),
        "password": generate_password(),
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "phone_number": generate_phone(),
        "home_address": generate_address(),
    }
    return Passenger(**dict)


def generate_driver() -> Driver:
    dict={
        "username": first_name.lower() + str(random.randint(100, 999)),
        "email": generate_email(first_name, last_name),
        "password": generate_password(),
        "first_name": first_name,
        "last_name": last_name,
        "patronymic": patronymic,
        "phone_number": generate_phone(),
        "home_address": generate_address(),
        "requisites": generate_card_number(),
        "car_number": generate_license_plate_russia()
    }
    return Driver(**dict)

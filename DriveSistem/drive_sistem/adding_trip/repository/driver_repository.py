from entity.account import Account
from entity.driver import Driver
from proxy.fake import generate_driver

class DriverRepository:
    def __init__(self):
        self.drivers = self.init_proxy()

    def init_proxy(self) -> dict:
        drivers = {p.email: p for p in [generate_driver() for _ in range(5)]}
        for email, driver in drivers.items():
            print(email, driver, "\n")
        return drivers

    def is_driver(self, account: Account) -> bool:
        driver = self.drivers.get(account.email)
        return driver and account.email == driver.email

    def get_account(self, account: Account) -> Driver | None:
        return self.drivers.get(account.email)
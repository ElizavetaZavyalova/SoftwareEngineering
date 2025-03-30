from entity.account import Account
from entity.passenger import Passenger
from proxy.fake import generate_passenger


class PassengerRepository:
    def __init__(self):
        self.passengers = self.init_proxy()

    def init_proxy(self) -> dict:
        passengers = {p.email: p for p in [generate_passenger() for _ in range(5)]}
        for email, driver in passengers.items():
            print(email, driver, "\n")
        return passengers

    def is_passenger(self, account: Account) -> bool:
        passenger = self.passengers.get(account.email)
        return passenger and account.email == passenger.email
    def get_account(self, account: Account) -> Passenger | None:
        return self.passengers.get(account.email)
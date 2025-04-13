from entity.user import User
from account_sistem.entity.email_confirmation import EmailConfirmation


class EmailSender:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EmailSender, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.smtp_server = "smtp.example.com"
            self.port = 587
            self._initialized = True
            print(f"Initializing SendEmail with SMTP server: {self.smtp_server} and port: {self.port}")

    def send_approve_register_email(self, email_confirmation: EmailConfirmation):
        print(
            "Sending email: " + email_confirmation.email + " approve_register_code: " + email_confirmation.confirm_code)

    def send_approve_chenge_password_email(self, email_confirmation: EmailConfirmation):
        print(
            "Sending email: " + email_confirmation.email + " approve_change_password: " + email_confirmation.confirm_code)

    def send_welcome_email(self, user: User):
        print("Sending email: " + user.email + " welcome " + user.first_name)

    def send_change_password_email(self, user: User):
        print("Sending email: " + user.email + " change_password_for: " + user.first_name)

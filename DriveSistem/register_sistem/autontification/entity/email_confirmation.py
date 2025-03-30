from pydantic import BaseModel, EmailStr


class EmailConfirmation(BaseModel):
    email: EmailStr
    confirm_code: str
    def __eq__(self, other):
        if isinstance(other, EmailConfirmation):
            return self.email == other.email and self.confirm_code == other.confirm_code
        return False
    def __hash__(self):
        return hash(self.email+self.confirm_code)

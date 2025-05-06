from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    password: str
    email: str


class login_user(BaseModel):
    password: str
    email: str

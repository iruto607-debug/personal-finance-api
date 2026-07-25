from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class FinanceBase(BaseModel):
    user_id: int
    amount: float
    description: Optional[str] = None


class FinanceCreate(FinanceBase):
    pass


class FinanceResponse(FinanceBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

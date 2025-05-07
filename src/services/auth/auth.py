from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from sqlmodel import select
from src.schemas.userSchema import UserSchema, login_user

from src.models.user import User
from typing import Any, Dict
import secrets  # better for generating tokens
from src.utils.security import HashPassword, generateJwtTokens

hash_password = HashPassword()
jwt_tokens = generateJwtTokens()


class AuthServices:
    async def create_user(self, userData: UserSchema, session: AsyncSession) -> UserSchema:
        user_data_dict = userData.model_dump()

        # Hash the password before saving
        user_data_dict["password"] = hash_password.hash_password(user_data_dict["password"])
        new_user = User(**user_data_dict)

        # Check if user already exists
        query = select(User).where(User.email == new_user.email)
        result = await session.exec(query)
        existing_user = result.first()

        if existing_user:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="User already exists."
            )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user

    async def login_user(self, userData: login_user, session: AsyncSession) -> Dict[str, Any]:
        user_data_dict = userData.model_dump()
        email = user_data_dict.get("email")
        password = user_data_dict.get("password")

        query = select(User).where(User.email == email)
        result = await session.exec(query)
        existing_user = result.first()

        if not existing_user:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="User does not exist."
            )

        # Verify hashed password
        if not hash_password.verify_password(password, existing_user.password):
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="Invalid credentials."
            )

        token = jwt_tokens.create_access_token(
            data={"sub": str(existing_user.id)}  # or "email": existing_user.email if preferred
        )
        return {
            "token": token,
            "type": "Bearer",
            "user": existing_user,
        }

from sqlmodel.ext.asyncio.session import AsyncSession
from starlette.status import HTTP_403_FORBIDDEN
from fastapi import HTTPException
from sqlmodel import select

from src.models.user import User


class AuthServices:
    async def create_user(self, userData, session: AsyncSession) -> User:
        user_data_dict = userData.model_dump()
        new_user = User(**user_data_dict)

        query = select(User).where(User.email == new_user.email)
        result = await session.exec(query)
        existing_user = result.first()

        if existing_user:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="User already exists.")

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user

from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.config.db import get_session
from src.services.auth.auth import AuthServices
from src.schemas.userSchema import UserSchema, login_user

auth_router = APIRouter()
auth_service = AuthServices()


@auth_router.post("/create-user", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserSchema, session: AsyncSession = Depends(get_session)):
    created_user = await auth_service.create_user(user_data, session)
    return created_user


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user_data: login_user, session: AsyncSession = Depends(get_session)):
    login_user = await auth_service.login_user(user_data, session)
    if not login_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return login_user

import typing as t
from fastapi import Form
from fastapi.routing import APIRouter
from sqlmodel import SQLModel

from dependencies import SupabaseDep, SessionDep, CurrentUserDep
from models import Profile

router = APIRouter(prefix="/auth")


class FormData(SQLModel):
    username: str
    password: str


@router.post("/sign-up")
async def sign_up(
    supabase: SupabaseDep, session: SessionDep, data: t.Annotated[FormData, Form()]
):
    response = supabase.auth.sign_up(
        {"email": data.username, "password": data.password}
    )
    if user := response.user:
        profile = Profile(user_id=user.id)
        session.add(profile)
        session.commit()
    return response.session


@router.get("/me")
async def me(current_user: CurrentUserDep):
    return current_user


@router.post("/sign-in")
async def sign_in(supabase: SupabaseDep, data: t.Annotated[FormData, Form()]):
    response = supabase.auth.sign_in_with_password(
        {"email": data.username, "password": data.password}
    )
    return response.session


@router.post("/sign-out")
async def sign_out(current_user: CurrentUserDep, supabase: SupabaseDep):
    supabase.auth.sign_out()
    return {"id": current_user.id}

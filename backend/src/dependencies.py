import typing as t
from sqlmodel import Session
from fastapi import Depends
from supabase import Client
from gotrue import User

from services.supabase import get_supabase_client
from db import get_session

import typing as t

from jose import JWTError, jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
    OAuth2PasswordBearer,
)
import config

ALGORITHM = "HS256"
security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")

TokenDep = t.Annotated[str, Depends(oauth2_scheme)]
SupabaseDep = t.Annotated[Client, Depends(get_supabase_client)]


def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, config.SUPABASE_JWT_SECRET, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=401, detail="Invalid authentication credentials"
            )
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication token")


def get_current_user(token: TokenDep, supabase: SupabaseDep) -> User:
    response = supabase.auth.get_user(token)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        )
    return response.user


SessionDep = t.Annotated[Session, Depends(get_session)]
CurrentUserDep = t.Annotated[User, Depends(get_current_user)]

from contextlib import asynccontextmanager
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from services.repository import Repository
from db import create_db_and_tables
from dependencies import SessionDep, CurrentUserDep
from api import auth, recipes, categories

from models import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("app startup")
    create_db_and_tables()
    yield
    print("app shutdown")


app = FastAPI(
    # root_path="/api",
    lifespan=lifespan,
)


app.include_router(auth.router)
app.include_router(recipes.router)
app.include_router(categories.router)

# app.middleware("http")
# async def add_session(request, call_next):
#     return await call_next(request)


origins = [
    # "http://localhost:8001",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(session: SessionDep):
    # print("test")
    return f"{session}" if session else "failed"


class ItemModel(BaseModel):
    title: str
    description: str | None


@app.post("/items/")
async def create_item(item: ItemModel, current_user: CurrentUserDep, db: SessionDep):
    return Repository(Recipe, db).create(
        item.model_dump(), update={"user_id": current_user.id}
    )
    # return "post items"
    # Create new item and associate it with the authenticated user
    # item.dict()
    # new_item = Item.model_validate(
    #     item,
    #     update={"user_id": current_user.id},
    #     # user_id=current_user.id,  # Use the Supabase user ID
    # )
    # db.add(new_item)
    # db.commit()
    # db.refresh(new_item)
    # return {"message": "Item created", "item": new_item}

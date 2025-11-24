from datetime import datetime
from functools import cached_property
from sqlmodel import Field, Relationship, SQLModel, func
from gotrue import User as GoTrueUser, Factor, UserIdentity
from pydantic import ConfigDict

import uuid
import typing as t

from services.supabase import supabase_client


class TimeStampModel(SQLModel):
    __abstract__ = True
    __table_args__ = {"schema": "public"}

    created_at: datetime = Field(default_factory=func.now)
    updated_at: datetime = Field(
        default_factory=func.now, sa_column_kwargs={"onupdate": func.now()}
    )


# class User(GoTrueUser, SQLModel, table=True):
#     profile: "Profile" = Relationship(
#         back_populates="user",
#         sa_relationship_kwargs={"uselist": False},
#     )

# class _User(SQLModel, GoTrueUser):
#     __abstract__ = True
#     __tablename__ = "users"
#     __table_args__ = {"schema": "public"}


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: uuid.UUID = Field(primary_key=True)
    # app_metadata: dict[str, t.Any]
    # user_metadata: dict[str, t.Any]
    # aud: str = Field()
    # confirmation_sent_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # recovery_sent_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # email_change_sent_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # new_email: t.Optional[str] = Field(nullable=True, default=None)
    # new_phone: t.Optional[str] = Field(nullable=True, default=None)
    # invited_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # action_link: t.Optional[str] = Field(nullable=True, default=None)
    # email: t.Optional[str] = Field(nullable=True, default=None)
    # phone: t.Optional[str] = Field(nullable=True, default=None)
    # confirmed_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # email_confirmed_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # phone_confirmed_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # last_sign_in_at: t.Optional[datetime] = Field(nullable=True, default=None)
    # role: t.Optional[str] = Field(nullable=True, default=None)
    # # identities: t.Optional[list[UserIdentity]] = Field(nullable=True, default=None)
    # is_anonymous: bool = Field(default=False)
    # # factors: t.Optional[list[Factor]] = Field(nullable=True, default=None)

    # profile: "Profile" = Relationship(
    #     back_populates="user",
    #     sa_relationship_kwargs={"uselist": False},
    # )


class Profile(TimeStampModel, table=True):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    user_id: uuid.UUID = Field(
        primary_key=True,
        unique=True,
        nullable=False,
        foreign_key="auth.users.id",
        ondelete="CASCADE",
    )

    @cached_property
    def user(self):
        return None
        # return supabase_client.auth.admin.get_user_by_id(self.user_id).user
    
    profile_picture_url: str | None = Field(default=None)

    # followers: list["Profile"] = Relationship(
    #     back_populates="following",
    #     sa_relationship_kwargs={
    #         "secondary": "user_follower",
    #         "primaryjoin": "Profile.user_id == UserFollower.followed_id",
    #         "secondaryjoin": "Profile.user_id == UserFollower.follower_id",
    #     },
    # )

    # following: list["Profile"] = Relationship(
    #     back_populates="followers",
    #     sa_relationship_kwargs={
    #         "secondary": "user_follower",
    #         "primaryjoin": "Profile.user_id == UserFollower.follower_id",
    #         "secondaryjoin": "Profile.user_id == UserFollower.followed_id",
    #     },
    # )

    recipes: list["Recipe"] | None = Relationship(back_populates="user")
    comments: list["Comment"] | None = Relationship(back_populates="user")
    likes: list["Like"] | None = Relationship(back_populates="user")


class Category(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    description: str | None = Field(default=None, nullable=True)
    ingredients: list["Ingredient"] = Relationship(back_populates="category")
    recipes: list["Recipe"] = Relationship(back_populates="category")


class RecipeIngredient(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str = Field(nullable=True)
    recipe_id: int = Field(
        primary_key=True, foreign_key="public.recipe.id", ondelete="CASCADE"
    )
    ingredient_id: int = Field(
        primary_key=True, foreign_key="public.ingredient.id", ondelete="CASCADE"
    )


class Ingredient(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    description: str = Field(nullable=True)
    category_id: int | None = Field(
        default=None,
        nullable=True,
        foreign_key="public.category.id",
        ondelete="SET NULL",
    )
    category: Category = Relationship(back_populates="ingredients")
    recipes: list["Recipe"] = Relationship(
        back_populates="ingredients", link_model=RecipeIngredient
    )


class Recipe(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    description: str = Field(nullable=True)
    user_id: uuid.UUID = Field(foreign_key="public.profile.user_id", ondelete="CASCADE")
    user: Profile = Relationship(back_populates="recipes")
    ingredients: list[Ingredient] = Relationship(
        back_populates="recipes", link_model=RecipeIngredient
    )
    category_id: int | None = Field(
        foreign_key="public.category.id",
        nullable=True,
        ondelete="SET NULL",
        default=None,
    )
    category: Category = Relationship(back_populates="recipes")
    comments: list["Comment"] = Relationship(back_populates="recipe")
    likes: list["Like"] = Relationship(back_populates="recipe")


class Followers(TimeStampModel, table=True):
    follower_id: uuid.UUID = Field(
        primary_key=True, foreign_key="public.profile.user_id"
    )
    followed_id: uuid.UUID = Field(
        primary_key=True, foreign_key="public.profile.user_id"
    )


class Comment(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="public.profile.user_id", ondelete="CASCADE")
    user: Profile = Relationship(back_populates="comments")
    recipe_id: int = Field(foreign_key="public.recipe.id", ondelete="CASCADE")
    recipe: Recipe = Relationship(back_populates="comments")
    comment: str = Field()
    parent_id: int | None = Field(
        default=None, foreign_key="public.comment.id", nullable=True, ondelete="CASCADE"
    )


class Like(TimeStampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: uuid.UUID = Field(primary_key=True, foreign_key="public.profile.user_id")
    user: Profile = Relationship(back_populates="likes")
    recipe_id: int = Field(foreign_key="public.recipe.id", ondelete="CASCADE")
    recipe: Recipe = Relationship(back_populates="likes")

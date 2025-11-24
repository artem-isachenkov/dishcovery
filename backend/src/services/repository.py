import typing as t
from sqlmodel import SQLModel, Session, select

TOut = t.TypeVar("TOut", bound=SQLModel)
TIn = t.TypeVar("TIn", dict, SQLModel)


class Repository(t.Generic[TOut]):
    def __init__(self, model: t.Type[TOut], session: Session):
        self.model = model
        self.session = session

    def create(self, obj: TIn, update: dict | None = None) -> TOut:
        new_obj = self.model.model_validate(obj, update=update)
        self.session.add(new_obj)
        self.session.commit()
        self.session.refresh(new_obj)
        return new_obj

    def read(self, obj_id: int) -> t.Optional[TOut]:
        return self.session.get(self.model, obj_id)

    def read_all(self) -> list[TOut]:
        statement = select(self.model)
        results = self.session.exec(statement)
        return results.all()

    def update(self, obj: TIn) -> TOut:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def delete(self, obj_id: int) -> bool:
        obj = self.session.get(self.model, obj_id)
        if obj:
            self.session.delete(obj)
            self.session.commit()
            return True
        return False

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..auth import get_client
from ..db import get_session
from ..schemas.category import Category, CategoryCreate, CategoryRead

TAG_NAME = "Category"
tag = {
    "name": TAG_NAME,
    "description": "Create and manage payment entry categories",
}

category_router = APIRouter(
    prefix="/category",
    tags=[TAG_NAME],
    dependencies=[Depends(get_client)],
    responses={404: {"description": "Not found"}},
)


@category_router.post("", response_model=CategoryRead, tags=[TAG_NAME])
def create_category(
    *, session: Session = Depends(get_session), category: CategoryCreate
):
    db_category = Category.from_orm(category)
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


@category_router.get("", response_model=list[CategoryRead], tags=[TAG_NAME])
def read_categories(*, session: Session = Depends(get_session)):
    categories = session.exec(select(Category)).all()
    return categories


@category_router.patch("", response_model=CategoryRead, tags=[TAG_NAME])
def update_category(*, session: Session = Depends(get_session), category: Category):
    session.merge(category)
    session.commit()
    session.refresh(category)
    return category


# TODO: Think about how this should work
# @category_router.delete("/{id}", tags=[TAG_NAME])
# def delete_category(*, session: Session = Depends(get_session), id: int):
#     category = session.query(Category).get(id)
#     if category is None:
#         raise HTTPException(status_code=404, detail="Category not found")
#     session.delete(category)
#     session.commit()

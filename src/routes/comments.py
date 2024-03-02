from typing import List

from fastapi import Depends, APIRouter, status, HTTPException
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.schemas import CommentBase, CommentResponse
from src.database.models import User, Comment, Picture

import src.repository.comments as comments_repo

from src.services.exceptions_func import no_comment_exception, no_picture_exception


router = APIRouter(
    prefix="/{picture_id}/comments", tags=["comments"]
)  # ??? do komentarzy chyba trzeba uderzać z poziomu zdjęcia picture/{picture_id}/


@router.get("/", response_model=List[CommentResponse])
async def display_all_comments(
    picture_id: int, db: Session = Depends(get_db)
) -> List[Comment]:
    # to może zrobić każdy
    no_picture_exception(picture_id, db)
    comments = await comments_repo.get_comments(db, picture_id)
    return comments


@router.post("/", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
async def add_new_comment(
    picture_id: int, body: CommentBase, db: Session = Depends(get_db)
) -> Comment:
    # to docelowo może zrobić każdy zalogowany użytkownik ale na razie każdy
    no_picture_exception(picture_id, db)
    new_comment = await comments_repo.create_new_comment(body, db, picture_id)
    return new_comment


@router.get("/{comment_id}", response_model=CommentResponse)
async def display_comment(comment_id: int, db: Session = Depends(get_db)):
    no_comment_exception(comment_id, db)
    comment = await comments_repo.get_comment(db, comment_id)
    return comment


@router.put(
    "/{comment_id}",
    response_model=CommentResponse,
)
async def edit_comment(
    comment_id: int, body: CommentBase, db: Session = Depends(get_db)
) -> Comment:
    no_comment_exception(comment_id, db)
    updated_comment = await comments_repo.edit_comment(body, db, comment_id)
    return updated_comment


@router.delete(
    "/{comment_id}",
    response_model=CommentResponse,
)
async def delete_comment(comment_id: int, db: Session = Depends(get_db)) -> Comment:
    no_comment_exception(comment_id, db)
    deleted_comment = await comments_repo.delete_comment(db, comment_id)
    return deleted_comment


# def no_picture_exception(func):
#     async def inner(picture_id: int, db: Session = Depends(get_db)):
#         picture = db.query(Picture).filter(Picture.id == picture_id).first()
#         if bool(picture):
#             result = await func(picture_id, db)
#             return result
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#     return inner
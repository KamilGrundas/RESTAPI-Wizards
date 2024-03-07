from typing import List, Dict

from sqlalchemy.orm import Session

from src.schemas import CommentBase, PictureBase
from src.database.models import Comment, Picture
from src.schemas import PictureResponse, PictureResponseDetails

from fastapi import Depends
from src.database.db import get_db


from fastapi import Depends, HTTPException, status


async def copy_picture_from_cloudinary_to_database(cloudinary_result, description, db):

    try:
        file_url = cloudinary_result["file_url"]
        public_id = cloudinary_result["public_id"]
    except:
        database_result = HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY, headers=cloudinary_result
        )
    else:
        database_result = await add_picture(
            url=file_url, public_id=public_id, description=description, db=db
        )

    return database_result


async def add_picture(
    url: str, public_id: str, description: str, db: Session
) -> Picture:
    new_picture = Picture(url=url, public_id=public_id, description=description)
    db.add(new_picture)
    db.commit()
    db.refresh(new_picture)
    return new_picture


async def add_tag(picture_id: int, db: Session):
    pass


async def get_picture(picture_id: int, db: Session):
    picture = db.query(Picture).filter(Picture.id == picture_id).first()
    return picture


async def get_picture_details(picture_id: int, db: Session):
    picture = db.query(Picture).filter(Picture.id == picture_id).first()

    return picture


async def delete_picture(picture_id: int, db: Session):
    picture = db.query(Picture).filter(Picture.id == picture_id).first()
    picture.is_deleted = True
    db.commit()
    db.refresh(picture)
    return picture


async def edit_description(picture_id: int, db: Session):
    pass


async def get_pictures(db: Session) -> List[Picture]:
    pictures = db.query(Picture).filter(Picture.is_deleted == False).all()
    return pictures


async def get_pictures_id_url(db: Session) -> List[Dict]:
    pictures = db.query(Picture).all()
    id_url = []
    for picture in pictures:
        id_url.append({"id": picture.id})

    print(id_url)

    return id_url


async def get_urls(db: Session) -> List[str]:
    pass


async def change_url(new_url, public_id, db: Session = Depends(get_db)) -> Picture:
    pass
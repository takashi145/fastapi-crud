from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas.post import Post, PostCreate
from cruds import post_crud

post_router = APIRouter(
    prefix="/posts",
    tags=["post"]
)

@post_router.post("/", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Create a new post and add it to the database.
    """
    return post_crud.create_post(db, post)


@post_router.get("/", response_model=List[Post], status_code=status.HTTP_200_OK)
def read_posts(db: Session = Depends(get_db)):
    """
    Retrieve all posts from the database.
    """
    return post_crud.get_posts(db)


@post_router.get("/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
def read_post(post_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific post by its ID.
    """
    post = post_crud.get_post(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@post_router.put("/{post_id}", response_model=Post, status_code=status.HTTP_200_OK)
def update_post(post_id: int, post: PostCreate, db: Session = Depends(get_db)):
    """
    Update a specific post by its ID.
    """
    return post_crud.update_post(db, post_id, post)


@post_router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific post by its ID.
    """
    post_crud.delete_post(db, post_id=post_id)

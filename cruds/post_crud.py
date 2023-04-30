from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.post import Post
from schemas.post import PostCreate


def get_posts(db: Session):
    """
    Retrieve all posts from the database.
    """
    return db.query(Post).all()


def create_post(db: Session, post: PostCreate):
    """
    Create a new post and add it to the database.
    """
    new_post = Post(title=post.title, description=post.description)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_post(db: Session, post_id: int):
    """
    Retrieve a specific post by its ID.
    """
    return db.query(Post).filter(Post.id == post_id).first()


def update_post(db: Session, post_id: int, post: PostCreate):
    """
    Update a specific post by its ID.
    """
    post_model = db.query(Post).filter(Post.id == post_id).first()

    if post_model is None:
        raise_not_found_exception()

    post_model.title = post.title
    post_model.description = post.description

    db.add(post_model)
    db.commit()
    return post_model


def delete_post(db: Session, post_id: int):
    """
    Delete a specific post by its ID.
    """
    post_model = db.query(Post).filter(Post.id == post_id).first()

    if post_model is None:
        raise_not_found_exception()

    db.delete(post_model)
    db.commit()
    return


def raise_not_found_exception():
    """
    Raise a not found exception for a post.
    """
    raise HTTPException(status_code=404, detail="Post not found")

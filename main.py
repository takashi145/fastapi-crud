from fastapi import FastAPI
from models import Base
from database import engine
from routers.post_router import post_router

app_settings = {
    "title": "Crud Api",
    "debug": False,
    "version": "0.1.0"
}

app = FastAPI(**app_settings)

app.include_router(post_router)


# @app.get("/")
# def read_root():
#     """
#     Return a simple Hello World message.
#     """
#     return {"message": "Hello World"}


Base.metadata.create_all(engine)

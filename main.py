from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db.session import engine
from db.base import Base
from api.base import api_router


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def create_templates(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI()
    create_tables()
    include_router(app)
    create_templates(app)
    return app


app = start_application()

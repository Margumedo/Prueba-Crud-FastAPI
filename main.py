from fastapi import FastAPI
from app.routes.user import router as users
from app.routes.product import router as produts
from app.routes.order import router as orders
from app.db.database import Base, engine
from app.db import models
from starlette.responses import RedirectResponse

app = FastAPI(
    title= "My second FASTAPI",
    description="Esta es mi segunda practica con FastAPI",
    version="1.0.0",
    openapi_tags=[{"name":"Users", "description":"user routes"},{"name":"Products", "description": "producrs routes"}]
)

def include_routes():

    routers = [users, produts, orders]

    for router in routers:
        app.include_router(router)

include_routes()

def create_tables():
    models.Base.metadata.create_all(bind=engine)
    print("Creo las tablas en BD")

create_tables()

@app.get("/")
async def doc():
    return RedirectResponse(url="docs")

@app.get("/home")
async def home():
    return {"Messaje":"Welcome to your fucking API Working"}

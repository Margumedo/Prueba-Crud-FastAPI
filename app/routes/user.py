from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db import models
from app.schemas.schemas import UserBase, ShowUser, UpdateUser
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get("/", response_model=List[ShowUser], status_code=200)
async def get_users(db: Session = Depends(get_db), skip: int=0, limit: int=100 ):
    users = db.query(models.User).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code=404, detail="No se encontro data")
    return users

@router.get("/{user_id}", response_model=ShowUser, status_code=200 )
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter_by(id = user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/product/{product_id}", response_model=List[ShowUser], status_code=200)
async def get_users_by_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    users = product.users
    return users

@router.post("/", status_code=201)
async def create_user( user: UserBase , db: Session = Depends(get_db)):
    find_user = db.query(models.User).filter(models.User.username == user.username or models.User.email == user.email ).first()
    if find_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario o email ya existe")
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"Message":"Usuario Creado con exito!",
            "user": new_user}

@router.patch("/{user_id}", status_code=202)
async def update_user(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    find_user= db.query(models.User).filter(models.User.id == user_id)
    if not find_user:
        raise HTTPException(status_code=202, detail="Usuario no encontrado")
    find_user.update(user.model_dump(exclude_unset=True))
    db.commit()
    return {"Message":"Usuario actualizado con exito"}

@router.delete("/{user_id}", status_code=200)
async def detele_user(user_id: int, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"Message":"Usuario Borrado con Exito!"}
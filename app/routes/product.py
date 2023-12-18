from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Product, User
from typing import List
from app.schemas.schemas import ShowProduct, ProductBase, UpdateProduct

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)



@router.get("/", response_model=List[ShowProduct], status_code=200)
async def get_products(db: Session = Depends(get_db)):
    producst = db.query(Product).all()
    if not producst:
        raise HTTPException(status_code=404, detail="No se encontraron products")
    return producst

@router.get("/{user_id}", response_model=List[ShowProduct], status_code=200)
async def get_products_buy_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    products = user.products
    return products

@router.post("/")
async def create_product(product: ProductBase, db: Session= Depends(get_db)):
    new_product = Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.patch("/{product_id}", status_code=202)
async def update_product(product_id: int, product: UpdateProduct  ,db: Session = Depends(get_db)):
    db_product = db.query(Product).filter(Product.id == product_id)
    if not db_product.first():
        raise HTTPException(status_code=404, detail="No se encontro el producto")
    db_product.update(product.model_dump(exclude_unset=True))
    db.commit()
    return {"Message":"Producto actualizado"}

@router.delete("/{product_id}", status_code=200)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product=db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="No se encontro el product")
    db.delete(product)
    db.commit()
    return {"Message":"Producto borrado con exito"}





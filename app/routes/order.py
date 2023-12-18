from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.models import User, Product, Order, OrderDetail
from datetime import datetime
from app.schemas.schemas import ProductOrder, ShowOrder
from typing import List


router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/{user_id}", response_model=ShowOrder, status_code=201)
async def create_order(user_id: int, order_data: List[ProductOrder], db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail=("Usuario no encontrado"))
    
    products = db.query(Product).filter(Product.id.in_([product.product_id for product in order_data])).all()
    if len(products) != len(order_data):
        raise HTTPException(status_code=404, detail="Algunos de los productos no se encontraron")

    new_order = Order(
        user_id = user_id,
        status = "Pendiente",
        total = 0
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    #Lista para almacenar los detalles del pedido(OrderDetail)
    order_details = []
    total = 0

    for product in order_data:
        new_product = next((p for p in products if p.id == product.product_id), None)
        if not new_product:
            raise HTTPException(status_code=404, detail=f"El producto de ID {product.product_id} no fue encontrado")
        
        order_detail = OrderDetail(
            order_id = new_order.id, 
            product_id = new_product.id, 
            quantity = product.quantity, 
            unit_price = new_product.amount 
            )
        #agregar la asociacion entre user y products
        user.products.append(new_product)

        order_details.append(order_detail)
        total = total + new_product.amount * product.quantity

    
    db.add_all(order_details)
    db.commit()

    new_order.total = total
    db.commit()
    db.refresh(new_order)
    return new_order
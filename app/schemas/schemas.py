from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime



class ProductBase(BaseModel):
    name: str
    amount: float
    brand: str
    items: int
    weight: float
    
    

class ShowProduct(BaseModel):
    id : int
    name : str
    amount : float
    brand : str
    items : int
    weight : float
    create : datetime
    update : Optional[datetime]


class UpdateProduct(BaseModel):

    name: str = None
    amount: float = None
    brand: str = None
    items: int = None 
    weight: float = None


class UserBase(BaseModel):

    
    username: str = Field(default="User", examples=["Nombre de usuario unico"])
    name: str = Field(default="usuario", examples=["Tu nombre",])
    lastname: Optional[str]
    password: str = Field(default="1234")
    email: str
    is_active: Optional[bool] = Field(default=False)
    
    

    class config():
        orm_mode = True
    

class ShowUser(BaseModel):

    id: int
    username: str
    name: Optional[str]
    lastname: Optional[str]
    email: str
    is_active: bool
    create: datetime
    update: Optional[datetime]
    products: List[ProductBase]
    

class UpdateUser(BaseModel):

    username: str = None
    name: str = None
    lastname: str = None
    password: str = None
    email: str = None
    is_active: bool = None

    class config():
        orm_mode = True

#clases para mi payload

class ProductOrder(BaseModel):
    product_id: int
    quantity: int 

    class config():
        orm_mode = True

class CreateOrder(BaseModel):
    user_id: int
    products: List[ProductOrder]

class ShowOrder(BaseModel):
    id: int
    user_id: int
    status: str
    total: float
    create: datetime
    update: Optional[datetime]
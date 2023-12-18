from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey, Table
from datetime import datetime
from app.db.database import Base
from sqlalchemy.orm import relationship


#defino mi relacion muchos a muchos entre User y Product

user_product_association = Table(
    'user_product_association',
    Base.metadata,
    Column("user_id", Integer, ForeignKey('users.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, nullable=True, unique=True)
    name = Column(String)
    lastname = Column(String)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, default=False)
    create = Column(DateTime, default=datetime.now)
    update = Column(DateTime, onupdate=datetime.now)

    #relacion uno a muchos con order
    Orders = relationship("Order", backref="orders")
    
    #relacion muchos a muchos con products
    products = relationship("Product", secondary=user_product_association, backref="users" )

class Product(Base):
    __tablename__= "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    brand = Column(String)
    items = Column(Integer)
    weight = Column(Float)
    create = Column(DateTime, default=datetime.now)
    update = Column(DateTime, onupdate=datetime.now)

    #relacion muchos a muchos con User ya definida en el backref

    # relacion uno a muchos con order details
    order_details = relationship("OrderDetail", backref="products")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)
    total = Column(Float)
    create = Column(DateTime, default=datetime.now)
    update = Column(DateTime, onupdate=datetime.now)

    #relacion uno a muchos con detalles de pedido
    order_detail = relationship("OrderDetail", backref="orders")

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id") )
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    unit_price = Column(Integer)
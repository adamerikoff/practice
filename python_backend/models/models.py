from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Enterprise(Base):
    __tablename__ = 'enterprises'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, default='')
    location = Column(String, default='')
    business_hours = Column(String, default='9:00 - 18:00')

    products = relationship("Product", back_populates="enterprise", cascade="all, delete-orphan", uselist=True)

    def __repr__(self):
        return f"<Enterprise(id={self.id}, name='{self.name}', description='{self.description}', location='{self.location}', business_hours='{self.business_hours}')>"


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, default='')
    price = Column(Float, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)

    enterprise_id = Column(Integer, ForeignKey('enterprises.id'))

    enterprise = relationship("Enterprise", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', description='{self.description}', price={self.price}, quantity_in_stock={self.quantity_in_stock})>"



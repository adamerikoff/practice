from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.models import Product
from schemas.product_schema import ProductCreate, ProductUpdate, ProductBase, ProductInDB

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.get("/", response_model=List[ProductBase])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Получает список продуктов.

    :param skip: Количество пропускаемых записей (по умолчанию 0).
    :param limit: Максимальное количество возвращаемых записей (по умолчанию 10).
    :param db: Сессия базы данных.
    :return: Список продуктов (см. схему ProductBase).
    """
    products = db.query(Product).offset(skip).limit(limit).all()
    return products


@router.get("/{product_id}", response_model=ProductBase)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Получает информацию о продукте по его идентификатору.

    :param product_id: Идентификатор продукта.
    :param db: Сессия базы данных.
    :return: Информация о продукте (см. схему ProductBase).
    """
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductBase)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Создает новый продукт.

    :param product: Данные для создания продукта (см. схему ProductCreate).
    :param db: Сессия базы данных.
    :return: Созданный продукт (см. схему ProductBase).
    """
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put("/{product_id}", response_model=ProductInDB)
async def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """
    Обновляет информацию о продукте.

    :param product_id: Идентификатор продукта.
    :param product: Новые данные для продукта (см. схему ProductUpdate).
    :param db: Сессия базы данных.
    :return: Обновленная информация о продукте (см. схему ProductInDB).
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for attr, value in product.dict().items():
        if attr != "id":  # Skip updating the ID
            setattr(db_product, attr, value)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Удаляет продукт.

    :param product_id: Идентификатор продукта.
    :param db: Сессия базы данных.
    :return: Сообщение об успешном удалении продукта.
    """
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}


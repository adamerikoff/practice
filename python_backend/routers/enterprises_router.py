from fastapi import APIRouter, Depends, HTTPException

from typing import List
from sqlalchemy.orm import Session

from models.models import Enterprise, Product
from database import get_db
from schemas.enterprise_schema import EnterpriseBase, EnterpriseCreate, EnterpriseInDB, EnterpriseUpdate
from schemas.product_schema import ProductBase

router = APIRouter(
    prefix="/enterprises",
    tags=["enterprises"]
)

@router.get("/", response_model=List[EnterpriseInDB])
async def read_enterprises(db: Session = Depends(get_db)):
    """
    Получает список всех предприятий.

    :param db: Сессия базы данных.
    :return: Список всех предприятий.(см. схему EnterpriseInDB).
    """
    return db.query(Enterprise).all()


@router.get("/{enterprise_id}", response_model=EnterpriseBase)
async def read_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    """
    Получает информацию о предприятии по его идентификатору.

    :param enterprise_id: Идентификатор предприятия.
    :param db: Сессия базы данных.
    :return: Информация о предприятии.(см. схему EnterpriseBase).
    """
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise


@router.post("/", response_model=EnterpriseBase)
async def create_enterprise(enterprise: EnterpriseCreate, db: Session = Depends(get_db)):
    """
    Создает новое предприятие.

    Тело запроса:
    - name (строка, обязательный): Название предприятия.
    - description (строка, опциональный): Описание предприятия.
    - location (строка, опциональный): Местоположение предприятия.
    
    :param enterprise: Данные для создания предприятия.
    :param db: Сессия базы данных.
    :return: Созданное предприятие.(см. схему EnterpriseBase).
    """
    db_enterprise = Enterprise(**enterprise.model_dump())
    db.add(db_enterprise)
    db.commit()
    db.refresh(db_enterprise)
    return db_enterprise


@router.put("/{enterprise_id}", response_model=EnterpriseInDB)
async def update_enterprise(enterprise_id: int, enterprise: EnterpriseUpdate, db: Session = Depends(get_db)):
    """
    Обновляет информацию о предприятии.

    Тело запроса:(см. схему EnterpriseUpdate).
    - name (строка, опциональный): Новое название предприятия.
    - description (строка, опциональный): Новое описание предприятия.
    - location (строка, опциональный): Новое местоположение предприятия.
    
    :param enterprise_id: Идентификатор предприятия.
    :param enterprise: Новые данные для предприятия.
    :param db: Сессия базы данных.
    :return: Обновленная информация о предприятии.(см. схему EnterpriseInDB).
    """
    db_enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not db_enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    for attr, value in vars(enterprise).items():
        if attr != "id":
            setattr(db_enterprise, attr, value) if value else None
    db.commit()
    db.refresh(db_enterprise)
    return db_enterprise


@router.delete("/{enterprise_id}")
async def delete_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    """
    Удаляет предприятие.

    :param enterprise_id: Идентификатор предприятия.
    :param db: Сессия базы данных.
    :return: Сообщение об успешном удалении предприятия.
    """
    db_enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not db_enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    db.delete(db_enterprise)
    db.commit()
    return {"message": "Enterprise deleted successfully"}


@router.get("/{enterprise_id}/products", response_model=List[ProductBase])
async def read_enterprise_products(enterprise_id: int, db: Session = Depends(get_db)):
    """
    Получает список продуктов, связанных с определенным предприятием.

    :param enterprise_id: Идентификатор предприятия.
    :param db: Сессия базы данных.
    :return: Список продуктов, связанных с предприятием (см. схему ProductBase).
    """
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if enterprise is None:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise.products
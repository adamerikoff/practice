from fastapi import APIRouter, Depends, HTTPException

from typing import List
from sqlalchemy.orm import Session
from models.models import Enterprise, Product
from database import get_db
from schemas.enterprise_schema import EnterpriseBase, EnterpriseCreate, EnterpriseInDB, EnterpriseUpdate

router = APIRouter(
    prefix="/enterprises",
    tags=["enterprises"]
)


@router.get("/", response_model=List[EnterpriseBase])
async def read_enterprises(db: Session = Depends(get_db)):
    return db.query(Enterprise).all()


@router.get("/{enterprise_id}", response_model=EnterpriseBase)
async def read_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise


@router.post("/", response_model=EnterpriseBase)
async def create_enterprise(enterprise: EnterpriseCreate, db: Session = Depends(get_db)):
    db_enterprise = Enterprise(**enterprise.model_dump())
    db.add(db_enterprise)
    db.commit()
    db.refresh(db_enterprise)
    return db_enterprise


@router.put("/{enterprise_id}", response_model=EnterpriseInDB)
async def update_enterprise(enterprise_id: int, enterprise: EnterpriseUpdate, db: Session = Depends(get_db)):
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
    db_enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not db_enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    db.delete(db_enterprise)
    db.commit()
    return {"message": "Enterprise deleted successfully"}


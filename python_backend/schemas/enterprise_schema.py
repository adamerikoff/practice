from pydantic import BaseModel
from typing import Optional

class EnterpriseBase(BaseModel):
    name: str
    description: Optional[str] = ""
    location: Optional[str] = ""
    business_hours: Optional[str] = "9:00 - 18:00"

class EnterpriseCreate(EnterpriseBase):
    pass

class EnterpriseUpdate(EnterpriseBase):
    pass

class EnterpriseInDB(EnterpriseBase):
    id: int

    class Config:
        orm_mode = True

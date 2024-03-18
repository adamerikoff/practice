from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Enterprise(Base):
    __tablename__ = 'enterprises'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String, default='')
    location = Column(String, default='')
    business_hours = Column(String, default='9:00 - 18:00')

    def __repr__(self):
        return f"<Enterprise(id={self.id}, name='{self.name}', description='{self.description}', location='{self.location}', business_hours='{self.business_hours}')>"

    


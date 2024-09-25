from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Car(Base):
    __tablename__ = 'Car'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    marka = Column(String(90), nullable=False)
    model = Column(String(90), nullable=False)
    rok_produkcji = Column(Integer, nullable=False)


class CarRating(Base):
    __tablename__ = 'Car_Rating'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('Car.ID'), nullable=False)
    ocena = Column(Integer, nullable=False)
    
    __table_args__ = (
        CheckConstraint('ocena >= 1 AND ocena <= 5'),
    )

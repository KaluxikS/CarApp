from sqlalchemy.orm import Session
from models import Car, CarRating
from schemas import CarBase, CarRatingBase
from sqlalchemy import func

def create_car(db: Session, car: CarBase):
    db_car = Car(marka = car.marka, model = car.model, rok_produkcji = car.rok_produkcji)
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.ID == car_id).first()

def add_rating(db: Session, car_id: int, ocena: CarRatingBase):
    db_rate = CarRating(car_id = car_id, ocena = ocena.ocena)
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate

def get_top10_cars(db: Session):
    return db.query(Car.ID, Car.marka, Car.model, Car.rok_produkcji,
                     func.avg(CarRating.ocena).label('avg_rate')).join(CarRating)\
                     .group_by(Car.ID).order_by(func.avg(CarRating.ocena).desc())\
                     .limit(10).all()
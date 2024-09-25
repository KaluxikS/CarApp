from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from database import engine, SessionLocal
import schemas, crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/cars/', response_model=schemas.CarBase)
def create_car(car: schemas.CarBase, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)

@app.post('/cars/{car_id}/rate')
def add_rating(car_id: int, ocena: schemas.CarRatingBase, db: Session = Depends(get_db)):
    db_car = crud.get_car(db, car_id=car_id)

    #checking if car with {car_id} exists
    if not db_car:
        raise HTTPException(status_code=404, detail="Nie znaleziono Samochodu")
    
    crud.add_rating(db=db, car_id=car_id, ocena=ocena)
    return {"message": "Ocena dodana"}

@app.get('/cars/top10')
def get_top_10(db: Session = Depends(get_db)):
    top_cars = crud.get_top10_cars(db)
    result = []
    for car in top_cars:
        result.append(
            {
                'id': car.ID,
                'marka': car.marka,
                'model': car.model,
                'rok_produkcji': car.rok_produkcji,
                'srednia_ocena': car.avg_rate
            }
        )
    return result

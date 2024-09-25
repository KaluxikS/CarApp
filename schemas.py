from pydantic import BaseModel, Field, field_validator

class CarBase(BaseModel):
    marka: str
    model: str
    rok_produkcji: int

    @field_validator('rok_produkcji', mode='before')
    def validate_rok_produkcji(cls, v):
        if v < 1850 or v > 2024:
            raise ValueError('Bledny rok produkcji. Musi być w zakresie ')
        return v
    
class CarRatingBase(BaseModel):
    ocena: int = Field(ge=1, le=5)
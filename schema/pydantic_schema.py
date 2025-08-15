from datetime import date
from pydantic import BaseModel

class KiBase(BaseModel):
    ki_number: int
    start_date: date
    end_date: date

class KiResponse(KiBase):
    id: int

class Config:
    # SQLAlchemyモデルから変換するために必要
    from_attributes = True

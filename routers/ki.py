from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.database import get_db
from schema import pydantic_schema
from crud import ki as crud_ki

router = APIRouter()

@router.get("/kis", response_model=list[pydantic_schema.KiResponse])
def read_all_kis(db: Session = Depends(get_db)):
    return crud_ki.get_all_kis(db)

@router.get("/ki/{ki_number}", response_model=pydantic_schema.KiResponse)
def read_ki(ki_number: int, db: Session = Depends(get_db)):
    db_ki = crud_ki.get_ki(db, ki_number)
    if db_ki is None:
        raise HTTPException(status_code=404, detail="Ki not found")
    return db_ki

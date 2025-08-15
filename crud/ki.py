from sqlalchemy.orm import Session
from schema import models



def get_ki(db: Session, ki_number: int):
    return db.query(models.Ki).filter(models.Ki.ki_number == ki_number).first()

def get_all_kis(db: Session):
    return db.query(models.Ki).order_by(models.Ki.ki_number).all()

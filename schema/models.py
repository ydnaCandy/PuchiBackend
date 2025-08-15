from sqlalchemy import Column, Integer, Date
from schema.database import Base

class Ki(Base):
    __tablename__ = "kis"

    id = Column(Integer, primary_key=True, index=True)
    ki_number = Column(Integer, unique=True, index=True)  # 期の番号
    start_date = Column(Date)
    end_date = Column(Date)
